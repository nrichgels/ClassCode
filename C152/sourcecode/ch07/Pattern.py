# Program: Pattern.py
# Authors: Michael H. Goldwasser
#          David Letscher
#
# This example is discussed in Chapter 7 of the book
# Object-Oriented Programming in Python
#
from Score import Score
from random import seed, randint

class Pattern:
  """Class for storing a color pattern for Mastermind."""

  def __init__(self, numPegs):
    """Construct a new pattern.
    
    Initially, the pattern consists of numPegs pegs, each set to color 0.
    """
    self._pegList = [0] * numPegs                 # Create a list of 0's with given length

  def __len__(self):
    """Return the length of the current pattern."""
    return len(self._pegList)
    
  def getPegColor(self, index):
    """Return the current color setting (an integer) of the specified peg.

    index               the index of the peg
    """
    return self._pegList[index]

  def setPegColor(self, index, colorID):
    """Set the color of a peg at the given index of the pattern.

    index               the index of the peg
    colorID             the desired color identifier (an integer)
    """
    self._pegList[index] = colorID

  def compareTo(self, otherPattern):
    """Compare the current pattern to otherPattern and calculate the score.

    otherPattern    the pattern to be compared to the current one

    Return a Score instance representing the result.
    See the Score class for details on the components of the score.
    """
    # First calculate the black component of the score
    black = 0
    for i in range(len(self._pegList)):
      if self.getPegColor(i) == otherPattern.getPegColor(i):
        black += 1

    # The white component is a little more difficult to calculate.
    # First find out the colors used in the current pattern
    colorsUsed = []
    for color in self._pegList:
      if color not in colorsUsed:
        colorsUsed.append(color)

    # For each color used find the smaller number of times
    # it appears in each pattern and add them up.
    white = 0
    for color in colorsUsed:
      white += min(self._pegList.count(color), otherPattern._pegList.count(color))
    white -= black                                # Don't count pegs that are paired up.

    return Score(black, white)

  def randomize(self, numColors):
    """Make a random pattern.

    numColors      the maximum number of colors to use in the pattern
    """
    seed()                                        # reset random number generator
    for i in range(len(self._pegList)):
      self._pegList[i] = randint(0, numColors-1)
#######  end of Pattern class #######

if __name__ == '__main__':
  modelA = (1, 3, 0, 3, 2)                        # will use as sample pattern
  patternA = Pattern(5)
  for i in range(len(modelA)):
    patternA.setPegColor(i, modelA[i])

  if len(patternA) != 5:
    print 'Pattern length is miscalculated'
  
  for i in range(5):
    if patternA.getPegColor(i) != modelA[i]:
      print 'Color at index', i, 'not properly set/retrieved'

  copy = Pattern(5)
  for i in range(5):
    copy.setPegColor(i, patternA.getPegColor(i))

  score = patternA.compareTo(copy)
  if score.getNumBlack() != 5 or score.getNumWhite() != 0:
    print 'Score miscalcuated'

  modelB = (3, 1, 2, 3, 1)                        # another sample pattern
  patternB = Pattern(5)
  for i in range(len(modelB)):
    patternB.setPegColor(i, modelB[i])

  score = patternA.compareTo(patternB)
  if score.getNumBlack() != 1 or score.getNumWhite() != 3:      # our expected score
    print 'Score miscalcuated'

  patternB.setPegColor(1, 3)   # turns second peg to black, disqualifies a previous white
  score = patternA.compareTo(patternB)
  if score.getNumBlack() != 2 or score.getNumWhite() != 2:      # our expected score
    print 'Score miscalcuated'
