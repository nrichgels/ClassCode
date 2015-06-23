# Program: house.py
# Authors: Michael H. Goldwasser
#          David Letscher
#
# This example is discussed in Chapter 3 of the book
# Object-Oriented Programming in Python
#
from cs1graphics import *
paper = Canvas(300, 200, 'skyBlue', 'My World')

sun = Circle(30, Point(250,50))
sun.setFillColor('yellow')
paper.add(sun)

facade = Square(60, Point(140,130))
facade.setFillColor('white')
paper.add(facade)

chimney = Rectangle(15, 28, Point(155,85))
chimney.setFillColor('red')
chimney.setBorderColor('red')
paper.add(chimney)

tree = Polygon(Point(50,80), Point(30,140), Point(70,140))
tree.setFillColor('darkGreen')
paper.add(tree)

smoke = Path(Point(155,70), Point(150,65), Point(160,55), Point(155,50))
paper.add(smoke)

sunraySW = Path(Point(225,75), Point(210,90))
sunraySW.setBorderColor('yellow')
sunraySW.setBorderWidth(6)
paper.add(sunraySW)
sunraySE = Path(Point(275,75), Point(290,90))
sunraySE.setBorderColor('yellow')
sunraySE.setBorderWidth(6)
paper.add(sunraySE)
sunrayNE = Path(Point(275,25), Point(290,10))
sunrayNE.setBorderColor('yellow')
sunrayNE.setBorderWidth(6)
paper.add(sunrayNE)
sunrayNW = Path(Point(225,25), Point(210,10))
sunrayNW.setBorderColor('yellow')
sunrayNW.setBorderWidth(6)
paper.add(sunrayNW)

grass = Rectangle(300, 80, Point(150,160))
grass.setFillColor('green')
grass.setBorderColor('green')
grass.setDepth(75)                 # must be behind house and tree
paper.add(grass)

window = Rectangle(15, 20, Point(130,120))
paper.add(window)
window.setFillColor('black')
window.setBorderColor('red')
window.setBorderWidth(2)
window.setDepth(30)

roof = Polygon(Point(105, 105), Point(175, 105), Point(170,85), Point(110,85))
roof.setFillColor('darkgray')
roof.setDepth(30)                  # in front of facade
chimney.setDepth(20)               # in front of roof
paper.add(roof)

otherTree = tree.clone()
otherTree.move(170,30)
otherTree.scale(1.2)
paper.add(otherTree)

car = Layer()
tire1 = Circle(10, Point(-20,-10))
tire1.setFillColor('black')
car.add(tire1)

tire2 = Circle(10, Point(20,-10))
tire2.setFillColor('black')
car.add(tire2)

body = Rectangle(70, 30, Point(0, -25))
body.setFillColor('blue')
body.setDepth(60)                  # behind the tires
car.add(body)

car.moveTo(110,180)
car.setDepth(20)
paper.add(car)

from time import sleep
timeDelay = .25                    # one-quarter second
car.move(-10, 0)
sleep(timeDelay)
car.move(-30, 0)
sleep(timeDelay)
car.move(-60, 0)
sleep(timeDelay)
car.move(-100, 0)
sleep(timeDelay)
