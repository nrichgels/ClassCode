"""cs1graphics.py

Copyright 2007, David Letscher and Michael H. Goldwasser

Go to www.cs1graphics.org for more information.

Version 1.0:  12/19/2007
"""

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#  
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#  
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
    
# Configuration options
_debug = 0                # can be 0, 1, 2 or 3

import copy as _copy
import math as _math
import random as _random
import Queue as _Queue
import time as _time
import threading as _threading
import thread as _thread
import atexit as _atexit

try:
  set                              # Python 2.4 or later
except:
  try:
    from sets import Set as set    # Python 2.3 compatibility
  except:
    raise RuntimeError('Cannot find set class;  Use Python 2.3 or later')

_ourRandom = _random.Random()
_ourRandom.seed(1234)     # initialize the random seed so that treatment of equal depths is reproducible

# Beginning of library
_underlyingLibrary = None

class _GraphicsManager:
  def __init__(self):
    self._running = True
    
    # Synchornization mechanisms
    self._commandQueue = _Queue.Queue()
    self._releaseQueue = _Queue.Queue()   # For blocking commands on the queue
    self._eventQueue = _Queue.Queue()
    self._refreshLock = _threading.Lock()
    
    # Underlying objects
    self._underlyingObject = dict()     # Key is chain, value is a renderedDrawable
    self._currentChain = tuple()         # Current chain of objects, each item in tuple is pair: (id, callingFunction)
    self._currentCanvas = None
    self._transformChain = tuple()
    self._transform = dict()           # Key = chain, value = transforms
    
    self._renderOrder = dict()
    
    self._canvases = dict()     # Key = drawble, value = set of canvases
    self._chains = dict()       # Key = (drawable, canvas), value = set of chains
    
    self._openCanvases = set()
    
    # Event handling
    self._handlers = dict()             # Key = drawable or canvas, value = callback object
    
    # Mouse
    self._mousePrevPosition = None
    self._mouseButtonDown = False
    
    self._forceUpdates = True

  def addCommandToQueue(self, command, blocking=False):
    if self._running:
      self._commandQueue.put( (command, blocking) )
      if blocking:
        return self._releaseQueue.get()

  def processCommands(self):
    global _graphicsManager
    try:
      while self._running and self._commandQueue.qsize() > 0:
        (command, blocking) = self._commandQueue.get(0)
        self.processCommand(command, blocking)
    except _Queue.Empty:
      if _debug >= 1:
        print 'Queue empty exception'
      
  def processCommand(self, command, blocking):
    global _graphicsManager, _tkroot
    if _debug >= 2:
      print
      print "Manager executing:", command, blocking
    if _debug >= 3:
      print "Current chain:", self._currentChain
      try:
        print "Update info", self._needsUpdatingInfo
      except:
        pass
      
    # Store a possible return value
    result = None

    # Canvases
    if command[0] == 'create canvas':
      command[1]._canvas = _RenderedCanvas( command[1], command[2], command[3], command[4], command[5], command[6])
      self._transform[((command[1], None), )] = _Transformation()

    elif command[0] == 'update canvas':
      if command[1]._canvas:
        command[1]._canvas.setHeight(command[2])
        command[1]._canvas.setWidth(command[3])
        command[1]._canvas.setBackgroundColor(command[4])
        command[1]._canvas.setTitle(command[5])
      
    elif command[0] == 'close canvas':
      command[1]._canvas._tkWin.withdraw()
      #command[1]._canvas = None
      keys = _graphicsManager._underlyingObject.keys()
      for k in keys:
        if k[0][0] == command[1]:
          _graphicsManager._underlyingObject.pop(k)
      
    elif command[0] == 'open canvas':
      command[1]._canvas._tkWin.deiconify()
      
    elif command[0] == 'begin refresh':
      self._currentChain = ((command[1], None), )
      self._transformationChain = (command[1]._base_Transformation, )
      self._currentCanvas = command[1]
      self._force = command[2]
      self._forceUpdates = False
      self._renderOrder[self._currentCanvas] = list()
      self._chainCount = dict()
      
    elif command[0] == 'complete refresh':
      # Remove any deleted objects
      for item in self._underlyingObject.keys():
        if item[0][0] == self._currentCanvas and item not in self._renderOrder[self._currentCanvas]:
          self.removeUnderlying(item)
      
      self._currentChain = tuple()
      self._tranformationChain = tuple()
      self._currentCanvas = None
      
      self._forceUpdates = True
      _tkroot.update()
      _tkroot.update()
      
    elif command[0] == 'set chain':
      self._currentChain = command[1]
      self._transformationChain = (self._transform[self._currentChain], )
      for x in self._prevRenderOrder:
        print x
      if self._currentChain in self._prevRenderOrder:
        i = self._prevRenderOrder.index(self._currentChain)
        if i > 0:
          self._renderOrder[self._currentCanvas] = self._prevRenderOrder[:i]
          
    elif command[0] == 'save to file':
      command[1]._canvas.saveToFile(command[2])
      
    # Drawables
    elif command[0] == 'begin draw':
      self._chainCount[ self._currentChain + ( (command[1], )) ] = self._chainCount.get(self._currentChain + ( (command[1], )), 0) + 1
      self._currentChain += ( (command[1], self._chainCount[ self._currentChain + ( (command[1], )) ]), )
      if self._canvases.has_key(command[1]):
        self._canvases[command[1]].add(self._currentCanvas)
      else:
        self._canvases[command[1]] = set([self._currentCanvas])
        
      if len(self._currentChain) > 2 and self._currentChain[-1][0] == self._currentChain[-2][0]:
        self._transformationChain += (self._transformationChain[-1], )
      else:
        self._transformationChain += (self._transformationChain[-1] * command[1]._transform, )
        
      self._transform[self._currentChain] = self._transformationChain[-1]
      if self._chains.has_key((command[1], self._currentCanvas)):
        self._chains[(command[1], self._currentCanvas)].add(self._currentChain)
      else:
        self._chains[(command[1], self._currentCanvas)] = set([self._currentChain])
      
      self._renderOrder[self._currentCanvas].append(self._currentChain)
      
    elif command[0] == 'complete draw':
      self._currentChain = self._currentChain[:-1]
      self._transformationChain = self._transformationChain[:-1]
      
    elif command[0] == 'draw circle':
      chain = self._currentChain
      if self._underlyingObject.has_key(chain):
        self._underlyingObject[chain].update(self._transformationChain[-1], self._force)
      else:
          # Create object
          self._underlyingObject[chain] = _RenderedCircle( command[1], self._currentCanvas, self._transformationChain[-1] )
        
    elif command[0] == 'draw rectangle':
      chain = self._currentChain
      if self._underlyingObject.has_key(chain):
        self._underlyingObject[chain].update(self._transformationChain[-1], self._force)
      else:
        # Create object
        self._underlyingObject[chain] = _RenderedRectangle( command[1], self._currentCanvas, self._transformationChain[-1] )
        
        
    elif command[0] == 'draw path':
      chain = self._currentChain
      if self._underlyingObject.has_key(chain):
        self._underlyingObject[chain].update(self._transformationChain[-1], self._force)
      else:
        # Create path in the correct position and add it to the canvas
        self._underlyingObject[self._currentChain] = _RenderedPath( command[1], self._currentCanvas, self._transformationChain[-1], command[1].getPoints() )
        
    elif command[0] == 'draw polygon':
      chain = self._currentChain
      if self._underlyingObject.has_key(chain):
        self._underlyingObject[chain].update(self._transformationChain[-1], self._force)
      else:
        # Create polygon in the correct position and add it to the canvas
        self._underlyingObject[self._currentChain] = _RenderedPolygon( command[1], self._currentCanvas, self._transformationChain[-1], command[1].getPoints() )

    elif command[0] == 'draw text':
      chain = self._currentChain
      if self._underlyingObject.has_key(chain):
        self._underlyingObject[chain].update(self._transformationChain[-1], self._force)
      else:
        self._underlyingObject[self._currentChain] = _RenderedText( command[1], self._currentCanvas, self._transformationChain[-1] )
        
    elif command[0] == 'get text size':
      text = command[1]
      size = command[2]
      tkWin = _Tkinter.Toplevel()
      canvas = _Tkinter.Canvas(tkWin)
      i = canvas.create_text(0, 0, text=text, font=('Helvetica', size, 'normal') )
      bbox = canvas.bbox(i)
      canvas.delete(i)
      tkWin.withdraw()
      result = (bbox[2]-bbox[0],bbox[3]-bbox[1])

    # Release blocking
    if blocking:
      self._releaseQueue.put(result)

  def objectChanged(self, drawable, position, properties, depth):
    if _debug >= 3:
        print "Object changed:", drawable, self._canvases.get(drawable, list()), drawable, position, properties, depth
        
    for can in self._canvases.get(drawable, list()):
      if can._autoRefresh:
        if _debug >= 3:
          print "Chains for update:", self._chains[(drawable,can)]
        if not depth and False:
          can._trueRefresh(False, set(self._chains[(drawable, can)]), position, properties, depth)
        else:
          can._trueRefresh(False, None, True, True, True)

  def removeUnderlying(self, chain):
    pass

  def addHandler(self, shape, callback):
    if self._handlers.has_key(shape):
      if callback not in self._handlers[shape]:
        self._handlers[shape].append(callback)
      else:
        raise ValueError
    else:
      self._handlers[shape] = [callback]

  def removeHandler(self, shape, callback):
    self._handlers[shape].remove(callback)

  def triggerHandler(self, shape, event):
    if self._handlers.has_key(shape) and len(self._handlers[shape]) > 0:
      event._trigger = shape
      for handler in self._handlers[shape]:
        eventThread = _EventThread(handler, event)
        eventThread.start()
      return True
    return False

class Point(object):
  """Stores a two-dimensional point using cartesian coordinates."""
  
  def __init__(self, initialX=0, initialY=0):
    """Create a new point instance.

    initialX   x-coordinate of the point (default 0)
    initialY   y-coordinate of the point (default 0)
    """
    if not isinstance(initialX, (int,float)):
      raise TypeError('numeric value expected for x-coodinate')

    if not isinstance(initialY, (int,float)):
      raise TypeError('numeric value expected for y-coodinate')

    self._x = initialX
    self._y = initialY

  def getX(self):
    """Return the x-coordinate."""
    return self._x

  def setX(self, val):
    """Set the x-coordinate to val."""
    if not isinstance(val, (int,float)):
      raise TypeError('numeric value expected for x-coodinate')
    self._x = val

  def getY(self):
    """Return the y-coordinate."""
    return self._y

  def setY(self, val):
    """Set the y-coordinate to val."""
    if not isinstance(val, (int,float)):
      raise TypeError('numeric value expected for y-coodinate')
    self._y = val

  def get(self):
    """Return an (x,y) tuple."""
    return self._x, self._y

  def scale(self, factor):
    """Scale the coordinates by the given factor."""
    if not isinstance(factor, (int,float)):
      raise TypeError('numeric value expected for factor')
    self._x *= factor
    self._y *= factor
    
  def distance(self, other):
    """Return the distance between this point and the other."""
    if not isinstance(other, Point):
      raise TypeError('other must be a Point instance')
    dx = self._x - other._x
    dy = self._y - other._y
    return _math.sqrt(dx * dx + dy * dy)

  def normalize(self):
    """Mutate the point, scaling it to have distance one from the origin.

    If the point currently represents the origin, it is unchanged.
    """    
    mag = self.distance( Point() )
    if mag > 0:
      self.scale(1/mag)

  def __str__(self):
    """Return a string representation of the point (e.g., '<0,0>')."""
    return '<' + str(self._x) + ',' + str(self._y) + '>'

  def __add__(self, other):
    """Return a new point that is the sum of this Point and the other."""
    if not isinstance(other, Point):
      raise TypeError('both operands must be Point instances')
    return Point(self._x + other._x, self._y + other._y)

  def __mul__(self, operand):
    """Return the result when multiplying the Point by an operand.

    When the operand is a scalar (i.e., an int or float), return a
    Point that has coordinates equal to the original times the factor.

    When operand is another Point, return a scalar that is the dot
    product of the two points.
    """
    if isinstance(operand, (int,float)):         # multiply by constant
      return Point(self._x * operand, self._y * operand)
    elif isinstance(operand, Point):           # dot-product
      return self._x * operand._x + self._y * operand._y
    else:
      raise TypeError('unexpected operand for multiplication')

  def __rmul__(self, operand):
    """Return the result when multiplying the Point by an operand.

    See __mul__ for details.
    """
    return self * operand

  def __xor__(self, angle):
    """Return a new point instance representing the original, rotated about the origin.

    angle  number of degrees of rotation (clockwise)
    """
    if not isinstance(angle, (int,float)):
      raise TypeError('numeric value expected for angle')
    angle = _math.pi*angle/180.
    mag = _math.sqrt(self._x * self._x + self._y * self._y)
    return Point(self._x * _math.cos(angle) - self._y * _math.sin(angle), self._x * _math.sin(angle) + self._y * _math.cos(angle))

