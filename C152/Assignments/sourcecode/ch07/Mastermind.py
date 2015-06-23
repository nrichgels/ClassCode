# Program: Mastermind.py
# Authors: Michael H. Goldwasser
#          David Letscher
#
# This example is discussed in Chapter 7 of the book
# Object-Oriented Programming in Python
#
from Score import Score
from Pattern import Pattern

class Mastermind:
  """Main class for the Mastermind game."""

  def __init__(self, inputManager, outputManager):
    """Create a new instance of the Mastermind game.

    inputManager        instance of class that gathers input from the user
    outputManager       instance of class that displays output to the user
    """
    self._inputManager = inputManager
    self._outputManager = outputManager
    playAgain = True
    while playAgain:
      self._runSingleGame()
      playAgain = self._inputManager.queryNewGame()

  def _runSingleGame(self):
    """Play one game."""
    # get parameters from the user
    lengthOfPattern = self._inputManager.queryLengthOfPattern()
    numberOfColors = self._inputManager.queryNumberOfColors()
    maxNumberOfTurns = self._inputManager.queryNumberOfTurns()
    self._outputManager.startGame(lengthOfPattern, maxNumberOfTurns)
    
    # pick a new secret
    secret = Pattern(lengthOfPattern)
    secret.randomize(numberOfColors)

    # start playing
    round = 0
    victory = False
    while round < maxNumberOfTurns and not victory:
      round += 1
      # enact a single turn
      guess = self._inputManager.enterGuess()
      result = guess.compareTo(secret)
      self._outputManager.displayTurn(guess, result)
      if result.getNumBlack() == lengthOfPattern:
        victory = True

    if victory:
      self._outputManager.announceVictory(secret)
    else:
      self._outputManager.announceDefeat(secret)

if __name__ == '__main__':
  from TextInput import TextInput
  from TextOutput import TextOutput

  # text-based version
  palette = ('Red', 'Blue', 'Green', 'White', 'Yellow', 'Orange',
             'Purple', 'Turquoise')
  input = TextInput(palette)
  output = TextOutput(palette)
  game = Mastermind(input, output)
