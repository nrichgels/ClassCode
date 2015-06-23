# Program: maxLength.py
# Authors: Michael H. Goldwasser
#          David Letscher
#
# This example is discussed in Chapter 5 of the book
# Object-Oriented Programming in Python
#
def maxLength(stringSeq):
  longSoFar = ''                        # empty string, by default
  for entry in stringSeq:
    if len(entry) > len(longSoFar):     # even longer
      longSoFar = entry
  return longSoFar


ingredients = ['carbonated water', 'caramel color',
   'phosphoric acid', 'sodium saccharin', 'potassium benzoate',
   'natural flavors', 'citric acid', 'caffeine',
   'potassium citrate', 'aspartame', 'dimethylpolysiloxane']

concern = maxLength(ingredients)        # calling our function
print concern