class _Transformation(object):
  def __init__(self, value=None):
    if value:
      self._matrix = value[:4]
      self._translation = value[4:]
    else:
      self._matrix = (1.,0.,0.,1.)
      self._translation = (0.,0.)

  def __repr__(self):
    return '\n   _Transformation '+str(hex(id(self)))+':\n   matrix = %s\n   translation = %s\n'%(repr(self._matrix),
                                         repr(self._translation))
    
  def image(self, point):
    return Point( self._matrix[0]*point._x + self._matrix[1]*point._y + self._translation[0],
      self._matrix[2]*point._x + self._matrix[3]*point._y + self._translation[1])

  def inv(self):
    detinv = 1. / self.det()
    m = ( self._matrix[3] * detinv, -self._matrix[1] * detinv, -self._matrix[2] * detinv, self._matrix[0] * detinv )
    t = ( -m[0]*self._translation[0] - m[1]*self._translation[1], -m[2]*self._translation[0] - m[3]*self._translation[1])

    return _Transformation(m+t)

  def __mul__(self, other):
    m = ( self._matrix[0] * other._matrix[0] + self._matrix[1] * other._matrix[2],
      self._matrix[0] * other._matrix[1] + self._matrix[1] * other._matrix[3],
      self._matrix[2] * other._matrix[0] + self._matrix[3] * other._matrix[2],
      self._matrix[2] * other._matrix[1] + self._matrix[3] * other._matrix[3])

    p = self.image( Point(other._translation[0], other._translation[1]) )

    return _Transformation(m + (p.getX(), p.getY()))

  def det(self):
    return (self._matrix[0] * self._matrix[3] - self._matrix[1] * self._matrix[2])

