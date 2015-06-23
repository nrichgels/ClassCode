# Program: leafcolor.py
# Authors: Michael H. Goldwasser
#          David Letscher
#
# This example is discussed in Chapter 10 of the book
# Object-Oriented Programming in Python
#
from cs1graphics import *

scene = Canvas()
trunkA = Rectangle(20, 50, Point(50,150) )
trunkA.setFillColor('brown')
trunkA.setDepth(60)
trunkB = Rectangle(20, 50, Point(150,150) )
trunkB.setFillColor('brown')
trunkB.setDepth(60)
scene.add(trunkA)
scene.add(trunkB)

leavesA = Circle(30, Point(50, 100))
leavesB = Circle(30, Point(150, 100))
seasonColor = Color('green')        # instance of Color class
leavesA.setFillColor(seasonColor)
leavesB.setFillColor(seasonColor)
scene.add(leavesA)
scene.add(leavesB)

raw_input('Press return to change seasons. ')
seasonColor.setByName('orange')     # changes leaves of both trees

raw_input('Press return to change the right-hand tree. ')
leavesB.setFillColor('yellow')      # reassigns B to a new color instance

raw_input('Press return to end. ')
scene.close()

