# Program: arch.py
# Authors: Michael H. Goldwasser
#          David Letscher
#
# This example is discussed in Chapter 5 of the book
# Object-Oriented Programming in Python
#
from cs1graphics import *
from math import sqrt                                   # use the official sqrt function

# chosing constants which give nice result
numLinks            = 50
restingLength       = 20.0
totalSeparation     = 630.0
elasticityConstant  = 0.005
gravityConstant     = 0.110
epsilon             = 0.001

# convenient function for adding up to three (x,y) tuples
def combine(A, B, C=(0,0) ):
  return (A[0] + B[0] + C[0], A[1] + B[1] + C[1])

# function returns a tuple representing the force being
# exerted upon point A due to the link joining A to B.
def calcForce(A, B):
  dX = (B[0] - A[0])
  dY = (B[1] - A[1])
  distance = sqrt(dX * dX + dY * dY)
  if distance > restingLength:                          # link being stretched
    stretch = distance - restingLength
    forceFactor = stretch * elasticityConstant
  else:
    forceFactor = 0
  return (forceFactor * dX, forceFactor * dY)           # returning a tuple

# function to alter the graphical path and refresh canvas
def drawChain(chainData, chainPath, theCanvas):
  for k in range(len(chainData)):
    chainPath.setPoint(Point(chainData[k][0], chainData[k][1]), k)
  theCanvas.refresh()

# initialize the chain; one end at (0,0) other at (totalSeparation,0)
chain = []
for k in range(numLinks + 1):
  X = totalSeparation * k / numLinks
  chain.append( (X, 0.0) )                              # add new position

# initialize the graphics
paper = Canvas(totalSeparation, totalSeparation)
paper.setAutoRefresh(False)
curve = Path()
for p in chain:
  curve.addPoint(Point(p[0], p[1]))
paper.add(curve)
graphicsCounter = 100                                   # draw every 100th iteration

somethingMoved = True                                   # force loop to start
while somethingMoved:
  somethingMoved = False                                # default for new iteration
  oldChain = list(chain)                                # record a copy of the data
  for k in range(1, numLinks):                          # alter all interior points
    gravForce = (0, gravityConstant)                    # downward force
    leftForce = calcForce(oldChain[k], oldChain[k-1])
    rightForce = calcForce(oldChain[k], oldChain[k+1])
    adjust = combine(gravForce, leftForce, rightForce)
    if abs(adjust[0]) > epsilon or abs(adjust[1]) > epsilon:
      somethingMoved = True
    chain[k] = combine(oldChain[k], adjust)

  graphicsCounter -= 1
  if graphicsCounter == 0:
    drawChain(chain, curve, paper)
    graphicsCounter = 100

curve.setBorderWidth(2)                                 # emphasize final result
drawChain(chain, curve, paper)