class Color(object):
  """A color representation.

  A color can be specified by name or RGB value, and can be made transparent.
  
  Available colors are:
  
  aliceblue, antiquewhite, antiquewhite1, antiquewhite2, antiquewhite3,
  antiquewhite4, aquamarine, aquamarine1, aquamarine2, aquamarine3, aquamarine4,
  azure, azure1, azure2, azure3, azure4, beige, bisque, bisque1, bisque2, bisque3,
  bisque4, black, blanchedalmond, blue, blue1, blue2, blue3, blue4, blueviolet,
  brown, brown1, brown2, brown3, brown4, burlywood, burlywood1, burlywood2,
  burlywood3, burlywood4, cadetblue, cadetblue1, cadetblue2, cadetblue3,
  cadetblue4, chartreuse, chartreuse1, chartreuse2, chartreuse3, chartreuse4,
  chocolate, chocolate1, chocolate2, chocolate3, chocolate4, coral, coral1,
  coral2, coral3, coral4, cornflowerblue, cornsilk, cornsilk1, cornsilk2,
  cornsilk3, cornsilk4, cyan, cyan1, cyan2, cyan3, cyan4, darkblue, darkcyan,
  darkgoldenrod, darkgoldenrod1, darkgoldenrod2, darkgoldenrod3, darkgoldenrod4,
  darkgray, darkgreen, darkgrey, darkkhaki, darkmagenta, darkolivegreen,
  darkolivegreen1, darkolivegreen2, darkolivegreen3, darkolivegreen4, darkorange,
  darkorange1, darkorange2, darkorange3, darkorange4, darkorchid, darkorchid1,
  darkorchid2, darkorchid3, darkorchid4, darkred, darksalmon, darkseagreen,
  darkseagreen1, darkseagreen2, darkseagreen3, darkseagreen4, darkslateblue,
  darkslategray, darkslategray1, darkslategray2, darkslategray3, darkslategray4,
  darkslategrey, darkturquoise, darkviolet, deeppink, deeppink1, deeppink2,
  deeppink3, deeppink4, deepskyblue, deepskyblue1, deepskyblue2, deepskyblue3,
  deepskyblue4, dimgray, dimgrey, dodgerblue, dodgerblue1, dodgerblue2,
  dodgerblue3, dodgerblue4, firebrick, firebrick1, firebrick2, firebrick3,
  firebrick4, floralwhite, forestgreen, gainsboro, ghostwhite, gold, gold1, gold2,
  gold3, gold4, goldenrod, goldenrod1, goldenrod2, goldenrod3, goldenrod4, gray,
  gray0, gray1, gray10, gray100, gray11, gray12, gray13, gray14, gray15, gray16,
  gray17, gray18, gray19, gray2, gray20, gray21, gray22, gray23, gray24, gray25,
  gray26, gray27, gray28, gray29, gray3, gray30, gray31, gray32, gray33, gray34,
  gray35, gray36, gray37, gray38, gray39, gray4, gray40, gray41, gray42, gray43,
  gray44, gray45, gray46, gray47, gray48, gray49, gray5, gray50, gray51, gray52,
  gray53, gray54, gray55, gray56, gray57, gray58, gray59, gray6, gray60, gray61,
  gray62, gray63, gray64, gray65, gray66, gray67, gray68, gray69, gray7, gray70,
  gray71, gray72, gray73, gray74, gray75, gray76, gray77, gray78, gray79, gray8,
  gray80, gray81, gray82, gray83, gray84, gray85, gray86, gray87, gray88, gray89,
  gray9, gray90, gray91, gray92, gray93, gray94, gray95, gray96, gray97, gray98,
  gray99, green, green1, green2, green3, green4, greenyellow, grey, grey0, grey1,
  grey10, grey100, grey11, grey12, grey13, grey14, grey15, grey16, grey17, grey18,
  grey19, grey2, grey20, grey21, grey22, grey23, grey24, grey25, grey26, grey27,
  grey28, grey29, grey3, grey30, grey31, grey32, grey33, grey34, grey35, grey36,
  grey37, grey38, grey39, grey4, grey40, grey41, grey42, grey43, grey44, grey45,
  grey46, grey47, grey48, grey49, grey5, grey50, grey51, grey52, grey53, grey54,
  grey55, grey56, grey57, grey58, grey59, grey6, grey60, grey61, grey62, grey63,
  grey64, grey65, grey66, grey67, grey68, grey69, grey7, grey70, grey71, grey72,
  grey73, grey74, grey75, grey76, grey77, grey78, grey79, grey8, grey80, grey81,
  grey82, grey83, grey84, grey85, grey86, grey87, grey88, grey89, grey9, grey90,
  grey91, grey92, grey93, grey94, grey95, grey96, grey97, grey98, grey99,
  honeydew, honeydew1, honeydew2, honeydew3, honeydew4, hotpink, hotpink1,
  hotpink2, hotpink3, hotpink4, indianred, indianred1, indianred2, indianred3,
  indianred4, ivory, ivory1, ivory2, ivory3, ivory4, khaki, khaki1, khaki2,
  khaki3, khaki4, lavender, lavenderblush, lavenderblush1, lavenderblush2,
  lavenderblush3, lavenderblush4, lawngreen, lemonchiffon, lemonchiffon1,
  lemonchiffon2, lemonchiffon3, lemonchiffon4, lightblue, lightblue1, lightblue2,
  lightblue3, lightblue4, lightcoral, lightcyan, lightcyan1, lightcyan2,
  lightcyan3, lightcyan4, lightgoldenrod, lightgoldenrod1, lightgoldenrod2,
  lightgoldenrod3, lightgoldenrod4, lightgoldenrodyellow, lightgray, lightgreen,
  lightgrey, lightpink, lightpink1, lightpink2, lightpink3, lightpink4,
  lightsalmon, lightsalmon1, lightsalmon2, lightsalmon3, lightsalmon4,
  lightseagreen, lightskyblue, lightskyblue1, lightskyblue2, lightskyblue3,
  lightskyblue4, lightslateblue, lightslategray, lightslategrey, lightsteelblue,
  lightsteelblue1, lightsteelblue2, lightsteelblue3, lightsteelblue4, lightyellow,
  lightyellow1, lightyellow2, lightyellow3, lightyellow4, limegreen, linen,
  magenta, magenta1, magenta2, magenta3, magenta4, maroon, maroon1, maroon2,
  maroon3, maroon4, mediumaquamarine, mediumblue, mediumorchid, mediumorchid1,
  mediumorchid2, mediumorchid3, mediumorchid4, mediumpurple, mediumpurple1,
  mediumpurple2, mediumpurple3, mediumpurple4, mediumseagreen, mediumslateblue,
  mediumspringgreen, mediumturquoise, mediumvioletred, midnightblue, mintcream,
  mistyrose, mistyrose1, mistyrose2, mistyrose3, mistyrose4, moccasin,
  navajowhite, navajowhite1, navajowhite2, navajowhite3, navajowhite4, navy,
  navyblue, oldlace, olivedrab, olivedrab1, olivedrab2, olivedrab3, olivedrab4,
  orange, orange1, orange2, orange3, orange4, orangered, orangered1, orangered2,
  orangered3, orangered4, orchid, orchid1, orchid2, orchid3, orchid4,
  palegoldenrod, palegreen, palegreen1, palegreen2, palegreen3, palegreen4,
  paleturquoise, paleturquoise1, paleturquoise2, paleturquoise3, paleturquoise4,
  palevioletred, palevioletred1, palevioletred2, palevioletred3, palevioletred4,
  papayawhip, peachpuff, peachpuff1, peachpuff2, peachpuff3, peachpuff4, peru,
  pink, pink1, pink2, pink3, pink4, plum, plum1, plum2, plum3, plum4, powderblue,
  purple, purple1, purple2, purple3, purple4, red, red1, red2, red3, red4,
  rosybrown, rosybrown1, rosybrown2, rosybrown3, rosybrown4, royalblue,
  royalblue1, royalblue2, royalblue3, royalblue4, saddlebrown, salmon, salmon1,
  salmon2, salmon3, salmon4, sandybrown, seagreen, seagreen1, seagreen2,
  seagreen3, seagreen4, seashell, seashell1, seashell2, seashell3, seashell4,
  sienna, sienna1, sienna2, sienna3, sienna4, skyblue, skyblue1, skyblue2,
  skyblue3, skyblue4, slateblue, slateblue1, slateblue2, slateblue3, slateblue4,
  slategray, slategray1, slategray2, slategray3, slategray4, slategrey, snow,
  snow1, snow2, snow3, snow4, springgreen, springgreen1, springgreen2,
  springgreen3, springgreen4, steelblue, steelblue1, steelblue2, steelblue3,
  steelblue4, tan, tan1, tan2, tan3, tan4, thistle, thistle1, thistle2, thistle3,
  thistle4, tomato, tomato1, tomato2, tomato3, tomato4, turquoise, turquoise1,
  turquoise2, turquoise3, turquoise4, violet, violetred, violetred1, violetred2,
  violetred3, violetred4, wheat, wheat1, wheat2, wheat3, wheat4, white,
  whitesmoke, yellow, yellow1, yellow2, yellow3, yellow4, yellowgreen
  """
  _colorValues = {
    'aliceblue'            : (240,248,255), 'antiquewhite'         : (250,235,215), 'antiquewhite1'        : (255,239,219),
    'antiquewhite2'        : (238,223,204), 'antiquewhite3'        : (205,192,176), 'antiquewhite4'        : (139,131,120),
    'aquamarine'           : (127,255,212), 'aquamarine1'          : (127,255,212), 'aquamarine2'          : (118,238,198),
    'aquamarine3'          : (102,205,170), 'aquamarine4'          : ( 69,139,116), 'azure'                : (240,255,255),
    'azure1'               : (240,255,255), 'azure2'               : (224,238,238), 'azure3'               : (193,205,205),
    'azure4'               : (131,139,139), 'beige'                : (245,245,220), 'bisque'               : (255,228,196),
    'bisque1'              : (255,228,196), 'bisque2'              : (238,213,183), 'bisque3'              : (205,183,158),
    'bisque4'              : (139,125,107), 'black'                : (  0,  0,  0), 'blanchedalmond'       : (255,235,205),
    'blue'                 : (  0,  0,255), 'blue1'                : (  0,  0,255), 'blue2'                : (  0,  0,238),
    'blue3'                : (  0,  0,205), 'blue4'                : (  0,  0,139), 'blueviolet'           : (138, 43,226),
    'brown'                : (165, 42, 42), 'brown1'               : (255, 64, 64), 'brown2'               : (238, 59, 59),
    'brown3'               : (205, 51, 51), 'brown4'               : (139, 35, 35), 'burlywood'            : (222,184,135),
    'burlywood1'           : (255,211,155), 'burlywood2'           : (238,197,145), 'burlywood3'           : (205,170,125),
    'burlywood4'           : (139,115, 85), 'cadetblue'            : ( 95,158,160), 'cadetblue1'           : (152,245,255),
    'cadetblue2'           : (142,229,238), 'cadetblue3'           : (122,197,205), 'cadetblue4'           : ( 83,134,139),
    'chartreuse'           : (127,255,  0), 'chartreuse1'          : (127,255,  0), 'chartreuse2'          : (118,238,  0),
    'chartreuse3'          : (102,205,  0), 'chartreuse4'          : ( 69,139,  0), 'chocolate'            : (210,105, 30),
    'chocolate1'           : (255,127, 36), 'chocolate2'           : (238,118, 33), 'chocolate3'           : (205,102, 29),
    'chocolate4'           : (139, 69, 19), 'coral'                : (255,127, 80), 'coral1'               : (255,114, 86),
    'coral2'               : (238,106, 80), 'coral3'               : (205, 91, 69), 'coral4'               : (139, 62, 47),
    'cornflowerblue'       : (100,149,237), 'cornsilk'             : (255,248,220), 'cornsilk1'            : (255,248,220),
    'cornsilk2'            : (238,232,205), 'cornsilk3'            : (205,200,177), 'cornsilk4'            : (139,136,120),
    'cyan'                 : (  0,255,255), 'cyan1'                : (  0,255,255), 'cyan2'                : (  0,238,238),
    'cyan3'                : (  0,205,205), 'cyan4'                : (  0,139,139), 'darkblue'             : (  0,  0,139),
    'darkcyan'             : (  0,139,139), 'darkgoldenrod'        : (184,134, 11), 'darkgoldenrod1'       : (255,185, 15),
    'darkgoldenrod2'       : (238,173, 14), 'darkgoldenrod3'       : (205,149, 12), 'darkgoldenrod4'       : (139,101,  8),
    'darkgray'             : (169,169,169), 'darkgreen'            : (  0,100,  0), 'darkgrey'             : (169,169,169),
    'darkkhaki'            : (189,183,107), 'darkmagenta'          : (139,  0,139), 'darkolivegreen'       : ( 85,107, 47),
    'darkolivegreen1'      : (202,255,112), 'darkolivegreen2'      : (188,238,104), 'darkolivegreen3'      : (162,205, 90),
    'darkolivegreen4'      : (110,139, 61), 'darkorange'           : (255,140,  0), 'darkorange1'          : (255,127,  0),
    'darkorange2'          : (238,118,  0), 'darkorange3'          : (205,102,  0), 'darkorange4'          : (139, 69,  0),
    'darkorchid'           : (153, 50,204), 'darkorchid1'          : (191, 62,255), 'darkorchid2'          : (178, 58,238),
    'darkorchid3'          : (154, 50,205), 'darkorchid4'          : (104, 34,139), 'darkred'              : (139,  0,  0),
    'darksalmon'           : (233,150,122), 'darkseagreen'         : (143,188,143), 'darkseagreen1'        : (193,255,193),
    'darkseagreen2'        : (180,238,180), 'darkseagreen3'        : (155,205,155), 'darkseagreen4'        : (105,139,105),
    'darkslateblue'        : ( 72, 61,139), 'darkslategray'        : ( 47, 79, 79), 'darkslategray1'       : (151,255,255),
    'darkslategray2'       : (141,238,238), 'darkslategray3'       : (121,205,205), 'darkslategray4'       : ( 82,139,139),
    'darkslategrey'        : ( 47, 79, 79), 'darkturquoise'        : (  0,206,209), 'darkviolet'           : (148,  0,211),
    'deeppink'             : (255, 20,147), 'deeppink1'            : (255, 20,147), 'deeppink2'            : (238, 18,137),
    'deeppink3'            : (205, 16,118), 'deeppink4'            : (139, 10, 80), 'deepskyblue'          : (  0,191,255),
    'deepskyblue1'         : (  0,191,255), 'deepskyblue2'         : (  0,178,238), 'deepskyblue3'         : (  0,154,205),
    'deepskyblue4'         : (  0,104,139), 'dimgray'              : (105,105,105), 'dimgrey'              : (105,105,105),
    'dodgerblue'           : ( 30,144,255), 'dodgerblue1'          : ( 30,144,255), 'dodgerblue2'          : ( 28,134,238),
    'dodgerblue3'          : ( 24,116,205), 'dodgerblue4'          : ( 16, 78,139), 'firebrick'            : (178, 34, 34),
    'firebrick1'           : (255, 48, 48), 'firebrick2'           : (238, 44, 44), 'firebrick3'           : (205, 38, 38),
    'firebrick4'           : (139, 26, 26), 'floralwhite'          : (255,250,240), 'forestgreen'          : ( 34,139, 34),
    'gainsboro'            : (220,220,220), 'ghostwhite'           : (248,248,255), 'gold'                 : (255,215,  0),
    'gold1'                : (255,215,  0), 'gold2'                : (238,201,  0), 'gold3'                : (205,173,  0),
    'gold4'                : (139,117,  0), 'goldenrod'            : (218,165, 32), 'goldenrod1'           : (255,193, 37),
    'goldenrod2'           : (238,180, 34), 'goldenrod3'           : (205,155, 29), 'goldenrod4'           : (139,105, 20),
    'gray'                 : (190,190,190), 'gray0'                : (  0,  0,  0), 'gray1'                : (  3,  3,  3),
    'gray10'               : ( 26, 26, 26), 'gray100'              : (255,255,255), 'gray11'               : ( 28, 28, 28),
    'gray12'               : ( 31, 31, 31), 'gray13'               : ( 33, 33, 33), 'gray14'               : ( 36, 36, 36),
    'gray15'               : ( 38, 38, 38), 'gray16'               : ( 41, 41, 41), 'gray17'               : ( 43, 43, 43),
    'gray18'               : ( 46, 46, 46), 'gray19'               : ( 48, 48, 48), 'gray2'                : (  5,  5,  5),
    'gray20'               : ( 51, 51, 51), 'gray21'               : ( 54, 54, 54), 'gray22'               : ( 56, 56, 56),
    'gray23'               : ( 59, 59, 59), 'gray24'               : ( 61, 61, 61), 'gray25'               : ( 64, 64, 64),
    'gray26'               : ( 66, 66, 66), 'gray27'               : ( 69, 69, 69), 'gray28'               : ( 71, 71, 71),
    'gray29'               : ( 74, 74, 74), 'gray3'                : (  8,  8,  8), 'gray30'               : ( 77, 77, 77),
    'gray31'               : ( 79, 79, 79), 'gray32'               : ( 82, 82, 82), 'gray33'               : ( 84, 84, 84),
    'gray34'               : ( 87, 87, 87), 'gray35'               : ( 89, 89, 89), 'gray36'               : ( 92, 92, 92),
    'gray37'               : ( 94, 94, 94), 'gray38'               : ( 97, 97, 97), 'gray39'               : ( 99, 99, 99),
    'gray4'                : ( 10, 10, 10), 'gray40'               : (102,102,102), 'gray41'               : (105,105,105),
    'gray42'               : (107,107,107), 'gray43'               : (110,110,110), 'gray44'               : (112,112,112),
    'gray45'               : (115,115,115), 'gray46'               : (117,117,117), 'gray47'               : (120,120,120),
    'gray48'               : (122,122,122), 'gray49'               : (125,125,125), 'gray5'                : ( 13, 13, 13),
    'gray50'               : (127,127,127), 'gray51'               : (130,130,130), 'gray52'               : (133,133,133),
    'gray53'               : (135,135,135), 'gray54'               : (138,138,138), 'gray55'               : (140,140,140),
    'gray56'               : (143,143,143), 'gray57'               : (145,145,145), 'gray58'               : (148,148,148),
    'gray59'               : (150,150,150), 'gray6'                : ( 15, 15, 15), 'gray60'               : (153,153,153),
    'gray61'               : (156,156,156), 'gray62'               : (158,158,158), 'gray63'               : (161,161,161),
    'gray64'               : (163,163,163), 'gray65'               : (166,166,166), 'gray66'               : (168,168,168),
    'gray67'               : (171,171,171), 'gray68'               : (173,173,173), 'gray69'               : (176,176,176),
    'gray7'                : ( 18, 18, 18), 'gray70'               : (179,179,179), 'gray71'               : (181,181,181),
    'gray72'               : (184,184,184), 'gray73'               : (186,186,186), 'gray74'               : (189,189,189),
    'gray75'               : (191,191,191), 'gray76'               : (194,194,194), 'gray77'               : (196,196,196),
    'gray78'               : (199,199,199), 'gray79'               : (201,201,201), 'gray8'                : ( 20, 20, 20),
    'gray80'               : (204,204,204), 'gray81'               : (207,207,207), 'gray82'               : (209,209,209),
    'gray83'               : (212,212,212), 'gray84'               : (214,214,214), 'gray85'               : (217,217,217),
    'gray86'               : (219,219,219), 'gray87'               : (222,222,222), 'gray88'               : (224,224,224),
    'gray89'               : (227,227,227), 'gray9'                : ( 23, 23, 23), 'gray90'               : (229,229,229),
    'gray91'               : (232,232,232), 'gray92'               : (235,235,235), 'gray93'               : (237,237,237),
    'gray94'               : (240,240,240), 'gray95'               : (242,242,242), 'gray96'               : (245,245,245),
    'gray97'               : (247,247,247), 'gray98'               : (250,250,250), 'gray99'               : (252,252,252),
    'green'                : (  0,255,  0), 'green1'               : (  0,255,  0), 'green2'               : (  0,238,  0),
    'green3'               : (  0,205,  0), 'green4'               : (  0,139,  0), 'greenyellow'          : (173,255, 47),
    'grey'                 : (190,190,190), 'grey0'                : (  0,  0,  0), 'grey1'                : (  3,  3,  3),
    'grey10'               : ( 26, 26, 26), 'grey100'              : (255,255,255), 'grey11'               : ( 28, 28, 28),
    'grey12'               : ( 31, 31, 31), 'grey13'               : ( 33, 33, 33), 'grey14'               : ( 36, 36, 36),
    'grey15'               : ( 38, 38, 38), 'grey16'               : ( 41, 41, 41), 'grey17'               : ( 43, 43, 43),
    'grey18'               : ( 46, 46, 46), 'grey19'               : ( 48, 48, 48), 'grey2'                : (  5,  5,  5),
    'grey20'               : ( 51, 51, 51), 'grey21'               : ( 54, 54, 54), 'grey22'               : ( 56, 56, 56),
    'grey23'               : ( 59, 59, 59), 'grey24'               : ( 61, 61, 61), 'grey25'               : ( 64, 64, 64),
    'grey26'               : ( 66, 66, 66), 'grey27'               : ( 69, 69, 69), 'grey28'               : ( 71, 71, 71),
    'grey29'               : ( 74, 74, 74), 'grey3'                : (  8,  8,  8), 'grey30'               : ( 77, 77, 77),
    'grey31'               : ( 79, 79, 79), 'grey32'               : ( 82, 82, 82), 'grey33'               : ( 84, 84, 84),
    'grey34'               : ( 87, 87, 87), 'grey35'               : ( 89, 89, 89), 'grey36'               : ( 92, 92, 92),
    'grey37'               : ( 94, 94, 94), 'grey38'               : ( 97, 97, 97), 'grey39'               : ( 99, 99, 99),
    'grey4'                : ( 10, 10, 10), 'grey40'               : (102,102,102), 'grey41'               : (105,105,105),
    'grey42'               : (107,107,107), 'grey43'               : (110,110,110), 'grey44'               : (112,112,112),
    'grey45'               : (115,115,115), 'grey46'               : (117,117,117), 'grey47'               : (120,120,120),
    'grey48'               : (122,122,122), 'grey49'               : (125,125,125), 'grey5'                : ( 13, 13, 13),
    'grey50'               : (127,127,127), 'grey51'               : (130,130,130), 'grey52'               : (133,133,133),
    'grey53'               : (135,135,135), 'grey54'               : (138,138,138), 'grey55'               : (140,140,140),
    'grey56'               : (143,143,143), 'grey57'               : (145,145,145), 'grey58'               : (148,148,148),
    'grey59'               : (150,150,150), 'grey6'                : ( 15, 15, 15), 'grey60'               : (153,153,153),
    'grey61'               : (156,156,156), 'grey62'               : (158,158,158), 'grey63'               : (161,161,161),
    'grey64'               : (163,163,163), 'grey65'               : (166,166,166), 'grey66'               : (168,168,168),
    'grey67'               : (171,171,171), 'grey68'               : (173,173,173), 'grey69'               : (176,176,176),
    'grey7'                : ( 18, 18, 18), 'grey70'               : (179,179,179), 'grey71'               : (181,181,181),
    'grey72'               : (184,184,184), 'grey73'               : (186,186,186), 'grey74'               : (189,189,189),
    'grey75'               : (191,191,191), 'grey76'               : (194,194,194), 'grey77'               : (196,196,196),
    'grey78'               : (199,199,199), 'grey79'               : (201,201,201), 'grey8'                : ( 20, 20, 20),
    'grey80'               : (204,204,204), 'grey81'               : (207,207,207), 'grey82'               : (209,209,209),
    'grey83'               : (212,212,212), 'grey84'               : (214,214,214), 'grey85'               : (217,217,217),
    'grey86'               : (219,219,219), 'grey87'               : (222,222,222), 'grey88'               : (224,224,224),
    'grey89'               : (227,227,227), 'grey9'                : ( 23, 23, 23), 'grey90'               : (229,229,229),
    'grey91'               : (232,232,232), 'grey92'               : (235,235,235), 'grey93'               : (237,237,237),
    'grey94'               : (240,240,240), 'grey95'               : (242,242,242), 'grey96'               : (245,245,245),
    'grey97'               : (247,247,247), 'grey98'               : (250,250,250), 'grey99'               : (252,252,252),
    'honeydew'             : (240,255,240), 'honeydew1'            : (240,255,240), 'honeydew2'            : (224,238,224),
    'honeydew3'            : (193,205,193), 'honeydew4'            : (131,139,131), 'hotpink'              : (255,105,180),
    'hotpink1'             : (255,110,180), 'hotpink2'             : (238,106,167), 'hotpink3'             : (205, 96,144),
    'hotpink4'             : (139, 58, 98), 'indianred'            : (205, 92, 92), 'indianred1'           : (255,106,106),
    'indianred2'           : (238, 99, 99), 'indianred3'           : (205, 85, 85), 'indianred4'           : (139, 58, 58),
    'ivory'                : (255,255,240), 'ivory1'               : (255,255,240), 'ivory2'               : (238,238,224),
    'ivory3'               : (205,205,193), 'ivory4'               : (139,139,131), 'khaki'                : (240,230,140),
    'khaki1'               : (255,246,143), 'khaki2'               : (238,230,133), 'khaki3'               : (205,198,115),
    'khaki4'               : (139,134, 78), 'lavender'             : (230,230,250), 'lavenderblush'        : (255,240,245),
    'lavenderblush1'       : (255,240,245), 'lavenderblush2'       : (238,224,229), 'lavenderblush3'       : (205,193,197),
    'lavenderblush4'       : (139,131,134), 'lawngreen'            : (124,252,  0), 'lemonchiffon'         : (255,250,205),
    'lemonchiffon1'        : (255,250,205), 'lemonchiffon2'        : (238,233,191), 'lemonchiffon3'        : (205,201,165),
    'lemonchiffon4'        : (139,137,112), 'lightblue'            : (173,216,230), 'lightblue1'           : (191,239,255),
    'lightblue2'           : (178,223,238), 'lightblue3'           : (154,192,205), 'lightblue4'           : (104,131,139),
    'lightcoral'           : (240,128,128), 'lightcyan'            : (224,255,255), 'lightcyan1'           : (224,255,255),
    'lightcyan2'           : (209,238,238), 'lightcyan3'           : (180,205,205), 'lightcyan4'           : (122,139,139),
    'lightgoldenrod'       : (238,221,130), 'lightgoldenrod1'      : (255,236,139), 'lightgoldenrod2'      : (238,220,130),
    'lightgoldenrod3'      : (205,190,112), 'lightgoldenrod4'      : (139,129, 76), 'lightgoldenrodyellow' : (250,250,210),
    'lightgray'            : (211,211,211), 'lightgreen'           : (144,238,144), 'lightgrey'            : (211,211,211),
    'lightpink'            : (255,182,193), 'lightpink1'           : (255,174,185), 'lightpink2'           : (238,162,173),
    'lightpink3'           : (205,140,149), 'lightpink4'           : (139, 95,101), 'lightsalmon'          : (255,160,122),
    'lightsalmon1'         : (255,160,122), 'lightsalmon2'         : (238,149,114), 'lightsalmon3'         : (205,129, 98),
    'lightsalmon4'         : (139, 87, 66), 'lightseagreen'        : ( 32,178,170), 'lightskyblue'         : (135,206,250),
    'lightskyblue1'        : (176,226,255), 'lightskyblue2'        : (164,211,238), 'lightskyblue3'        : (141,182,205),
    'lightskyblue4'        : ( 96,123,139), 'lightslateblue'       : (132,112,255), 'lightslategray'       : (119,136,153),
    'lightslategrey'       : (119,136,153), 'lightsteelblue'       : (176,196,222), 'lightsteelblue1'      : (202,225,255),
    'lightsteelblue2'      : (188,210,238), 'lightsteelblue3'      : (162,181,205), 'lightsteelblue4'      : (110,123,139),
    'lightyellow'          : (255,255,224), 'lightyellow1'         : (255,255,224), 'lightyellow2'         : (238,238,209),
    'lightyellow3'         : (205,205,180), 'lightyellow4'         : (139,139,122), 'limegreen'            : ( 50,205, 50),
    'linen'                : (250,240,230), 'magenta'              : (255,  0,255), 'magenta1'             : (255,  0,255),
    'magenta2'             : (238,  0,238), 'magenta3'             : (205,  0,205), 'magenta4'             : (139,  0,139),
    'maroon'               : (176, 48, 96), 'maroon1'              : (255, 52,179), 'maroon2'              : (238, 48,167),
    'maroon3'              : (205, 41,144), 'maroon4'              : (139, 28, 98), 'mediumaquamarine'     : (102,205,170),
    'mediumblue'           : (  0,  0,205), 'mediumorchid'         : (186, 85,211), 'mediumorchid1'        : (224,102,255),
    'mediumorchid2'        : (209, 95,238), 'mediumorchid3'        : (180, 82,205), 'mediumorchid4'        : (122, 55,139),
    'mediumpurple'         : (147,112,219), 'mediumpurple1'        : (171,130,255), 'mediumpurple2'        : (159,121,238),
    'mediumpurple3'        : (137,104,205), 'mediumpurple4'        : ( 93, 71,139), 'mediumseagreen'       : ( 60,179,113),
    'mediumslateblue'      : (123,104,238), 'mediumspringgreen'    : (  0,250,154), 'mediumturquoise'      : ( 72,209,204),
    'mediumvioletred'      : (199, 21,133), 'midnightblue'         : ( 25, 25,112), 'mintcream'            : (245,255,250),
    'mistyrose'            : (255,228,225), 'mistyrose1'           : (255,228,225), 'mistyrose2'           : (238,213,210),
    'mistyrose3'           : (205,183,181), 'mistyrose4'           : (139,125,123), 'moccasin'             : (255,228,181),
    'navajowhite'          : (255,222,173), 'navajowhite1'         : (255,222,173), 'navajowhite2'         : (238,207,161),
    'navajowhite3'         : (205,179,139), 'navajowhite4'         : (139,121, 94), 'navy'                 : (  0,  0,128),
    'navyblue'             : (  0,  0,128), 'oldlace'              : (253,245,230), 'olivedrab'            : (107,142, 35),
    'olivedrab1'           : (192,255, 62), 'olivedrab2'           : (179,238, 58), 'olivedrab3'           : (154,205, 50),
    'olivedrab4'           : (105,139, 34), 'orange'               : (255,165,  0), 'orange1'              : (255,165,  0),
    'orange2'              : (238,154,  0), 'orange3'              : (205,133,  0), 'orange4'              : (139, 90,  0),
    'orangered'            : (255, 69,  0), 'orangered1'           : (255, 69,  0), 'orangered2'           : (238, 64,  0),
    'orangered3'           : (205, 55,  0), 'orangered4'           : (139, 37,  0), 'orchid'               : (218,112,214),
    'orchid1'              : (255,131,250), 'orchid2'              : (238,122,233), 'orchid3'              : (205,105,201),
    'orchid4'              : (139, 71,137), 'palegoldenrod'        : (238,232,170), 'palegreen'            : (152,251,152),
    'palegreen1'           : (154,255,154), 'palegreen2'           : (144,238,144), 'palegreen3'           : (124,205,124),
    'palegreen4'           : ( 84,139, 84), 'paleturquoise'        : (175,238,238), 'paleturquoise1'       : (187,255,255),
    'paleturquoise2'       : (174,238,238), 'paleturquoise3'       : (150,205,205), 'paleturquoise4'       : (102,139,139),
    'palevioletred'        : (219,112,147), 'palevioletred1'       : (255,130,171), 'palevioletred2'       : (238,121,159),
    'palevioletred3'       : (205,104,137), 'palevioletred4'       : (139, 71, 93), 'papayawhip'           : (255,239,213),
    'peachpuff'            : (255,218,185), 'peachpuff1'           : (255,218,185), 'peachpuff2'           : (238,203,173),
    'peachpuff3'           : (205,175,149), 'peachpuff4'           : (139,119,101), 'peru'                 : (205,133, 63),
    'pink'                 : (255,192,203), 'pink1'                : (255,181,197), 'pink2'                : (238,169,184),
    'pink3'                : (205,145,158), 'pink4'                : (139, 99,108), 'plum'                 : (221,160,221),
    'plum1'                : (255,187,255), 'plum2'                : (238,174,238), 'plum3'                : (205,150,205),
    'plum4'                : (139,102,139), 'powderblue'           : (176,224,230), 'purple'               : (160, 32,240),
    'purple1'              : (155, 48,255), 'purple2'              : (145, 44,238), 'purple3'              : (125, 38,205),
    'purple4'              : ( 85, 26,139), 'red'                  : (255,  0,  0), 'red1'                 : (255,  0,  0),
    'red2'                 : (238,  0,  0), 'red3'                 : (205,  0,  0), 'red4'                 : (139,  0,  0),
    'rosybrown'            : (188,143,143), 'rosybrown1'           : (255,193,193), 'rosybrown2'           : (238,180,180),
    'rosybrown3'           : (205,155,155), 'rosybrown4'           : (139,105,105), 'royalblue'            : ( 65,105,225),
    'royalblue1'           : ( 72,118,255), 'royalblue2'           : ( 67,110,238), 'royalblue3'           : ( 58, 95,205),
    'royalblue4'           : ( 39, 64,139), 'saddlebrown'          : (139, 69, 19), 'salmon'               : (250,128,114),
    'salmon1'              : (255,140,105), 'salmon2'              : (238,130, 98), 'salmon3'              : (205,112, 84),
    'salmon4'              : (139, 76, 57), 'sandybrown'           : (244,164, 96), 'seagreen'             : ( 46,139, 87),
    'seagreen1'            : ( 84,255,159), 'seagreen2'            : ( 78,238,148), 'seagreen3'            : ( 67,205,128),
    'seagreen4'            : ( 46,139, 87), 'seashell'             : (255,245,238), 'seashell1'            : (255,245,238),
    'seashell2'            : (238,229,222), 'seashell3'            : (205,197,191), 'seashell4'            : (139,134,130),
    'sienna'               : (160, 82, 45), 'sienna1'              : (255,130, 71), 'sienna2'              : (238,121, 66),
    'sienna3'              : (205,104, 57), 'sienna4'              : (139, 71, 38), 'skyblue'              : (135,206,235),
    'skyblue1'             : (135,206,255), 'skyblue2'             : (126,192,238), 'skyblue3'             : (108,166,205),
    'skyblue4'             : ( 74,112,139), 'slateblue'            : (106, 90,205), 'slateblue1'           : (131,111,255),
    'slateblue2'           : (122,103,238), 'slateblue3'           : (105, 89,205), 'slateblue4'           : ( 71, 60,139),
    'slategray'            : (112,128,144), 'slategray1'           : (198,226,255), 'slategray2'           : (185,211,238),
    'slategray3'           : (159,182,205), 'slategray4'           : (108,123,139), 'slategrey'            : (112,128,144),
    'snow'                 : (255,250,250), 'snow1'                : (255,250,250), 'snow2'                : (238,233,233),
    'snow3'                : (205,201,201), 'snow4'                : (139,137,137), 'springgreen'          : (  0,255,127),
    'springgreen1'         : (  0,255,127), 'springgreen2'         : (  0,238,118), 'springgreen3'         : (  0,205,102),
    'springgreen4'         : (  0,139, 69), 'steelblue'            : ( 70,130,180), 'steelblue1'           : ( 99,184,255),
    'steelblue2'           : ( 92,172,238), 'steelblue3'           : ( 79,148,205), 'steelblue4'           : ( 54,100,139),
    'tan'                  : (210,180,140), 'tan1'                 : (255,165, 79), 'tan2'                 : (238,154, 73),
    'tan3'                 : (205,133, 63), 'tan4'                 : (139, 90, 43), 'thistle'              : (216,191,216),
    'thistle1'             : (255,225,255), 'thistle2'             : (238,210,238), 'thistle3'             : (205,181,205),
    'thistle4'             : (139,123,139), 'tomato'               : (255, 99, 71), 'tomato1'              : (255, 99, 71),
    'tomato2'              : (238, 92, 66), 'tomato3'              : (205, 79, 57), 'tomato4'              : (139, 54, 38),
    'turquoise'            : ( 64,224,208), 'turquoise1'           : (  0,245,255), 'turquoise2'           : (  0,229,238),
    'turquoise3'           : (  0,197,205), 'turquoise4'           : (  0,134,139), 'violet'               : (238,130,238),
    'violetred'            : (208, 32,144), 'violetred1'           : (255, 62,150), 'violetred2'           : (238, 58,140),
    'violetred3'           : (205, 50,120), 'violetred4'           : (139, 34, 82), 'wheat'                : (245,222,179),
    'wheat1'               : (255,231,186), 'wheat2'               : (238,216,174), 'wheat3'               : (205,186,150),
    'wheat4'               : (139,126,102), 'white'                : (255,255,255), 'whitesmoke'           : (245,245,245),
    'yellow'               : (255,255,  0), 'yellow1'              : (255,255,  0), 'yellow2'              : (238,238,  0),
    'yellow3'              : (205,205,  0), 'yellow4'              : (139,139,  0), 'yellowgreen'          : (154,205, 50),
  }

  def __init__(self, colorChoice='White'):
    """Create a new Color instance (default 'White').

    The parameter can be either:
       - a string with the name of the color
       - an (r,g,b) tuple
       - an existing Color instance (which will be cloned)
    """
    # we intentionally have Drawable objects using a color
    # register with the color instance, so that when the color is
    # mutated, the object can be informed that it has changed
    self._drawables = []
    
    if isinstance(colorChoice,str):
      try:
        self.setByName(colorChoice)
      except ValueError, ve:
        raise ValueError(str(ve))
    elif isinstance(colorChoice,tuple):
      try:
        self.setByValue(colorChoice)
      except ValueError, ve:
        raise ValueError(str(ve))
    elif isinstance(colorChoice,Color):
      self._colorName = colorChoice._colorName
      self._transparent = colorChoice._transparent
      self._colorValue = colorChoice._colorValue
    else:
      raise TypeError('Invalid color specification')

  def setByName(self, colorName):
    """Set the color to colorName.

    colorName   a string representing a valid name
    
    If colorName is 'Transparent' the resulting color will not
    show up on a canvas.
    """
    if not isinstance(colorName,str):
      raise TypeError('string expected as color name')

    self._colorName = colorName.lower().replace(' ','')
    if self._colorName == 'transparent':
      self._transparent = True
      self._colorValue = (0,0,0)
    else:
      try:
        self._transparent = False
        self._colorValue = Color._colorValues[self._colorName.lower()]
      except KeyError:
        raise ValueError('%s is not a valid color name' % colorName)
    self._informDrawables()

  def getColorName(self):
    """Return the name of the color.

    If the color was set by RGB value, it returns 'Custom'.
    """
    return self._colorName

  def setByValue(self, rgbTuple):
    """Set the color to the given tuple of (red, green, blue) values."""
    if not isinstance(rgbTuple,tuple):
      raise TypeError('(r,g,b) tuple expected')
    if len(rgbTuple)!=3:
      raise ValueError('(r,g,b) tuple must have three components')
    for val in rgbTuple:
      if not isinstance(val,(int,float)):
        raise TypeError('tuple entries must be numeric')
      elif not 0 <= val <= 255:
        raise ValueError('tuple entries must be from 0 to 255')
    self._transparent = False
    self._colorName = 'Custom'
    self._colorValue = rgbTuple
    self._informDrawables()

  def getColorValue(self):
    """Return a tuple of the (red, green, blue) color components."""
    return (self._colorValue[0], self._colorValue[1], self._colorValue[2])

  def isTransparent(self):
    """Return a boolean variable indicating if the current color is transparent."""
    return self._transparent
  
  def randomColor():
    """Return a random color."""
    return Color((_random.randint(0,255),_random.randint(0,255),_random.randint(0,255)))
  randomColor = staticmethod(randomColor)

  def __repr__(self):
    """Return the name of the color, if named.  Otherwise return the (r,g,b) value."""
    if self._colorName == 'Custom':
      return self._colorValue.__repr__()
    else:
      return self._colorName

  def _register(self, drawable):
    """Called to register a Drawable with this Color instance"""
    if drawable not in self._drawables:
      self._drawables.append(drawable)
  
  def _unregister(self, drawable):
    """Called to unregister a Drawable with this Color instance"""
    if drawable in self._drawables:
      self._drawables.remove(drawable)
  
  def _informDrawables(self):
    """When the Color instance has been mutated, we must inform those registered drawables."""
    for drawable in self._drawables:
      drawable._objectChanged()

