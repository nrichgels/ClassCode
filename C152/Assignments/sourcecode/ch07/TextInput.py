# Program: TextInput.py
# Authors: Michael H. Goldwasser
#          David Letscher
#
# This example is discussed in Chapter 7 of the book
# Object-Oriented Programming in Python
#
from Pattern import Pattern

class TextInput:
  """Class for dealing with text-based input for the Mastermind game."""
  
  def __init__(self, colorNames):
    """Create a new text input instance.

    colorNames       a sequence of strings (each color must start with a different letter)
    """
    self._lengthOfPattern = 0                  # will later be queried from the user
    self._palette = ''                         # initials for color choices, e.g., R for red
    for color in colorNames:
      self._palette += color[0].upper()

  def _readInt(self, prompt, small, large):
    """Robustly prompt the user for an integer from small to large."""
    prompt = prompt + ' (from ' + str(small) + ' to ' + str(large) + ')? '
    answer = small - 1                         # intentionally invalid
    while not small <= answer <= large:
      try:
        answer = int(raw_input(prompt))
        if not small <= answer <= large:
          print 'Integer must be from '+str(small)+' to '+str(large)+'.'
      except ValueError:
        print 'That is not a valid integer.'
    return answer

  def queryLengthOfPattern(self):
    """Ask the user how many pegs in the secret pattern."""
    self._lengthOfPattern = \
                  self._readInt('How many pegs are in the secret', 1, 10)
    return self._lengthOfPattern
  
  def queryNumberOfColors(self):
    """Ask the user how many colors to use for secret pattern."""
    self._numColorsInUse = \
       self._readInt('How many colors are available', 2, len(self._palette))
    return self._numColorsInUse
  
  def queryNumberOfTurns(self):
    """Ask the user maximum number of guesses to be allowed."""
    return self._readInt('How many turns are allowed', 1, 20)
  
  def queryNewGame(self):
    """Offer the user a new game. Return True if accepted, False otherwise."""
    print
    response = raw_input('Would you like to play again? ')
    return response.lower() in ('y', 'yes')
  
  def enterGuess(self):
    """Get a guess from the user and return it as a Pattern instance."""
    validPattern = False
    while not validPattern:
      print                                    # intentional blank line
      prompt = 'Enter a guess (colors are '
      prompt += self._palette[:self._numColorsInUse] + '): '
      patternString = raw_input(prompt)
      
      validPattern = True
      if len(patternString) != self._lengthOfPattern:
        print 'The pattern must have', self._lengthOfPattern, 'pegs'
        validPattern = False
      else:
        for i in range(self._lengthOfPattern):
          if patternString[i].upper() not in self._palette[:self._numColorsInUse]:
            validPattern = False
        if not validPattern:
          print 'The color options are', self._palette[:self._numColorsInUse]
          
      if validPattern:
        pattern = Pattern(self._lengthOfPattern)
        for i in range(self._lengthOfPattern):
          pattern.setPegColor(i, self._palette.index(patternString[i].upper()))

    return pattern
