# Program: Score.py
# Authors: Michael H. Goldwasser
#          David Letscher
#
# This example is discussed in Chapter 7 of the book
# Object-Oriented Programming in Python
#
class Score:
  """A score for a single turn from game of Mastermind.
  
  A "black" component designates the number of pegs that are
  exact matches for the answer.  A "white" component counts
  pegs that are correctly colored but not well positioned.
  """
  
  def __init__(self, numBlack, numWhite):
    """Create score with given black and white components."""
    self._numBlack = numBlack
    self._numWhite = numWhite
    
  def getNumBlack(self):
    """Return the black component of the score."""
    return self._numBlack

  def getNumWhite(self):
    """Return the white component of the score."""
    return self._numWhite