class _GraphicsContainer(object):
  def __init__(self):
    self._contents = []

  def __contains__(self, obj):
    """Return True if obj is currently in the container; False otherwise."""
    return obj in self._contents

  def add(self, drawable):
    """Add the Drawable object to the container."""
    # not doing error checking here, as we want tailored messages for Canvas and Layer
    self._contents.append(drawable)

  def remove(self, drawable):
    """Remove the Drawable object from the container."""
    # not doing error checking here, as we want tailored messages for Canvas and Layer
    self._contents.remove(drawable)

  def clear(self):
    """Remove all objects from the container."""
    contents = list(self._contents)  # intentional clone
    for drawable in contents:
      self.remove(drawable)

  def getContents(self):
    """Return the contents of the container, sorted by depth."""
    contentsPair = list()
    for drawable in self._contents:
      contentsPair.append( (drawable._depth, drawable) )
    contentsPair.sort()
    contentsPair.reverse()

    if _debug >= 3:
      print "Contents of container (depth, item):", contentsPair

    contents = list()
    for pair in contentsPair:
      contents.append(pair[1])

    return contents

class Event(object):
  """An event typically triggered by the user interface."""
  def __init__(self):
    self._eventType = ""
    self._x, self._y = 0, 0
    self._prevx, self._prevy = 0,0
    self._key = ""
    self._trigger = None
    
  def getDescription(self):
    """Return a text description of the event.

    Possibilities include:
      'mouse click', 'mouse release', 'mouse drag', 'keyboard, 'timer'
    """
    return self._eventType
    
  def getMouseLocation(self):
    """Return a Point designating the location of the mouse at the time of the event."""
    return Point(self._x, self._y)
  
  def getOldMouseLocation(self):
    """Return a Point designating the location of the mouse at the start of a mouse drag."""
    return Point(self._prevx, self._prevy)
  
  def getTrigger(self):
    """Return a reference to the object that triggered the event."""
    return self._trigger
  
  def getKey(self):
    """Return a string designating the key pressed for a keyboard event."""
    return self._key

