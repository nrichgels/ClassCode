# Program: Bullseye.py
# Authors: Michael H. Goldwasser
#          David Letscher
#
# This example is discussed in Chapter 11 of the book
# Object-Oriented Programming in Python
#
from cs1graphics import *

class Bullseye(Drawable):
  """Represent a bullseye with an arbitrary number of bands."""

  def __init__(self, numBands, radius, primary='black', secondary='white'):
    """Create a bullseye object with alternating colors.

    The reference point for the bullseye will be its center.

    numBands         the number of desired bands (must be at least 1)
    radius           the total radius for the bullseye (must be positive)
    primary          the color of the outermost band (default black)
    secondary        the color of the secondary band (default white)
    """
    if numBands <= 0:
      raise ValueError('Number of bands must be positive')
    if radius <= 0:
      raise ValueError('radius must be positive')

    Drawable.__init__(self)                            # must call parent constructor
    self._outer = Circle(radius)
    self._outer.setFillColor(primary)

    if numBands == 1:
      self._rest = None
    else:  # create new bullseye with one less band, reduced radius, and inverted colors
      innerR = float(radius) * (numBands-1) / numBands
      self._rest = Bullseye(numBands-1, innerR, secondary, primary)

  def getNumBands(self):
    """Return the number of bands in the bullseye."""
    bandcount = 1                                      # outer is always there
    if self._rest:                                     # still more
      bandcount += self._rest.getNumBands()
    return bandcount

  def getRadius(self):
    """Return the radius of the bullseye."""
    return self._outer.getRadius()                     # ask the circle

  def setColors(self, primary, secondary):
    """Recolor the bullseye with the two specified colors.

    primary      will be used for the outermost band
    secondary    will be used for the secondary band
    """
    self._outer.setFillColor(primary)
    if self._rest:
      self._rest.setColors(secondary, primary)         # color inversion

  def _draw(self):
    self._beginDraw()                                  # required protocol for Drawable
    self._outer._draw()                                # draw the circle
    if self._rest:
      self._rest._draw()                               # recursively draw the rest
    self._completeDraw()                               # required protocol for Drawable
    

def _mainAlt():
  paper = Canvas(400, 160)

  print "\nUNIT: creating lay1"
  lay1 = Layer()

  print "\nUNIT: creating sq1"
  sq1 = Square(70, Point(130,30))

  print "\nUNIT: coloring sq1"
  sq1.setFillColor('yellow')

  print "\nUNIT: changing sq1 depth"
  sq1.setDepth(60)

  print "\nUNIT: adding sq1 to lay1"
  lay1.add(sq1)

  print "\nUNIT: creating simple bullseye"
  simple = Bullseye(3, 60)

  print "\nUNIT: moving simple bullseye"
  simple.move(65, 80)

  print "\nUNIT: changing depth of simple bullseye"
  simple.setDepth(70)

  print "\nUNIT: adding simple bullseye to lay1"
  lay1.add(simple)

  print "\nUNIT: adding lay1 to paper"
  paper.add(lay1)

  print "\nUNIT: changing depth of lay1"
  lay1.setDepth(80)
  
  print "\nUNIT: creating sq2"
  sq2 = Square(60, Point(130,120))

  print "\nUNIT: changing color of sq2"
  sq2.setFillColor('green')

  print "\nUNIT: adding sq2 to lay1"
  lay1.add(sq2)

  print "\nUNIT: changing detph of sq2"
  sq2.setDepth(90)
  

  print "\nUNIT: creating bullseye blue"
  blue = Bullseye(4, 45, 'darkblue', 'skyblue')

  print "\nUNIT: adding bullseye blue to paper"
  paper.add(blue)

  print "\nUNIT: changing depth of bullseye blue"
  blue.setDepth(75)

  print "\nUNIT: moving bullseye blue"
  blue.move(195,80)

  print "\nUNIT: creating sq3"
  sq3 = Square(35,Point(135,80))

  print "\nUNIT: changing color of sq3"
  sq3.setFillColor('orange')

  print "\nUNIT: changing depth of sq3"
  sq3.setDepth(85)

  print "\nUNIT: adding sq3 to paper"
  paper.add(sq3)
  
  raw_input('Press return to continue ')
    

if __name__ == "__main__":

  from time import sleep
  paper = Canvas(375, 160)
  sleep(2)

  simple = Bullseye(3, 60)
  paper.add(simple)
  simple.move(65, 80)
  simple.setDepth(49)

  blue = Bullseye(4, 45, 'darkblue', 'skyblue')
  paper.add(blue)
  blue.move(190,80)

  colored = Bullseye(11, 60, 'red', 'green')
  paper.add(colored)
  colored.move(320,80)
  colored.setDepth(51)
  raw_input('Press return to continue ')

  colored.setColors('red', 'yellow')
  raw_input('Press return to continue ')

  simple.move(75,0)
  raw_input('Press return to continue ')

  colored.move(-75,0)
  raw_input('Press return to continue ')

  blue.move(0,50)
  raw_input('Press return to continue ')

  blue.scale(2)
  raw_input('Press return to continue ')
