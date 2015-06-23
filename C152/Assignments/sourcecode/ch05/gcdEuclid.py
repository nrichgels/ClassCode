# Program: gcdEuclid.py
# Authors: Michael H. Goldwasser
#          David Letscher
#
# This example is discussed in Chapter 5 of the book
# Object-Oriented Programming in Python
#
u = int(raw_input('Enter first number: '))
v = int(raw_input('Enter second number: '))

while v != 0:
  r = u % v
  u = v
  v = r

print 'The gcd is', u
