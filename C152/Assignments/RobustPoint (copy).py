"""
Program: RobustPoint.py
Authors: Michael H. Goldwasser
         David Letscher
Documentation added by Rick Walker

This example is discussed in Chapter 6 of the book
Object-Oriented Programming in Python
"""

from math import sqrt                      # needed for computing distances

class Point:
  # Here is a pound comment
  """ The representation of a point in Cartesian coordinates
  
  The X coordinate is the horizontal component of the Point
  The Y coordinate is the vertical component of the Point
  """

  #### CONSTRUCTOR #########################################################  
  def __init__(self, initialX=0, initialY=0):
    """ Create Point and set initial values for the X and Y coordinates.
    
    Process:  Creates a new Point and sets Point's coordinates to the input parameters
    Preconditions:  X and Y are the (numeric) horizontal and vertical components of the point, resp.
    Postconditions:  The X and Y coordinates of the new point are initialX and initialY, resp.
    """
    self._x = initialX
    self._y = initialY
  ##########################################################################
    
  #### method getX #########################################################    
  def getX(self):
    """ Return the X (horizontal) coordinate.
    
    Precondition:  None
    Postcondition:  Value of Y coordinate is returned as the value of the method.
                    Point is unchanged. 
    """   
    return self._x
  ##########################################################################
    
  #### method setX #########################################################
  def setX(self, val):
    """ Set the X (horizontal) coordinate. 
    
    Process:  Set the horizontal coordinate to the supplied value.
    Precondition:  val - int or float - intended value for the horizontal coordinate.
    Postcondition:  X coord is set to val
    Exception:  raises TypeError if val is not float or int
    """
    if not isinstance(val, (float, int)):
        raise TypeError ("Coordinate must be a float or int")
    self._x = val
  ##########################################################################
    
  #### method getY #########################################################
  def getY(self):
    """ Return the Y (vertical) coordinate.
    
    Precondition:  None
    Postcondition:  Value of Y coordinate is returned as the value of the method.
                    Point is unchanged.
    """
    return self._y
  ##########################################################################
    
  #### method setY #########################################################
  def setY(self, val):
    """ Set the Y (vertical) coordinate.

    Process:  Set the vertical coordinate to the supplied value.
    Precondition:  val - int or float - intended value for the vertical coordinate.
    Postcondition:  Y coord is set to val
    Exception:  raises TypeError if val is not float or int
    """    
    if not isinstance(val, (float, int)):
        raise TypeError ("Coordinate must be a float or int")
    self._y = val
  ##########################################################################
    
  #### method scale ########################################################
  def scale(self, factor):
    """ Multiply both coordinates by a factor.
    
    Process:  Slides point in or out along a ray from the origin thru the point
              to a position with distance from the origin being factor * current 
              distance from the origin.
    Precondition:  factor is a float or int containing the scale factor
    Postcondition:  Point is relocated on the ray from the origin and through
                    the current position.          
    """
    self._x *= factor
    self._y *= factor
  ##########################################################################
    
  #### method distance #####################################################
  def distance(self, other):
    """ Returns distance of this Point from other Point.
    
    Process:  Finds distance between current point and other
    Precondition:  other is a Point on the opposite endpoint of line
                   from current point
    Postcondition:  a float value for the distance is returned as the
                    value of the function.
                    Point is unchanged.
    """
    ###### DATA DICTIONARY ######
    # dx - numeric - difference in x values
    # dy - numeric - difference in y values
    #############################
    
    dx = self._x - other._x
    dy = self._y - other._y
    return sqrt(dx * dx + dy * dy)                    # imported from math module
  ##########################################################################
    
  #### method normalize ####################################################
  def normalize(self):
    """ Scale Point so that distance from the origin is 1.
    
    Process:  Divide coordinates by distance from origin.
    Precondition:  None
    Postcondition:  Point is relocated on the ray from the origin and through
                    the current position, at one unit from the origin.
    """
    ###### DATA DICTIONARY ######
    # mag - numeric - distance to origin
    #############################
    
    mag = self.distance( Point() )
    if mag > 0:
      self.scale(1/mag)
  ##########################################################################
    
  #### method __str __ #####################################################
  def __str__(self):
    """ 'Stringify' Point value.
    
    Precondition:  None
    Postcondition:  Returns string containing representation of the Point
                    as the value.
                    Point is unchanged.
    """
    return '<' + str(self._x) + ',' + str(self._y) + '>'
  ##########################################################################
    
  #### method __add__ for '+' operation ####################################
  def __add__(self, other):
    """ Point addition - binary operator 
    
    Process:  Adds current Point to other (right) Point operand.
    Precondition:  other is a Point
    Postcondition:  A new Point that is the sum is returned as the 
                    value of the method.
                    Value of this Point is unchanged.
    """
    return Point(self._x + other._x, self._y + other._y)
  ##########################################################################
    
  #### method __mul__ for '*' operation ####################################
  def __mul__(self, operand):
    """ Performs  scalar multiplication or finds dot product
    
    Process:  Polymorphic function finds product of this Point and right operand.
              Result type depends on type  of the right operand ...
                result is scalar (dot product) if right operand is another Point, or
                          a point if right operand is a scalar.
    Precondition:  right operand is a Point or a scalar (float or int)
    Postcondition:  returns result as the value of the function.
                    Value of operands is unchanged.
    """
    # multiply by a numerical scalar
    if isinstance(operand, (int,float)):
      return Point(self._x * operand, self._y * operand)
    # multiply by a point (dot product)
    elif isinstance(operand, Point):
      return self._x * operand._x + self._y * operand._y
  ##########################################################################
    
  #### method __rmul__ for right * operation ###############################
  def __rmul__(self, operand):
    """ Performs scalar multiplication when this Point is the right operand
    
    Process:  finds the product of a scalar (as the left operand) with 
              this Point.
    Precondition:  Left operand of multiplication is a scalar (int or float)
    Postcondition:  The scalar product is returned as the value of the operation
                    Value of operands is unchanged.
    """
    return self * operand
  ##########################################################################
                
if __name__ == '__main__':

  a = Point()
  a.setX(-5)
  a.setY(7)
  print 'a is', a                           # demonstrates __str__

  b = Point(8, 6)
  print 'b is', b

  print 'distance between is', a.distance(b)
  print '  should be same as', b.distance(a)

  c = a + b
  print 'c = a + b results in', c

  print 'magnitude of b is', b.distance(Point())
  b.normalize()
  print 'normalized b is', b
  print 'magnitude of b is', b.distance(Point())

  print 'a * b =', a * b
  print 'a * 3 =', a * 3
  print '3 * a =', 3 * a
  
  
