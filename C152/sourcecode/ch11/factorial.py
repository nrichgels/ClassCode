# Program: factorial.py
# Authors: Michael H. Goldwasser
#          David Letscher
#
# This example is discussed in Chapter 11 of the book
# Object-Oriented Programming in Python
#
def factorial(n):
  """Compute the factorial of n.

  n is presumed to be a positive integer.
  """
  if n <= 1:
    return 1
  else:
    return n * factorial(n-1)
    