class EventHandler(object):
  """A base class for creating new event handlers.

  The handle method for this base class does not do anything.
  """
  def __init__(self):
    """Create a new event handler.
    
    Children of this class must call this constructor.
    """
    pass

  def handle(self, event):
    """Handle an event.
    
    Child classes must override this method, but do not need
    to call it.
    """
    pass

class _ReleaseHandler(EventHandler):
  def __init__(self, lock):
    self._lock = lock
    self._event = None
    self._lock.acquire()

  def handle(self, event):
    if event.getDescription() in ['keyboard', 'mouse click']:
      self._event = event
      self._lock.release()

class _EventTrigger(object):

  def __init__(self):
    pass

  def wait(self):
    """Wait for an event to occur.

    When an event occurs, an Event instance is returned
    with information about what has happened.
    """
    lock = _threading.Lock()
    rh = _ReleaseHandler(lock)
    self.addHandler(rh)
    lock.acquire()
    self.removeHandler(rh)
    return rh._event

  def addHandler(self, handler):
    """Register an EventHandler instance with this object."""
    if not isinstance(handler, EventHandler):
      raise TypeError('Only instance of EventHandler (or child class) can handle events')
    try:
      _graphicsManager.addHandler(self, handler)
    except ValueError:
      raise ValueError('Handler is already handling events for this object')

  def removeHandler(self, handler):
    """Unregister an EventHandler instance from this object."""
    if not isinstance(handler, EventHandler):
      raise TypeError('Parameter is not an instance of EventHandler (or child class)')
    try:
      _graphicsManager.removeHandler(self, handler)
    except ValueError:
      raise ValueError('The handler is not currently associated with this object.')
      
    
class _EventThread(_threading.Thread):
  def __init__(self, handler, event):
    _threading.Thread.__init__(self)
    self._handler = handler
    self._event = event
  
  def run(self):
    self._handler.handle(self._event)

class Canvas(_GraphicsContainer, _EventTrigger):
  """A window that can be drawn upon."""

  def __init__(self, w=200, h=200, bgColor=None, title="Graphics canvas", autoRefresh=True):
    """Create a new drawing canvas.

    A new canvas will be created.
      w             width of drawing area (default 200)
      h             height of drawing area (default 200)
      bgColor       color of the background (default 'White')
      title         window title (default 'Graphics Canvas')
      autoRefresh   whether auto-refresh mode is used (default True)
    """
    global _graphicsManager
    _GraphicsContainer.__init__(self)
    _EventTrigger.__init__(self)
      
    self._base_Transformation = _Transformation()
    self._canvasUpdated = True
    
    if not bgColor:
      bgColor = 'white'

    if not isinstance(w, (int,float)):
      raise TypeError('width must be numeric')
    if not isinstance(h, (int,float)):
      raise TypeError('height must be numeric')
    if not isinstance(title,str):
      raise TypeError('title must be a string')
    if not isinstance(autoRefresh,bool):
      raise TypeError('autoRefresh flag must be a boolean value')
    
    if isinstance(bgColor,Color):
      self._backgroundColor = bgColor
    else:
      try:
        self._backgroundColor = Color(bgColor)
      except TypeError,te:
        raise TypeError(str(te))
      except ValueError,ve:
        raise ValueError(str(ve))

    self._width = w
    self._height = h
    self._title = title
    self._autoRefresh = autoRefresh
    self._canvasOpen = True
    _graphicsManager._openCanvases.add(self)
    
    _graphicsManager.addCommandToQueue(('create canvas', self, w, h, self._backgroundColor, title, autoRefresh))
      
  def setBackgroundColor(self, color):
    """Set the background color.

    The parameter can be either:
       - a string with the name of the color
       - an (r,g,b) tuple
       - an existing Color instance
    """
    if isinstance(color,Color):
      self._backgroundColor = color
    else:
      try:
        self._backgroundColor = Color(color)
      except TypeError,te:
        raise TypeError(str(te))
      except ValueError,ve:
        raise ValueError(str(ve))
    self._canvasChanged()

  def getBackgroundColor(self):
    """Return the background color as a Color instance."""
    return self._backgroundColor
    
  def setWidth(self, w):
    """Reset the canvas width to w."""
    if not isinstance(w, (int,float)):
      raise TypeError('width must be numeric value')
    if w <= 0:
      raise ValueError('width must be positive')
    self._width = w
    self._canvasChanged()

  def getWidth(self):
    """Return the width of the canvas."""
    return self._width

  def setHeight(self, h):
    """Reset the canvas height to h."""
    if not isinstance(h, (int,float)):
      raise TypeError('height must be numeric value')
    if h <= 0:
      raise ValueError('height must be positive')
    self._height = h
    self._canvasChanged()

  def getHeight(self):
    """Return the height of the canvas."""
    return self._height

  def setTitle(self, title):
    """Set the title for the canvas window to given string."""
    if not isinstance(title,str):
      raise TypeError('title must be a string')
    self._title = title
    self._canvasChanged()

  def getTitle(self):
    """Return the title of the window."""
    return self._title

  def close(self):
    """Close the canvas window (if not already closed).

    The window can be reopened with a subsequent call to open().
    """
    if self._canvasOpen:
      _graphicsManager.addCommandToQueue(("close canvas", self))
      _graphicsManager._openCanvases.remove(self)
      self._canvasOpen = False
      
  def open(self):
    """Opens a graphic window (if not already open).

    The window can be closed with a subsequent call to close().
    """
    if not self._canvasOpen:
      self._canvasOpen = True
      _graphicsManager._openCanvases.add(self)
        
      if not self._canvas:
        _graphicsManager.addCommandToQueue(('create canvas', self, self._width, self._height, self._backgroundColor, self._title, self._autoRefresh))
      else:
        _graphicsManager.addCommandToQueue(("open canvas", self))
      
      if self._autoRefresh:
        self.refresh(True)

  def add(self, drawable):
    """Add the Drawable object to the canvas."""
    if not isinstance(drawable,Drawable):
      raise TypeError('Only Drawable objects can be added to a Canvas')
    if drawable in self._contents:
      raise ValueError('Object already on the Canvas')
    _GraphicsContainer.add(self, drawable)
    if '_transform' not in vars(drawable):
      raise StandardError('Drawable instance not properly initialized (was parent constructor called?)')
    try:
      drawable._draw
    except:
      raise StandardError('Child class of Drawable must provide a _draw method')
    
    if _graphicsManager._canvases.has_key(drawable):
      _graphicsManager._canvases[drawable].add(self)
    else:
      _graphicsManager._canvases[drawable] = set([self])
    
    self._canvasChanged()

  def remove(self, drawable):
    """Remove the drawable object from the canvas."""
    if drawable not in self._contents:
      raise ValueError('Object not currently on the Canvas')
    _GraphicsContainer.remove(self, drawable)
    self._canvasChanged()

  def setAutoRefresh(self, autoRefresh=True):
    """Change the auto-refresh mode.

    When True (the default), every change to the canvas or to an
       object drawn upon the canvas will be immediately rendered to
       the screen.

    When False, all changes are recorded internally, yet not shown
       on the screen until the next subsequent call to the refresh()
       method of this canvas.  This allows multiple changes to be
       buffered and rendered all at once.
    """
    if not isinstance(autoRefresh,bool):
      raise TypeError('autoRefresh flag should be a bool')
    if autoRefresh and not self._autoRefresh:
      self.refresh()  # flush the current queue
    self._autoRefresh = autoRefresh

  def refresh(self, force=False):
    """
    Forces all internal changes to be rendered to the screen.

    This method is only necessary when the auto-refresh property
    of the canvas has previously been turned off.  If force is
    True then the entire window is redrawn regardless of need.
    """
    self._trueRefresh(force, None, True, True, True)
    
  def _trueRefresh(self, force, needsUpdating, position, properties, depth):
    _graphicsManager._refreshLock.acquire()

    try:
      _graphicsManager.addCommandToQueue(("begin refresh", self, force))
      _graphicsManager._needsUpdatingInfo = (position, properties, depth)
      if not needsUpdating:
        _graphicsManager.addCommandToQueue(("update canvas", self, self._height, self._width, self._backgroundColor, self._title))
        for drawable in self.getContents():
          drawable._draw()
      else:
        for chain in needsUpdating:
          _graphicsManager.addCommandToQueue(("set chain", chain))
          chain[-1][0]._draw()
      _graphicsManager.addCommandToQueue(("complete refresh", self), True)
    except:
      if _debug >= 1:
        print "Exception thrown in refresh"

    _graphicsManager._refreshLock.release()

  def saveToFile(self, filename):
    """Save a picture of the current canvas to a file."""
    if not isinstance(filename, str):
      raise TypeError('filename must be a string')
    background = Rectangle(self.getWidth()+2, self.getHeight()+2)
    background.move( float(self.getWidth())/2, float(self.getHeight())/2 )
    background.setFillColor(self.getBackgroundColor())
    background.setBorderColor(self.getBackgroundColor())

    maxDepth = 0
    for o in self._contents:
      if o.getDepth() > maxDepth:
        maxDepth = o.getDepth()

    background.setDepth(maxDepth+1)
    self.add(background)
    self.refresh(True)    
    
    _graphicsManager.addCommandToQueue(('save to file', self, filename))
    
    self.remove(background)
    self.refresh()
    
  def _canvasChanged(self):
    self._canvasUpdated = True
    if self._autoRefresh:
      self.refresh()
    
