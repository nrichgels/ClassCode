# Program: sqrt.py
# Authors: Michael H. Goldwasser
#          David Letscher
#
# This example is discussed in Chapter 5 of the book
# Object-Oriented Programming in Python
#
def sqrtA(number):
  guess = 1.0
  while guess != number / guess:
    guess = (guess + number / guess) / 2.0       # use average
  return guess

def sqrtAguru(number):
  guess = 1.0
  while guess * guess != number:
    guess = (guess + number / guess) / 2.0       # use average
  return guess

def sqrtB(number):
  guess = 1.0
  for trial in range(100):
    guess = (guess + number / guess) / 2.0       # use average
  return guess

def sqrtC(number, allowableError=.000001):
  guess = 1.0
  while abs(guess - number / guess) > allowableError:
    guess = (guess + number / guess) / 2.0       # use average
  return guess

def sqrtD(number):
  prevGuess = 0.0
  guess = min(1.0, number)
  while prevGuess < guess:
    prevGuess = guess
    avg = (guess + number / guess) / 2.0
    guess = min(avg, number / avg)
  return guess

def sqrtE(number):
  if number < 0:
    raise ValueError('sqrt(number): number is negative')
  prevGuess = 0.0
  guess = min(1.0, number)
  while prevGuess < guess:
    prevGuess = guess
    avg = (guess + number / guess) / 2.0
    guess = min(avg, number / avg)
  return guess

def sqrtF(number):
  if not isinstance(number, (int,float)):
    raise TypeError('sqrt(number): number must be numeric')
  if number < 0:
    raise ValueError('sqrt(number): number is negative')
  # done error checking;  can safely perform our calculation...
  prevGuess = 0.0
  guess = min(1.0, number)
  while prevGuess < guess:
    prevGuess = guess
    avg = (guess + number / guess) / 2.0
    guess = min(avg, number / avg)
  return guess
