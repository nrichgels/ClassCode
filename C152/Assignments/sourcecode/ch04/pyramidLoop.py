# Program: pyramidLoop.py
# Authors: Michael H. Goldwasser
#          David Letscher
#
# This example is discussed in Chapter 4 of the book
# Object-Oriented Programming in Python
#
from cs1graphics import *

numLevels = 8                             # number of levels
unitSize = 12                             # the height of one level
screenSize = unitSize * (numLevels + 1)
paper = Canvas(screenSize, screenSize)
centerX = screenSize / 2.0                # same for all levels

# create levels from top to bottom
for level in range(numLevels):
  width = (level + 1) * unitSize          # width varies by level
  block = Rectangle(width, unitSize)      # height is always unitSize
  centerY = (level + 1) * unitSize
  block.move(centerX, centerY)
  block.setFillColor('gray')
  paper.add(block)
