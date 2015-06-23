# Program: GraphicsOutput.py
# Authors: Michael H. Goldwasser
#          David Letscher
#
# This example is discussed in Chapter 7 of the book
# Object-Oriented Programming in Python
#
from cs1graphics import *

class GraphicsOutput:
  """Provide graphics-based output for the Mastermind game."""
  
  def __init__(self, colorNames, pegRadius = 10):
    """Construct a new GraphicsOutput instance.

    colorNames       a sequence of strings (each color must start with a different letter)
    pegRadius        radius of a displayed peg (default 10)

    pegRadius technically describes the radius of a single peg, yet
    the entire display is scaled accordingly.
    """
    self._colorNames = colorNames
    self._pegRadius = pegRadius

    # following will be reset when game starts
    self._currentTurnNum = self._lengthOfPattern = self._maxNumberOfTurns = 0
    self._canvas = None

  def startGame(self, lengthOfPattern, maxNumberOfTurns):
    """Game is beginning with specified parameters."""
    if self._canvas:   # from previous game
      self._canvas.close()
    self._currentTurnNum = 0
    self._lengthOfPattern = lengthOfPattern
    self._maxNumberOfTurns = maxNumberOfTurns
    
    # Set the size of board that works for the given parameters
    width = (4*self._lengthOfPattern + 7) * self._pegRadius
    height = (4*self._maxNumberOfTurns + 6) * self._pegRadius
    self._canvas = Canvas(width, height, 'tan', 'Mastermind')
    self._canvas.setAutoRefresh(False)
    self._setupBackground()
    
  def _drawPattern(self, thePattern, row):
    """Display the given Pattern at indicated row."""
    for i in range(self._lengthOfPattern):
      peg = Circle(self._pegRadius, self._getCenterPoint(row, i))
      peg.setFillColor(self._colorNames[thePattern.getPegColor(i)])
      self._canvas.add(peg)

  def announceVictory(self, secret):
    """Inform the player that he/she has correctly matched the secret Pattern."""
    self._drawPattern(secret, self._maxNumberOfTurns)
    self._canvas.refresh()

  def announceDefeat(self, secret):
    """Inform the player that he/she has lost and reveal the secret Pattern."""
    self._drawPattern(secret, self._maxNumberOfTurns)
    self._canvas.refresh()

  def displayTurn(self, guess, result):
    """Display recent guess Pattern and resulting Score to the screen."""
    self._drawPattern(guess, self._currentTurnNum)

    black = Text(str(result.getNumBlack()), 2*self._pegRadius)
    black.move((4*self._lengthOfPattern+2)*self._pegRadius,
      (4*(self._maxNumberOfTurns-self._currentTurnNum-1)+7)*self._pegRadius)
    black.setFontSize(2*self._pegRadius)
    black.setFontColor('black')
    self._canvas.add(black)
    
    white = Text(str(result.getNumWhite()), 2*self._pegRadius)
    white.move((4*self._lengthOfPattern+5)*self._pegRadius,
      (4*(self._maxNumberOfTurns-self._currentTurnNum-1)+7)*self._pegRadius)
    white.setFontSize(2*self._pegRadius)
    white.setFontColor('white')
    self._canvas.add(white)

    self._canvas.refresh()
    self._currentTurnNum += 1

  def _getCenterPoint(self, row, col):
    """Locate the position for a peg.

    Return a Point instance positioned at the center of the peg.

    row     the row that the peg is in
    col     the column that the peg is in
    """
    return Point((4*col + 3) * self._pegRadius,
      (4*(self._maxNumberOfTurns-row-1) + 7) * self._pegRadius)

  def _setupBackground(self):
    """Draw the background to the graphics canvas."""
    block = Rectangle(4*self._lengthOfPattern*self._pegRadius, 4*self._pegRadius,
      Point((1 + 2*self._lengthOfPattern)*self._pegRadius, 3*self._pegRadius) )
    block.setFillColor('brown')
    block.setDepth(100)
    self._canvas.add(block)
  
    for row in range(self._maxNumberOfTurns):
      for col in range(self._lengthOfPattern):
        hole = Circle(self._pegRadius/2, self._getCenterPoint(row,col))
        hole.setFillColor('black')
        hole.setDepth(90)
        self._canvas.add(hole)
    self._canvas.refresh()

