# Program: pyramidNested.py
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
  # all blocks at this level have same y-coordinate
  centerY = (level + 1) * unitSize
  leftmostX = centerX - unitSize * level / 2.0
  for blockCount in range(level + 1):
    block = Square(unitSize)
    block.move(leftmostX + unitSize * blockCount, centerY)
    block.setFillColor('gray')
    paper.add(block)
