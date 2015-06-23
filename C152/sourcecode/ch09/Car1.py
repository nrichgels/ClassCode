# Program: Car1.py
# Authors: Michael H. Goldwasser
#          David Letscher
#
# This example is discussed in Chapter 9 of the book
# Object-Oriented Programming in Python
#
from cs1graphics import *

class Car(Layer):
  def __init__(self, bodyColor='blue'):
    Layer.__init__(self)                              # call the parent constructor

    tire1 = Circle(10, Point(-20,-10))
    tire1.setFillColor('black')
    self.add(tire1)

    tire2 = Circle(10, Point(20,-10))
    tire2.setFillColor('black')
    self.add(tire2)

    self._body = Rectangle(70, 30, Point(0, -25))
    self._body.setFillColor(bodyColor)
    self._body.setDepth(60)                                 # behind the tires
    self.add(self._body)

  def setBodyColor(self, bodyColor):
    self._body.setFillColor(bodyColor)

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
  raw_input('Hit Return to Continue')

  stripe = Path(Point(-35,-25),Point(35,-25))
  stripe.setBorderWidth(4)
  racecar.add(stripe)
  raw_input('Hit Return to End')
  paper.close()
