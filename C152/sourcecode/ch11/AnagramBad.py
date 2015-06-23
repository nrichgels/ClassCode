# Program: AnagramBad.py
# Authors: Michael H. Goldwasser
#          David Letscher
#
# This example is discussed in Chapter 11 of the book
# Object-Oriented Programming in Python
#
from BinarySearch import search

def anagrams(lexicon, charsToUse, prefix=''):
  """
  Return a list of anagrams, formed with prefix followed by charsToUse.

  lexicon          a list of words (presumed to be alphabetized)
  charsToUse       a string which represents the characters to be arranged
  prefix           a prefix which is presumed to come before the arrangement
                   of the charsToUse (default empty string)
  """
  solutions = []
  if len(charsToUse) > 1:
    for i in range(len(charsToUse)):         # pick charsToUse[i] next
      newPrefix = prefix + charsToUse[i]
      newCharsToUse = charsToUse[ : i] + charsToUse[i+1 : ]
      solutions.extend(anagrams(lexicon, newCharsToUse, newPrefix))
  else:     # check to see if we have a good solution
    candidate = prefix + charsToUse
    if search(lexicon, candidate):           # use binary search
      solutions.append(candidate)
  return solutions

if __name__ == '__main__':
  from FileUtilities import readWordFile
  print 'Will begin by reading the file of words.'
  words = readWordFile()
  words.sort()

  puzzle = raw_input('enter a string of characters to use: ')
  while puzzle:
    solutions = anagrams(words, puzzle)
    if solutions:
      solutions = list(set(solutions))       # remove duplicates
      solutions.sort()
      print 'Solutions include:'
      print '\n'.join(solutions)

    puzzle = raw_input('enter a string of characters to use: ')
