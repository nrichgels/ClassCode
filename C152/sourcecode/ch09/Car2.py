# Program: Car2.py
# Authors: Michael H. Goldwasser
#          David Letscher
#
# This example is discussed in Chapter 9 of the book
# Object-Oriented Programming in Python
#
from cs1graphics import *

class Car(Drawable):
  def __init__(self, bodyColor='blue'):
    Drawable.__init__(self)                       # call the parent constructor

    self._tire1 = Circle(10, Point(-20,-10))
    self._tire1.setFillColor('black')
    self._tire2 = Circle(10, Point(20,-10))
    self._tire2.setFillColor('black')
    self._body = Rectangle(70, 30, Point(0, -25))
    self._body.setFillColor(bodyColor)

  def setBodyColor(self, bodyColor):
    self._body.setFillColor(bodyColor)

  def _draw(self):
    self._beginDraw()                             # required protocol
    self._body._draw()
    self._tire1._draw()
    self._tire2._draw()
    self._completeDraw()                          # required protocol


if __name__ == "__main__":
  from time import sleep
  
  paper = Canvas(300,300)

  racecar = Car()
  racecar.moveTo(150,150)
  paper.add(racecar)

  raw_input('Hit Return to Continue')

  wagon = Car('green')
  wagon.moveTo(200,300)
  wagon.scale(1.5)
  paper.add(wagon)
  raw_input('Hit Return to Continue')

  racecar.setBodyColor('red')
  raw_input('Hit Return to End')
  paper.close()
