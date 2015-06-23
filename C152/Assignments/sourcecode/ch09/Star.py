# Program: Star.py
# Authors: Michael H. Goldwasser
#          David Letscher
#
# This example is discussed in Chapter 9 of the book
# Object-Oriented Programming in Python
#
from cs1graphics import *

class Star(Polygon):
  def __init__(self, numRays=5, outerRadius=10, innerRatio=.5, center=Point(0,0)):
    Polygon.__init__(self)                    # call the parent constructor
    top = Point(0, -outerRadius)              # top point is directly above the origin
    angle = 180.0 / numRays
    
    for i in range(numRays):
      self.addPoint(top ^ (angle * (2 * i)))                   # outer point
      self.addPoint(innerRatio * top ^ (angle * (2 * i + 1)))  # inner point

    self.adjustReference(0, outerRadius)      # move reference from top point to center
    self.move(center.getX(), center.getY())   # re-center entire star
    self._innerRatio = innerRatio             # record as an attribute

  def setInnerRatio(self, newRatio):
    factor = newRatio / self._innerRatio
    self._innerRatio = newRatio
    for i in range(1, self.getNumberOfPoints(), 2):            # inner points only
      self.setPoint(factor * self.getPoint(i), i)


if __name__ == '__main__':
  from time import sleep
  
  paper = Canvas(500,300)
  paper.setBackgroundColor('midnightblue')
  castor = Star()
  paper.add(castor)
  castor.move(250,150)
  castor.setFillColor('lightpink')
  castor.setBorderColor('lightpink')

  raw_input('Press Return to Continue')

  for steps in range(9):
    castor.rotate(20)
    sleep(0.25)

  raw_input('Press Return to Continue')

  altair = Star(8)
  altair.move(300,100)
  altair.setBorderColor('white')
  altair.setFillColor('white')
  paper.add(altair)

  raw_input('Press Return to Continue')

  altair.scale(2)

  raw_input('Press Return to Continue')

  sun = Star(20,40)
  sun.move(100,200)
  sun.setBorderColor('yellow')
  sun.setFillColor('yellow')
  paper.add(sun)

  raw_input('Press Return to Continue')


  test = Canvas(500,500)
  spot = Circle(5,Point(250,250))
  spot.setFillColor('black')
  spot.setDepth(0)
  test.add(spot)

  raw_input('Press Return to Continue')

  starA = Star(6, 50, .5, Point(0,0))
  starA.setDepth(10)
  starA.move(250,250)
  test.add(starA)

  raw_input('Press Return to Continue')

  starB = Star(8, 70, .5, Point(0,0))
  starB.setDepth(20)
  starB.moveTo(250,250)
  test.add(starB)

  raw_input('Press Return to Continue')

  starC = Star(5, 100, .5, Point(250,250))
  starC.setDepth(30)
  test.add(starC)

  raw_input('Press Return to Continue')

  for i in range(180):
    starA.rotate(2)
    starB.rotate(2)
    starC.rotate(2)

  raw_input('Press Return to End')
  paper.close()
  test.close()
