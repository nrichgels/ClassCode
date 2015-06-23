# Program: BinarySearchBad.py
# Authors: Michael H. Goldwasser
#          David Letscher
#
# This example is discussed in Chapter 11 of the book
# Object-Oriented Programming in Python
#
def search(lexicon, target):
  """Search for the target within lexicon.

  lexicon    a list of words (presumed to be alphabetized)
  target     the desired word
  """
  if len(lexicon) == 0:                                     # base case
    return False                              
  else:
    midIndex = len(lexicon) // 2
    if target == lexicon[midIndex]:                         # found it
      return True
    elif target < lexicon[midIndex]:                        # check left side
      return search(lexicon[ : midIndex], target)
    else:                                                   # check right side
      return search(lexicon[midIndex+1 : ], target)
