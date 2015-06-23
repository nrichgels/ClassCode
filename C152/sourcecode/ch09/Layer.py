# Program: Layer.py
# Authors: Michael H. Goldwasser
#          David Letscher
#
# This example is discussed in Chapter 9 of the book
# Object-Oriented Programming in Python
#
from cs1graphics import Drawable, _GraphicsContainer

class Layer(Drawable, _GraphicsContainer):
  """
  Stores a group of shapes that can act as one drawable object.
  """
  
  def __init__(self):
    """
    Construct a new instance of Layer.
    """
    Drawable.__init__(self)
    _GraphicsContainer.__init__(self)

  def _draw(self):
    """
    Renders the group of objects to the screen.
    """
    self._beginDraw()                  # required protocol
    for shape in self.getContents():
      shape._draw()
    self._completeDraw()               # required protocol