class Drawable(_EventTrigger):
  """An object that can be drawn to a graphics canvas."""
  
  def __init__(self, reference=None):
    """Create a Drawable instance.

    referencePoint  local reference point for scaling, rotating and flipping
                      (default Point(0,0) )
    """
    _EventTrigger.__init__(self)

    if reference:
      if not isinstance(reference,Point):
        raise TypeError('reference point must be a Point instance')
      self._reference = reference
    else:
      self._reference = Point()
    self._transform = _Transformation()
    self._depth = [50, _ourRandom.random()]
    
    # Give an autoupdate feature to user-defined methods
    if not vars(self.__class__).has_key('_noAutomaticCall'):
      keys = vars(self.__class__).keys()
      for n in keys:
        v = vars(self.__class__)[n]
        try:
          v.__call__
          if n not in ['__new__', '__init__', '_draw']:
            self._replaceMethod(n, v)
        except:
          pass
          
  def _replaceMethod(self, name, cs1graphicsWrapper):
    def wrap(self, *args, **kw):
      result = cs1graphicsWrapper(self, *args, **kw)
      self._objectChanged()
      return result
    setattr(self.__class__, name, wrap)

  def move(self, dx, dy):
    """Move the object dx units along X-axis and dy units along Y-axis.

    For the default coordinate system, positive dx is rightward and
    negative is leftward; positive dy is downard and negative is upward.
    """
    if not isinstance(dx, (int,float)):
      raise TypeError('dx must be numeric')
    if not isinstance(dy, (int,float)):
      raise TypeError('dy must be numeric')
    self._transform = _Transformation( (1.,0.,0.,1.,dx,dy)) * self._transform
    self._objectChanged(True,False,False)

  def moveTo(self, x, y):
    """Move the object to align its reference point with (x,y)"""
    if not isinstance(x, (int,float)):
      raise TypeError('x must be numeric')
    if not isinstance(y, (int,float)):
      raise TypeError('y must be numeric')
    curRef = self.getReferencePoint()
    self.move(x-curRef.getX(), y-curRef.getY())
    self._objectChanged(True,False,False)

  def rotate(self, angle):
    """Rotate the object around its current reference point.

    angle  number of degrees of clockwise rotation
    """
    if not isinstance(angle, (int,float)):
      raise TypeError('angle must be specified numerically')
    angle = -_math.pi*angle/180.
    p = self._localToGlobal(self._reference)
    trans = _Transformation((1.,0.,0.,1.)+p.get())
    rot = _Transformation((_math.cos(angle),_math.sin(angle),
                -_math.sin(angle),_math.cos(angle),0.,0.))
    
    self._transform = trans*(rot*(trans.inv()*self._transform))
    self._objectChanged(True,False,False)

  def scale(self, factor):
    """Scale the object relative to its current reference point.

    factor      scale is multiplied by this number (must be positive)
    """
    if not isinstance(factor, (int,float)):
      raise TypeError, 'scaling factor must be a positive number'
    if factor<=0:
      raise ValueError, 'scaling factor must be a positive number'
    
    p = self._localToGlobal(self._reference)
    trans = _Transformation((1.,0.,0.,1.)+p.get())
    sca = _Transformation((factor,0.,0.,factor,0.,0.))

    self._transform = trans*(sca*(trans.inv()*self._transform))
    self._objectChanged(True,False,False)

  def stretch(self, xFactor, yFactor, angle=0):
    """Stretch the shape in mutltiple direction.
    
    By default the x-axis is scaled by a factor of xFactor and the
    y-axis is scaled by a factor of yFactor.  The optional
    parameter rotates the directions that the streching is performed
    along.
    """
    if not isinstance(xFactor, (int,float)) or not isinstance(yFactor, (int,float)):
      raise TypeError, 'stretch factor must be a positive number'
    if xFactor<=0 or yFactor<=0:
      raise ValueError, 'stretch factor must be a positive number'
    
    p = self._localToGlobal(self._reference)
    trans = _Transformation((1.,0.,0.,1.)+p.get())
    rot = _Transformation((_math.cos(angle),_math.sin(angle),
                -_math.sin(angle),_math.cos(angle),0.,0.))
    rotinv = rot.inv()
    sca = _Transformation((xFactor,0.,0.,yFactor,0.,0.))
    
    self._transform = trans*(rotinv*(sca*(rot*(trans.inv()*self._transform))))
    self._objectChanged(True,False,False)
    
  def flip(self, angle=0):    
    """Flip the object reflected about its current reference point.

    By default the flip is a left-to-right flip with a vertical axis of symmetry.

    angle     a clockwise rotation of the axis of symmetry away from vertical
    """    
    if not isinstance(angle, (int,float)):
      raise TypeError('angle must be numeric')
    
    angle = _math.pi*angle/180.
    p = self._localToGlobal(self._reference)
    trans = _Transformation((1.,0.,0.,1.)+p.get())
    rot = _Transformation((_math.cos(angle),_math.sin(angle),
                -_math.sin(angle),_math.cos(angle),0.,0.))
    rotinv = rot.inv()
    invert = _Transformation((-1.,0.,0.,1.,0.,0.))
    
    self._transform = trans*(rotinv*(invert*(rot*(trans.inv()*self._transform))))
    self._objectChanged(True,False,False)
    
  def shear(self, shear, angle=0):
    """Shear the object relative to its current reference point.
    
    By default, points with the same y-coordinate as the reference point are left
    unchanged.  A point d units above the reference point is shifted d * shear
    units to the right.  The optional angle parameter rotates the axis
    that the shearing occurs along.

    angle      clockwise angle for shear
    """    
    if not isinstance(shear, (int,float)):
      raise TypeError('shear factor must be numeric')
    if not isinstance(angle, (int,float)):
      raise TypeError('angle must be numeric')
    
    angle = _math.pi*angle/180.
    p = self._localToGlobal(self._reference)
    trans = _Transformation((1.,0.,0.,1.)+p.get())
    rot = _Transformation((_math.cos(angle),_math.sin(angle),
                -_math.sin(angle),_math.cos(angle),0.,0.))
    rotinv = rot.inv()
    sh = _Transformation((1.,-shear,0.,1.,0.,0.))
    
    self._transform = trans*(rotinv*(sh*(rot*(trans.inv()*self._transform))))
    self._objectChanged(True,False,False)

  def getReferencePoint(self):
    """Return a copy of the current reference point.

    Note that mutating that copy has no effect on the Drawable object.
    """
    return self._localToGlobal(self._reference)

  def adjustReference(self, dx, dy):
    """Move the local reference point relative to its current position.

    Note that the object is not moved at all.
    """
    if not isinstance(dx, (int,float)):
      raise TypeError('dx must be numeric')
    if not isinstance(dy, (int,float)):
      raise TypeError('dy must be numeric')
    p = self._localToGlobal(self._reference)
    p = Point(p.getX()+dx, p.getY()+dy)
    self._reference = self._globalToLocal(p)

  def setDepth(self, depth):
    """Set the depth of the object.

    Objects with a higher depth will be rendered behind those with lower depths.
    """
    if not isinstance(depth, (int,float)):
      raise TypeError('depth must be numeric')
    self._depth[-2] = depth
    self._objectChanged(False,False,True)

  def getDepth(self):
    """Return the depth of the object."""
    return self._depth[-2]

  def clone(self):
    """Return a duplicate of the drawable object.

    Note that the duplicate is not automatically added to any
    canvases or layers, even if original is currently so.
    """
    return _copy.deepcopy(self)

  def _localToGlobal(self, point):
    if not isinstance(point,Point):
      raise TypeError('parameter must be a Point instance')
    return self._transform.image(point)

  def _globalToLocal(self, point):
    if not isinstance(point,Point):
      raise TypeError('parameter must be a Point instance')
    return self._transform.inv().image(point)

  def _beginDraw(self):
    _graphicsManager.addCommandToQueue(("begin draw", self))

  def _completeDraw(self):
    _graphicsManager.addCommandToQueue(("complete draw", self))

  def _draw(self):
    """Cause the object to be drawn (typically, the method is not called directly)."""
    if _debug>=2:
      print "within Drawable._draw for self=",self
    raise NotImplementedError('_draw() method must be implemented for each shape.')

  def _objectChanged(self, position=True, properties=True, depth=True):
    """Designate that some trait of this object has been mutated.

    As a result, all of its rendered images may need to be updated.
    """
    if _graphicsManager:
      _graphicsManager.objectChanged(self, position, properties, depth)

class Layer(Drawable, _GraphicsContainer):
  """A composite that represents a group of shapes as a single drawable object.

  Objects are placed onto the layer relative to the coordinate
  system of the layer itself.  The layer can then be placed onto a
  canvas (or even onto another layer).
  """
  def __init__(self):
    """Construct a new Layer instance.

    The layer is initially empty.
    
    The reference point of that layer is initially the origin in
    its own coordinate system, (0,0).
    """
    Drawable.__init__(self)
    _GraphicsContainer.__init__(self)
      
  def _noAutomaticCall(self):
    pass

  def add(self, drawable):
    """Add the Drawable object to the layer."""
    if _debug>=2: print 'Call to Layer.add with self=',self,' drawable=',drawable
    if not isinstance(drawable,Drawable):
      raise TypeError('parameter must be an instance of a Drawable object')
    if drawable in self._contents:
      raise ValueError('The object is already on the Layer')
    if '_transform' not in vars(drawable):
      raise StandardError('Drawable not properly initialized (was parent constructor called?)')
    try:
      drawable._draw
    except:
      raise StandardError('Drawable class must have a _draw method')
    
    _GraphicsContainer.add(self, drawable)
    self._objectChanged()
    
  def remove(self, drawable):
    """Remove the Drawable object from the layer.

    A ValueError is raised if the drawable is not currently in the layer.
    """
    if drawable not in self._contents:
      raise ValueError('object not currently on the Layer')
    
    _GraphicsContainer.remove(self,drawable)
    self._objectChanged()

  def _draw(self):
    self._beginDraw()
    for shape in self.getContents():
      shape._draw()
    self._completeDraw()

class Shape(Drawable):
  """A drawable objects that has a border."""
  
  def __init__(self, reference=None):
    """Construct a Shape instance.

    reference  the initial placement of the shape's reference point.
               (default Point(0,0) )
    """
    if reference and not isinstance(reference,Point):
      raise TypeError('reference point must be a Point instance')
    Drawable.__init__(self, reference)
    self._borderColor = Color("Black")
    self._borderWidth = 1

  def setBorderColor(self, color):
    """
    Set the border color to a copy of the indicated color.

    The parameter can be either:
       - a string with the name of the color
       - an (r,g,b) tuple
       - an existing Color instance
    """
    old = self._borderColor
    if isinstance(color,Color):
      self._borderColor = color
    else:
      try:
        self._borderColor = Color(color)
      except TypeError,te:
        raise TypeError(str(te))
      except ValueError,ve:
        raise ValueError(str(ve))
    self._objectChanged(False,True,False)

    if self._borderColor is not old:
      self._borderColor._register(self)
      if not isinstance(self,FillableShape) or old is not self._fillColor:
        # this shape no longer using the old color
        old._unregister(self)

  def getBorderColor(self):
    """Return the color of the object's border."""
    return self._borderColor

  def setBorderWidth(self, width):
    """
    Set the width of the border to the indicated width.
    """
    if not isinstance(width, (int,float)):
      raise TypeError('Border width must be non-negative number')
    if width < 0:
      raise ValueError("A shape's border width cannot be negative.")
    self._borderWidth = width
    self._objectChanged(False,True,False)

  def getBorderWidth(self):
    """Return the width of the border."""
    return self._borderWidth
    
class FillableShape(Shape):
  """A shape that can be filled with an interior color."""
  
  def __init__(self, reference=None):
    """Construct a new FillableShape instance.

    The interior color defaults to 'Transparent'.

    reference  the initial placement of the shape's reference point.
               (default Point(0,0) )
    """
    if reference and not isinstance(reference,Point):
      raise TypeError('reference point must be a Point instance')
    Shape.__init__(self, reference)
    self._fillColor = Color("Transparent")

  def setFillColor(self, color):
    """Set the interior color of the shape to the color.

    The parameter can be either:
       - a string with the name of the color
       - an (r,g,b) tuple
       - an existing Color instance
    """
    old = self._fillColor
    if isinstance(color,Color):
      self._fillColor = color
    else:
      try:
        self._fillColor = Color(color)
      except TypeError,te:
        raise TypeError(str(te))
      except ValueError,ve:
        raise ValueError(str(ve))
    self._objectChanged(False,True,False)

    if self._fillColor is not old:
      self._fillColor._register(self)
      if self._borderColor is not old:
        # no longer using the old color
        old._unregister(self)


  def getFillColor(self):
    """Return the color of the shape's interior."""
    return self._fillColor

class Circle(FillableShape):
  """A circle that can be drawn to a canvas."""
  def __init__(self, radius=10, centerPt=None):
    """Construct a new instance of Circle.

    radius    the circle's radius (default 10)
    centerPt  a Point representing the placement of the circle's center
                (default Point(0,0) )

    The reference point for a circle is originally its center.
    """
    if not isinstance(radius, (int,float)):
      raise TypeError('Radius must be a number')
    if radius <= 0:
      raise ValueError("The circle's radius must be positive.")
    if centerPt and not isinstance(centerPt,Point):
      raise TypeError("The circle's center must be specified as a Point")

    FillableShape.__init__(self) # intentionally not sending center
    if not centerPt:
      centerPt = Point()
    self._transform = _Transformation( (radius,0.,0.,radius,centerPt.getX(),centerPt.getY()) )
      
  def _noAutomaticCall(self):
    pass

  def setRadius(self, r):
    """Set the radius of the circle to r."""
    if not isinstance(r, (int,float)):
      raise TypeError('Radius must be a number')
    if r <= 0:
      raise ValueError("The circle's radius must be positive.")

    factor = float(r)/self.getRadius()
    self._transform = self._transform * _Transformation((factor,0.,0.,factor,0.,0.))
    
    self._objectChanged(True,False,False)
    
  def getRadius(self):
    """Return the radius of the circle."""
    return _math.sqrt(self._transform._matrix[0]**2 + self._transform._matrix[1]**2)

  def _draw(self):
    self._beginDraw()

    _graphicsManager.addCommandToQueue(('draw circle', self))
      
    self._completeDraw()
     
