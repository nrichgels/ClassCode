# Program: TextOutput.py
# Authors: Michael H. Goldwasser
#          David Letscher
#
# This example is discussed in Chapter 7 of the book
# Object-Oriented Programming in Python
#
class TextOutput:
  """Provide text-based output for the Mastermind game."""
  
  def __init__(self, colorNames):
    """Construct a new TextOutput instance.
    
    colorNames       a sequence of strings (each color must start with a different letter)
    """
    self._colorOptions = ''                               # initials for color choices
    for color in colorNames:
      self._colorOptions += color[0].upper()
    # following will be reset when startGame is called
    self._currentTurnNum = self._lengthOfPattern = self._maxNumberOfTurns = 0

  def startGame(self, lengthOfPattern, maxNumberOfTurns):
    """Game is beginning with specified parameters."""
    self._currentTurnNum = 0
    self._lengthOfPattern = lengthOfPattern
    self._maxNumberOfTurns = maxNumberOfTurns
    
  def displayTurn(self, guess, result):
    """Display recent guess Pattern and resulting Score to the screen."""
    self._currentTurnNum += 1
    print 'On turn', self._currentTurnNum, 'of', self._maxNumberOfTurns,
    print 'guess', self._patternAsString(guess), 'scored',
    print result.getNumBlack(), 'black and', result.getNumWhite(), 'white.'

  def announceVictory(self, secret):
    """Inform the player that he/she has correctly matched the secret Pattern."""
    print
    print 'Congratulations, you won!'
    print 'The secret was', self._patternAsString(secret)

  def announceDefeat(self, secret):
    """Inform the player that he/she has lost and reveal the secret Pattern."""
    print
    print 'The secret was', self._patternAsString(secret)
    print 'Good luck next time.'

  def _patternAsString(self, thePattern):
    """Returns string representation of given Pattern using color shorthands."""
    display = ''
    for i in range(self._lengthOfPattern):
      display += self._colorOptions[thePattern.getPegColor(i)]
    return display
