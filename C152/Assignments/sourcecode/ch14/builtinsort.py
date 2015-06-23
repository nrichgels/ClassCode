# Program: builtinsort.py
# Authors: Michael H. Goldwasser
#          David Letscher
#
# This example is discussed in Chapter 14 of the book
# Object-Oriented Programming in Python
#
data = ['bread', 'soda', 'cheese', 'milk', 'pretzels']

# approach to using decorated tuples for sorting
decorated = []
for s in data:
  decorated.append( (len(s), s) )      # add a tuple starting with length
decorated.sort()
for i in range(len(data)):
  data[i] = decorated[i][1]            # retrieve second piece of each tuple


# approach using a comparison function
def lengthCmp(a, b):
  if len(a) < len(b):
    return -1
  elif len(a) == len(b):
    return 0
  else:
    return 1

# alternate comparison function, using built-in cmp
def lengthCmp(a, b):
  return cmp(len(a), len(b))

# demonstration of use of the comparison function
data.sort(lengthCmp)                   # use our function for comparing, not the default


# decorator function
def lengthDecorator(s):
  return len(s)

# demonstration of use of decorator function
data.sort(key=lengthDecorator)         # use our decorator function

# demonstration when using str.__len__ as this function
data.sort(key=str.__len__)

# or even use the built-in len function
data.sort(key=len)