class Rectangle(FillableShape):
  """A rectangle that can be drawn to the canvas."""
  def __init__(self, w=20, h=10, centerPt=None):
    """
    Construct a new instance of a Rectangle.

    The reference point for a rectangle is its center.

    w         the width of the rectangle (default 20)
    h         the height of the rectangle (default 10)
    centerPt  a Point representing the placement of the rectangle's center
                (default Point(0,0) )
    """
    if not isinstance(w, (int,float)):
      raise TypeError('Width must be a number')
    if w <= 0:
      raise ValueError('The width must be positive.')
    if not isinstance(h, (int,float)):
      raise TypeError('Height must be a number')
    if h <= 0:
      raise ValueError('The height must be positive.')
    if centerPt and not isinstance(centerPt,Point):
      raise TypeError('center must be specified as a Point')

    FillableShape.__init__(self)  # intentionally not sending center point

    if not centerPt:
      centerPt = Point(0,0)

    self._transform = _Transformation( (w, 0., 0., h, centerPt.getX(), centerPt.getY()) )
      
  def _noAutomaticCall(self):
    pass

  def getWidth(self):
    """Return the width of the rectangle."""
    return _math.sqrt(self._transform._matrix[0]**2 + self._transform._matrix[2]**2)
  
  def getHeight(self):
    """Return the height of the rectangle."""
    return _math.sqrt(self._transform._matrix[1]**2 + self._transform._matrix[3]**2)

  def setWidth(self, w):
    """Set the width of the rectangle to w."""
    if not isinstance(w, (int,float)):
      raise TypeError('Width must be a positive number')
    if w <= 0:
      raise ValueError("The rectangle's width must be positive")
    factor = float(w) / self.getWidth()
    p = self._localToGlobal(self._reference)
    trans = _Transformation((1.,0.,0.,1.)+p.get())
    sca = _Transformation((factor,0.,0.,1.,0.,0.))
    
    self._transform = trans*(sca*(trans.inv()*self._transform))
    self._objectChanged(True,False,False)
    
  def setHeight(self, h):
    """Set the height of the rectangle to h."""
    if not isinstance(h, (int,float)):
      raise TypeError('Height must be a positive number')
    if h <= 0:
      raise ValueError("The rectangle's height must be positive")
    factor = float(h) / self.getHeight()
    p = self._localToGlobal(self._reference)
    trans = _Transformation((1.,0.,0.,1.)+p.get())
    sca = _Transformation((1.,0.,0.,factor,0.,0.))
    
    self._transform = trans*(sca*(trans.inv()*self._transform))
    self._objectChanged(True,False,False)

  def _draw(self):
    self._beginDraw()

    _graphicsManager.addCommandToQueue(('draw rectangle', self))
      
    self._completeDraw()

class Square(Rectangle):
  """A square that can be drawn to the canvas."""
  def __init__(self, size=10, centerPt=None):
    """
    Construct a new Square instance.

    The reference point for a square is its center.

    size      the dimension of the square (default 10)
    centerPt  a Point representing the placement of the rectangle's center
                (defaults Point(0,0) )
    """
    if not isinstance(size, (int,float)):
      raise TypeError('size must be a number')
    if size <= 0:
      raise ValueError("The size must be positive.")
    if centerPt and not isinstance(centerPt,Point):
      raise TypeError('center must be specified as a Point')

    Rectangle.__init__(self, size, size, centerPt)
      
  def _noAutomaticCall(self):
    pass


  def getSize(self):
    """Return the length of a side of the square."""
    return self.getWidth()

  def setSize(self, s):
    """Set the width and height of the square to s."""
    if not isinstance(s, (int,float)):
      raise TypeError('size must be a number')
    if s <= 0:
      raise ValueError('The size must be positive.')
    
    Rectangle.setWidth(self, s)
    Rectangle.setHeight(self, s)

  def setWidth(self, w):
    """Set the width and height of the square to w."""
    if not isinstance(w, (int,float)):
      raise TypeError('width must be a positive number')
    if w <= 0:
      raise ValueError("The square's width must be positive")
    self.setSize(w)

  def setHeight(self, h):
    """Set the width and height of the square to h."""
    if not isinstance(h, (int,float)):
      raise TypeError('height must be a positive number')
    if h <= 0:
      raise ValueError("The square's height must be positive")
    self.setSize(h)

class Path(Shape):
  """
  A path that can be drawn to a canvas.
  """
  def __init__(self, *points):
    """
    Construct a new instance of a Path.

    The path is described as a series of points that are connected in order.

    These points can be initialized by sending each individual Point
    as a separate parameter, or by sending a single parameter
    containing a sequence of Points. If no parameters are sent, the
    path initially has zero points.

    The reference point for a path is initially aligned with the first
    point of the path.
    """
    Shape.__init__(self)
    
    if len(points)==1:
      try:
        points = tuple(points[0])
      except:
        pass   # original parameter might be a single Point
    for p in points:
      if not isinstance(p,Point):
        raise TypeError('non-Point specified as parameter')
    self._points = list(points)
    if len(self._points)>=1:
      self.adjustReference(self._points[0].getX(),
      self._points[0].getY())
      
  def _noAutomaticCall(self):
    pass

  def addPoint(self, point, index=-1):
    """Add a new point to the Path.

    point  a Point instance
    index  designates where on the path the new point is placed
           (at the end, by default)
    """
    if not isinstance(point,Point):
      raise TypeError('parameter must be a Point instance')
    if index>-1:
      self._points.insert(point, index)
    else:
      self._points.append(point)
    if len(self._points)==1:  # first point added
      self._reference = Point(point.getX(), point.getY())
    self._objectChanged(True,False,False)

  def deletePoint(self, index=-1):
    """Remove the Point at the given index.

    By default, deletes the last point."""
    if not isinstance(index,int):
      raise TypeError('index must be an integer')
    try:
      self._points.pop(index)
    except:
      raise IndexError('index out of range')
    self._objectChanged(True,False,False)

  def clearPoints(self):
    """Remove all points, setting this back to an empty Path."""
    self._points = list()
    self._objectChanged(True,False,False)

  def getNumberOfPoints(self):
    """Return the current number of points."""
    return len(self._points)

  def getPoint(self, index):
    """Return a copy of the Point at the given index.

    Subsequently mutating that copy has no effect on the Path.
    """
    if not isinstance(index,int):
      raise TypeError('index must be an integer')
    try:
      p = self._points[index]
    except:
      raise IndexError('index out of range')
    return Point(p.getX(), p.getY())

  def setPoint(self, point, index=-1):
    """Change the Point at the given index to a new value.

    By default, the last point is changed.
    """
    if not isinstance(index,int):
      raise TypeError('index must be an integer')
    if not isinstance(point,Point):
      raise TypeError('first parameter must be a Point instance')
    try:
      self._points[index] = point
    except:
      raise IndexError('index out of range')
    self._objectChanged(True,False,False)

  def getPoints(self):
    """Return a list of Point instances that are copies of the points on the Path."""
    return list(self._points)
    
  def _draw(self):
    self._beginDraw()

    _graphicsManager.addCommandToQueue(("draw path", self))

    self._completeDraw()


class Polygon(Path,FillableShape):
  """A polygon that can be drawn to a canvas."""
  def __init__(self, *points):
    """Construct a new Polygon instance.

    The polygon is described as a series of points that are connected in order.
    The last point is automatically connected back to the first to close the polygon.

    These points can be initialized by sending each individual Point
    as a separate parameter, or by sending a single parameter
    containing a sequence of Points. If no parameters are sent, the
    polygon initially has zero points.

    The reference point for a polygon is initially aligned with the
    first point of the polygon.
    """
    FillableShape.__init__(self)
    try:
      Path.__init__(self, points)
    except TypeError,te:
      raise TypeError(str(te))
      
  def _noAutomaticCall(self):
    pass

  def _draw(self):
    self._beginDraw()

    _graphicsManager.addCommandToQueue(("draw polygon", self))

    self._completeDraw()

#class Image(Drawable):
  #def __init__(self, filename):
    #Drawable.__init__(self)
    #if not isinstance(filename,str):
      #raise TypeError('filename must be a string')
    #self._filename = filename   # of course, we won't know if this is legitimate until it is added to a canvas
         
  #def rotate(self,angle):
    #"""Not yet implemented."""
    #raise NotImplementedError('rotating image is not yet implemented')
    
  #def scale(self,factor):
    #"""Not yet implemented."""
    #raise NotImplementedError('scaling image is not yet implemented')

  #def _draw(self):
    #self._beginDraw()

    #_graphicsManager.addCommandToQueue(("draw image", self))
    
    #self._completeDraw()

class Text(Drawable):
  """A piece of text that can be drawn to a canvas."""
  def __init__(self, message='', fontsize=12, centerPt=None):
    """
    Construct a new Text instance.

    The text color is initially black, although this can be changed by
    setColor.  The reference point for the text is initially its center.

    message   a string which is to be displayed (default empty string)
    fontsize  the font size (default 12)
    centerPt  where to locate the center of the text (default Point(0,0) )
    """
    if not isinstance(message,str):
      raise TypeError('message must be a string')
    if not isinstance(fontsize,int):
      raise TypeError('fontsize must be an integer')
    if fontsize <= 0:
      raise ValueError('fontsize must be positive')
    if centerPt and not isinstance(centerPt, Point):
      raise TypeError('center must be a Point')

    Drawable.__init__(self)
    self._text = message
    self._size = fontsize
    self._color = Color("black")
    if centerPt:
      self.move(centerPt.getX(), centerPt.getY())
      
  def _noAutomaticCall(self):
    pass

  def setMessage(self, message):
    """Set the string to be displayed.

    message  a string
    """
    if not isinstance(message,str):
      raise TypeError('message must be a string')
    self._text = message
    self._objectChanged(False,True,False)

  def getMessage(self):
    """Return the current string."""
    return self._text

  def setFontColor(self, color):
    """Set the color of the font.

    The parameter can be either:
       - a string with the name of the color
       - an (r,g,b) tuple
       - an existing Color instance
    """
    old = self._color
    if isinstance(color,Color):
      self._color = color
    else:
      try:
        self._color = Color(color)
      except TypeError,te:
        raise TypeError(str(te))
      except ValueError,ve:
        raise ValueError(str(ve))
    
    if self._color is not old:
      self._color._register(self)
      # no longer using the old color
      old._unregister(self)
        
    self._objectChanged(False,True,False)

  def getFontColor(self):
    """Return the current font color."""
    return self._color

  def setFontSize(self, fontsize):
    """Set the font size."""
    if not isinstance(fontsize,int):
      raise TypeError('fontsize must be an integer')
    if fontsize <= 0:
      raise ValueError('fontsize must be positive')
    self._size = fontsize
    self._objectChanged(False,True,False)

  def getFontSize(self):
    """Return the current font size."""
    return size

  def rotate(self,angle):
    """Not yet implemented."""
    raise NotImplementedError('rotating text is not yet implemented')
    
  def scale(self,factor):
    """Not yet implemented."""
    raise NotImplementedError('scaling text is not yet implemented.  Use setSize to change font')
 
  def getDimensions(self):
    """Return a (width,height) tuple measuring visual dimensions of currently displayed message."""
    #return .75*self._size*(2+len(self._text)), 2.*self._size
    return _graphicsManager.addCommandToQueue(("get text size", self._text, self._size), True)
 
  def _draw(self):
    self._beginDraw()

    _graphicsManager.addCommandToQueue(("draw text", self))
    
    self._completeDraw()

class Button(Text, Rectangle, EventHandler):
  """A button that can respond to events."""
  def __init__(self, message="", centerPt=None):
    """Create a new button.
    
    The width and height of the button automatically adjust
    to the size of the displayed text.
    
    message   the text to display on the button
    centerPt  where to place the center of the button
    """
    Text.__init__(self, message)
    w, h = self.getDimensions()
    Rectangle.__init__(self, w+self._size, h+self._size, centerPt)
    EventHandler.__init__(self)
    self._baseBorderWidth = self._borderWidth

    self.setFillColor("white")
    self.addHandler(self)
  
  def _noAutomaticCall(self):
    pass
  
  def _resize(self):
    w, h = self.getDimensions()
    self.setWidth(w+self._size)
    self.setHeight(h+self._size)

  def handle(self, event):
    """Highlight the button when the button is clicked."""
    if _debug >= 3:
      print "Button self handler"
    if event._eventType == "mouse click":
      Rectangle.setBorderWidth(self, self._baseBorderWidth + 2)
    elif event._eventType == "mouse release":
      Rectangle.setBorderWidth(self, self._baseBorderWidth)

  def _draw(self):
    self._beginDraw()
    Rectangle._draw(self)
    Text._draw(self)
    self._completeDraw()

  def setBorderWidth(self, width):
    """
    Set the width of the border to the indicated width.
    """
    self._baseBorderWidth = width
    Rectangle.setBorderWidth(self, width)
    
  def setMessage(self, message):
    """Changes the button's text to message and automatically resizes the button."""
    Text.setMessage(self, message)
    self._resize()
    
  def setFontSize(self, fontsize):
    """Changes the button's text size and automatically resizes the button."""
    Text.setFontSize(self, fontsize)
    self._resize()
    
    
class TextBox(Text, Rectangle, EventHandler):
  """Widget for text entry."""
  def __init__(self, width=100, height=50, centerPt=None):
    """Construct a box to enter text into.
    
    width     the width of the box
    height    the height of the box
    centerPt  the location of the boxes center
    """
    Text.__init__(self, '', 12, centerPt)
    Rectangle.__init__(self, width, height, centerPt)
    self.setFillColor('white')     # rectangle interior was transparent by default
    EventHandler.__init__(self)
    self.addHandler(self)
      
  def _noAutomaticCall(self):
    pass

  def _draw(self):
    self._beginDraw()
    Rectangle._draw(self)          # access the overridden Rectangle version of _draw
    Text._draw(self)               # access the overridden Text version of _draw
    self._completeDraw()
    
  def handle(self, event):
    """When the text box is in focus append any keypress to the display text."""
    if event._eventType == 'keyboard':
      if event.getKey() == '\b':
        self.setMessage(self.getMessage()[:-1])
      else:
        self.setMessage(self.getMessage() + event.getKey())

    
class Timer(_EventTrigger):
  def __init__(self, delay, repeat=False):
    _EventTrigger.__init__(self)
    self._delay = delay
    self._repeat = repeat
    self._running = False
    self._handlers = list()
    
  def start(self, force=False):
    if not self._running or force:
      self._running = True
      self._thread = _TimerThread(self, self._delay)
      self._thread.start()
    
  def stop(self):
    self._running = False
    
  def addHandler(self, handler):
    if not isinstance(handler, EventHandler):
      raise TypeError('Only child classes of EventHandler can handle events')
    if handler not in self._handlers:
      self._handlers.append(handler)
    else:
      raise ValueError('Handler is already associated to the shape')
    
  def removeHandler(self, handler):
    if handler in self._handlers:
      self._handlers.remove(handler)
    else:
      raise ValueError('Cannot remove hander from shape it is not associated to')
    
