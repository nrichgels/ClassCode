# Program: Square.py
# Authors: Michael H. Goldwasser
#          David Letscher
#
# This example is discussed in Chapter 9 of the book
# Object-Oriented Programming in Python
#
class Square(Rectangle):
  """
  A square that can be drawn to a canvas.
  """
  def __init__(self, size=10, center=None):
    """
    Construct a new instance of Square.

    The reference point for a square is its center.

    size        the dimension of the square (defaults 10)
    center      a Point representing the placement of the rectangle's center
                (default Point(0,0) )
    """
    Rectangle.__init__(self, size, size, center)

  def setWidth(self, width):
    """
    Set the length and width of the square to size.
    """
    self.setSize(width)

  def setHeight(self, height):
    """
    Set the length and width of the square to size.
    """
    self.setSize(height)

  def setSize(self, size):
    """
    Set the length and width of the square to size.
    """
    Rectangle.setWidth(self, size)                # parent version of this method
    Rectangle.setHeight(self, size)               # parent version of this method

  def getSize(self):
    """
    Returns the length of a side of the square.
    """
    return self.getWidth()
