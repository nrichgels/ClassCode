# Program: LabeledRectangle.py
# Authors: Michael H. Goldwasser
#          David Letscher
#
# This example is discussed in Chapter 9 of the book
# Object-Oriented Programming in Python
#
from cs1graphics import *

class LabeledRectangle(Text, Rectangle):
  def __init__(self, message, width, height):
    Text.__init__(self, message)
    Rectangle.__init__(self, width, height)
    self.setFillColor('white')     # rectangle interior was transparent by default

  def _draw(self):
    self._beginDraw()
    Rectangle._draw(self)          # access the overridden Rectangle version of _draw
    Text._draw(self)               # access the overridden Text version of _draw
    self._completeDraw()

if __name__ == '__main__':
  paper = Canvas()
  sign = LabeledRectangle('This space for rent', 180, 50)
  sign.move(100,100)
  sign.setFillColor('green')
  paper.add(sign)
