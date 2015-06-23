# Program: BinarySearch.py
# Authors: Michael H. Goldwasser
#          David Letscher
#
# This example is discussed in Chapter 11 of the book
# Object-Oriented Programming in Python
#
def search(lexicon, target, start=0, stop=None):
  """Search for the target within lexicon[start:stop].

  lexicon    a list of words (presumed to be alphabetized)
  target     the desired word
  start      the smallest index at which to look (default 0)
  stop       the index before which to stop (default len(lexicon) )
  """
  if stop is None:
    stop = len(lexicon)
  if start >= stop:                                         # nothing left
    return False
  else:
    midIndex = (start + stop) // 2
    if target == lexicon[midIndex]:                         # found it
      return True
    elif target < lexicon[midIndex]:                        # check left side
      return search(lexicon, target, start, midIndex)
    else:                                                   # check right side
      return search(lexicon, target, midIndex+1, stop)
    
def prefixSearch(lexicon, target, start=0, stop=None):
  """Search to see if target occurs as a prefix of a word in lexicon[start:stop].

  lexicon    a list of words (presumed to be alphabetized)
  target     the desired word
  start      the smallest index at which to look (default 0)
  stop       the index before which to stop (default len(lexicon) )
  """
  if stop is None:
    stop = len(lexicon)
  if start >= stop:
    return False
  else:
    midIndex = (start + stop)//2
    if lexicon[midIndex].startswith(target):                # found prefix
      return True
    elif target < lexicon[midIndex]:                        # check left side
      return prefixSearch(lexicon, target, start, midIndex)
    else:                                                   # check right side
      return prefixSearch(lexicon, target, midIndex+1, stop)

if __name__ == '__main__':
  from FileUtilities import readWordFile
  lexicon = readWordFile()
  lexicon.sort()

  goal = raw_input('enter a potential word [return to quit]: ')
  while goal:
    if search(lexicon, goal):
      print goal, 'as a word: found'
    else:
      print goal, 'as a word: not found'

    if prefixSearch(lexicon, goal):
      print goal, 'as a prefix: found'
    else:
      print goal, 'as a prefix: not found'

    goal = raw_input('enter a potential word [return to quit]: ')
            
    
