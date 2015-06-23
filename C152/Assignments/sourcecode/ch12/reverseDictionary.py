# Program: reverseDictionary.py
# Authors: Michael H. Goldwasser
#          David Letscher
#
# This example is discussed in Chapter 12 of the book
# Object-Oriented Programming in Python
#
def buildReverse(dictionary):
  """Return a reverse dictionary based upon the original."""
  reverse = {}
  for key,value in dictionary.items():        # map value back to key
    if value in reverse:  
      reverse[value].append(key)              # add to existing list
    else:  
      reverse[value] = [ key ]                # establish new list
  return reverse


if __name__ == "__main__":

  original = { 'A':1, 'B':2, 'C':2, 'D':3, 'E':1, 'F':2 }
  print buildReverse(original)
    
