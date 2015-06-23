# Program: gcdSlow.py
# Authors: Michael H. Goldwasser
#          David Letscher
#
# This example is discussed in Chapter 5 of the book
# Object-Oriented Programming in Python
#
u = int(raw_input('Enter first number: '))
v = int(raw_input('Enter second number: '))

guess = min(u,v)                             # can't be bigger than this
while u % guess > 0 or v % guess > 0:        # nonzero remainder
  guess -= 1

print 'The gcd is', guess