class _TimerThread(_threading.Thread):
  def __init__(self, timer, delay):
    _threading.Thread.__init__(self)
    self._timer = timer
    self._delay = delay
    
  def run(self):
    _time.sleep(self._delay)
    if self._timer._repeat and self._timer._running:
      self._timer.start(True)
    if self._timer._running:
      for handler in self._timer._handlers:
        e = Event()
        e._eventType = 'timer'
        handler.handle(e)
        
class Monitor(object):
  """Monitor class for thread synchronization."""
  def __init__(self):
    """Create a new monitor instance."""
    self._lock = _threading.Lock()
    self._lock.acquire()
    
  def wait(self):
    """Wait for the monitor to be released by another thread."""
    self._lock.acquire()
    
  def release(self):
    """Release a thread that is waiting on the monitor."""
    if self._lock.locked():
      self._lock.release()

try:
  import Tkinter as _Tkinter

  _tkroot = None

  _underlyingLibrary = 'Tkinter'

  class _TkGraphicsManager(_GraphicsManager):
    def removeUnderlying(self, chain):
      if _debug >= 2:
        print "Removing underlying object", chain
      chain[0][0]._canvas._canvas.delete(self._underlyingObject[chain]._object)
      self._underlyingObject.pop(chain)
      
  _UnderlyingManager = _TkGraphicsManager

  class _RenderedCanvas(object):
    def __init__(self, canvas, w, h, background, title, refresh):
      if _debug >= 2: print "Creating _RenderedCanvas"
      self._parent = canvas
      
      self._tkWin = _Tkinter.Toplevel()
      self._tkWin.protocol("WM_DELETE_WINDOW", self._parent.close)
      self._tkWin.title(title)
      self._canvas = _Tkinter.Canvas(self._tkWin,width=w,height=h,background=getTkColor(background))
      self._canvas.pack(expand=False,side=_Tkinter.TOP)
      self._tkWin.resizable(0,0)

      # Setup function to deal with events
      callback = lambda event : self._handleEvent(event)
      self._canvas.bind('<Button>', callback)
      self._canvas.bind('<ButtonRelease>', callback)
      self._canvas.bind('<Key>', callback)
      self._canvas.bind('<Motion>', callback)
      self._canvas.bind('<Enter>', callback)
      self._canvas.focus_set()
  
    def setBackgroundColor(self, color):
      self._canvas.config(background=getTkColor(color))
  
    def setWidth(self, w):
      self._canvas.config(width=w)
  
    def setHeight(self, h):
      self._canvas.config(height=h)
  
    def setTitle(self, title):
      self._tkWin.title(title)

    def saveToFile(self, filename):
      self._canvas.postscript(file=filename)

    def _handleEvent(self, event):
      global _graphicsManager
      if _debug >= 3:
        print "Event happened", self, event.type, event.x, event.y, event.char
        print "Overlapping:", self._canvas.find_overlapping(event.x, event.y, event.x, event.y)
        
      # Create the event
      e = Event()
      if not _graphicsManager._mousePrevPosition:
        e._prevx, e._prevy = event.x, event.y
      else:
        e._prevx, e._prevy = _graphicsManager._mousePrevPosition[0], _graphicsManager._mousePrevPosition[1]
      _graphicsManager._mousePrevPosition = (int(event.x), int(event.y))
      e._x, e._y = event.x, event.y
      
      if int(event.type) == 2:   # Keypress
        e._eventType = 'keyboard'
        if event.char:
          e._key = event.char
        else:
          if event.keysym == 'Return':
            e._key = '\n'
          elif event.keysym == 'BackSpace':
            e._key = '\b'
          elif event.keysym == 'Tab':
            e._key = '\t'
          else:
            return  # ignore this event.
      elif int(event.type) == 4: # Mouse click
        e._eventType = 'mouse click'
        _graphicsManager._mouseButtonDown = True
      elif int(event.type) == 5: # Mouse release
        e._eventType = 'mouse release'
        _graphicsManager._mouseButtonDown = False
      elif int(event.type) == 6: # Mouse move
        if _graphicsManager._mouseButtonDown:
          e._eventType = 'mouse drag'
        else:
          return
      else:
        return
        
      if _debug >= 2:
        print "Event triggered", e._eventType, e._x, e._y, e._prevx, e._prevy, e._key
        
      # Find the shape where the event occurred:
      tkIds = self._canvas.find_overlapping(event.x, event.y, event.x, event.y)
      chain = ((self._parent, None), )
      if len(tkIds) > 0:
        for c in _graphicsManager._renderOrder[self._parent]:
          if _graphicsManager._underlyingObject.has_key(c) and _graphicsManager._underlyingObject[c]._object == tkIds[-1]:
            chain = c
        
      # Trigger the event handler(s)
      for i in range(len(chain),0,-1):
        subchain = chain[:i]
        p = _graphicsManager._transform.get(subchain, _Transformation()).image(Point(event.x, event.y))
        e.x, e.y = p._x, p._y
          
        triggered = _graphicsManager.triggerHandler(subchain[-1][0], e)
          
        if triggered:
          break
      
  def getTkColor(color):
    if color._transparent:
      return ""
    return "#%04X%04X%04X" % (256*color.getColorValue()[0], 256*color.getColorValue()[1], 256*color.getColorValue()[2])
  
  class _RenderedDrawable(object):
    def __init__(self, drawable, canvas):
      self._drawable = drawable
      self._canvas = canvas
      self._object = None
  
    def update(self, transform, force=True):
      if _graphicsManager._needsUpdatingInfo[2] or force:
        if _debug >= 2:
          print "Adjusting object depth", _graphicsManager._currentChain, force, _graphicsManager._needsUpdatingInfo
        # Fix the depth
        below = None
        if len(_graphicsManager._renderOrder[_graphicsManager._currentCanvas]) > 1:
          for k in _graphicsManager._renderOrder[_graphicsManager._currentCanvas][-2::-1]:
            if _graphicsManager._underlyingObject.has_key(k):
              below = _graphicsManager._underlyingObject[k]._object
              break
        if below:
          self._canvas._canvas._canvas.lift(self._object, below)
        else:
          self._canvas._canvas._canvas.lower(self._object)
    
    def remove(self, doRefresh=True):
      self._canvas._canvas.remove(self, doRefresh)
  
  class _RenderedShape(_RenderedDrawable):
    def __init__(self, drawable, canvas):
      _RenderedDrawable.__init__(self, drawable, canvas)
  
  class _RenderedFillableShape(_RenderedShape):
    def __init__(self, drawable, canvas):
      _RenderedShape.__init__(self, drawable, canvas)
  
    def update(self, transform, force=True):
      if _graphicsManager._needsUpdatingInfo[1] or force:
	if self._drawable._borderWidth > 0:
          self._canvas._canvas._canvas.itemconfigure(self._object, fill=getTkColor(self._drawable._fillColor), outline=getTkColor(self._drawable._borderColor), width=self._drawable._borderWidth)
        else:
          self._canvas._canvas._canvas.itemconfigure(self._object, fill=getTkColor(self._drawable._fillColor), outline=None)
      _RenderedShape.update(self, transform, force)

  class _RenderedCircle(_RenderedFillableShape):
    def __init__(self, drawable, canvas, transform):
      _RenderedFillableShape.__init__(self, drawable, canvas)
      center = transform.image(Point(0.,0.))
      det = transform.det()
      if det > 0.:
        radius = _math.sqrt(det)
      else:
        radius = 0.
                                
      points = []
      for i in range(0,360,5):
        points.append(Point(1,0) ^ i)
      statement = "self._object = canvas._canvas._canvas.create_polygon("
      for p in points:
        statement += str(transform.image(p).getX()) + ", " + str(transform.image(p).getY()) + ", "
      statement += "smooth=1)"
      exec statement
       
      _RenderedFillableShape.update(self, transform, True)
  
    def update(self, transform, force=True):
      # Update size and position      
      if _graphicsManager._needsUpdatingInfo[0]:
        center = transform.image(Point(0.,0.))
        radius = _math.sqrt(abs(transform.det()))
      
      points = []
      for i in range(0,360,10):
        points.append(Point(1,0) ^ i)
      statement = "self._canvas._canvas._canvas.coords(self._object"
      for p in points:
        statement += ", " + str(transform.image(p).getX()) + ", " + str(transform.image(p).getY())
      statement += ")"
      exec statement
      _RenderedFillableShape.update(self, transform, force)

  class _RenderedRectangle(_RenderedFillableShape):
    def __init__(self, drawable, canvas, transform):
      _RenderedFillableShape.__init__(self, drawable, canvas)
      
      points = [Point(-.5,-.5), Point(-.5,.5), Point(.5,.5), Point(.5,-.5)]
      for i in range(4):
        points[i] = transform.image(points[i])
      self._object = canvas._canvas._canvas.create_polygon(points[0].get(), points[1].get(), points[2].get(), points[3].get())
      _RenderedFillableShape.update(self, transform, True)

    def update(self, transform, force=True):
      if _graphicsManager._needsUpdatingInfo[0] or force:
        points = [Point(-.5,-.5), Point(-.5,.5), Point(.5,.5), Point(.5,-.5)]
        for i in range(4):
          points[i] = transform.image(points[i])
        self._canvas._canvas._canvas.coords(self._object, points[0].getX(), points[0].getY(), points[1].getX(), points[1].getY(),
                          points[2].getX(), points[2].getY(), points[3].getX(), points[3].getY())
      _RenderedFillableShape.update(self, transform, force)

  class _RenderedPath(_RenderedShape):
    def __init__(self, drawable, canvas, transform, points):
      _RenderedShape.__init__(self, drawable, canvas)

      if len(points) > 1:
        tkPts = [(transform.image(p).getX(),transform.image(p).getY()) for p in points]
        self._object = canvas._canvas._canvas.create_line(tkPts,fill=getTkColor(self._drawable._borderColor),  width=self._drawable._borderWidth)
  
        _RenderedShape.update(self, transform, True)
      else:        
        tkPts = [(0,0)] * 3
        self._object = canvas._canvas._canvas.create_line(tkPts,fill=None,width=0)

    def update(self, transform, force=True):
      if _graphicsManager._needsUpdatingInfo[0] or force:
        self._canvas._canvas._canvas.itemconfigure(self._object, fill=getTkColor(self._drawable._borderColor))
  
        if len(self._drawable.getPoints()) > 1:
          tkCoords = []
          for p in self._drawable.getPoints():
            tkCoords.append(transform.image(p).getX())
            tkCoords.append(transform.image(p).getY())
          tkCoords = tuple(tkCoords)
          self._canvas._canvas._canvas.coords(self._object,tuple(tkCoords))
    
          _RenderedShape.update(self, transform, force)
        else:
          pass

  class _RenderedPolygon(_RenderedFillableShape):
    def __init__(self, drawable, canvas, transform, points):
      _RenderedFillableShape.__init__(self, drawable, canvas)

      if len(points) > 2:
        tkPts = [(transform.image(p).getX(),transform.image(p).getY()) for p in points]
        self._object = canvas._canvas._canvas.create_polygon(tkPts)
        
        _RenderedFillableShape.update(self, transform, True)
      else:
        tkPts = [(0,0)] * 3
        self._object = canvas._canvas._canvas.create_polygon(tkPts,fill=None,width=0)
      

    def update(self, transform, force=True):
      if _graphicsManager._needsUpdatingInfo[0]:
        if len(self._drawable.getPoints()) > 2:
          tkCoords = []
          for p in self._drawable.getPoints():
            tkCoords.append(transform.image(p).getX())
            tkCoords.append(transform.image(p).getY())
          tkCoords = tuple(tkCoords)
          self._canvas._canvas._canvas.coords(self._object,tuple(tkCoords))
          
          _RenderedFillableShape.update(self, transform, force)
        else:
          pass
      

  class _RenderedText(_RenderedDrawable):
    def __init__(self, drawable, canvas, transform):
      _RenderedDrawable.__init__(self, drawable, canvas)
      center = transform.image(Point(0.,0.))
      
      self._object = canvas._canvas._canvas.create_text(center.get(), text=drawable._text, anchor='center',
              fill=getTkColor(drawable._color), font=('Helvetica', drawable._size, 'normal') )
      _RenderedDrawable.update(self, transform, True)
  
    def update(self, transform, force=True):
      if _graphicsManager._needsUpdatingInfo[0] or force:
        # Update size and position
        center = transform.image(Point(0.,0.))
  
        self._canvas._canvas._canvas.coords(self._object, center.getX(), center.getY())
      if _graphicsManager._needsUpdatingInfo[1]:
        self._canvas._canvas._canvas.itemconfigure(self._object, font=('Helvetica', self._drawable._size, 'normal'), fill=getTkColor(self._drawable._color), text=self._drawable._text)
      _RenderedDrawable.update(self, transform, force)

  def _startCommandThread():
    global _tkroot
    try:
      _tkroot = _Tkinter.Tk()
    except:
      raise StandardError('Unable to start Tkinter on your system')
      _graphicsManager._running = False
    _tkroot.withdraw()

    while _graphicsManager._running:
      _graphicsManager.processCommands()
      if _graphicsManager._forceUpdates:
        _tkroot.update()
      _time.sleep(.01)
      
  _tkroot = None

except ImportError:
  print "Tkinter is not available on your system.  It must be installed to use cs1graphics."

def _stopCommandThread():
  while len(_graphicsManager._openCanvases) > 0:
    _time.sleep(.25)
  _graphicsManager._running = False
  _time.sleep(.25)

_graphicsManager = _UnderlyingManager()

# Start command thread
_thread.start_new_thread(_startCommandThread, ())
_atexit.register(_stopCommandThread)

