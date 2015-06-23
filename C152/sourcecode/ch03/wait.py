# Program: wait.py
# Authors: Michael H. Goldwasser
#          David Letscher
#
# This example is discussed in Chapter 3 of the book
# Object-Oriented Programming in Python
#
from cs1graphics import *

paper = Canvas()
light = Circle(20, Point(100,100))
light.setFillColor('red')
paper.add(light)
light.wait()
light.setFillColor('green')
paper.wait()
paper.close()

paper = Canvas()
cue = paper.wait()                                # wait indefinitely for user event
ball = Circle(10, cue.getMouseLocation())
ball.setFillColor('red')
paper.add(ball)
