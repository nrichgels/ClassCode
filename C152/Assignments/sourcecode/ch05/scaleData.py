# Program: scaleData.py
# Authors: Michael H. Goldwasser
#          David Letscher
#
# This example is discussed in Chapter 5 of the book
# Object-Oriented Programming in Python
#
# version without any type-checking
def scaleData(data, factor):
  for i in range(len(data)):
    data[i] = factor * data[i]

# version with complete type-checking
def scaleData(data, factor):
  if not isinstance(data, list):
    raise TypeError('data must be a list')
  for item in data:
    if not isinstance(item, (int,float)):
      raise TypeError('data items must all be numeric')
  if not isinstance(factor, (int,float)):
    raise TypeError('factor must be numeric')
  for i in range(len(data)):
    data[i] = factor * data[i]
