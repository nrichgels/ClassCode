# Program: enterNames.py
# Authors: Michael H. Goldwasser
#          David Letscher
#
# This example is discussed in Chapter 5 of the book
# Object-Oriented Programming in Python
#
guests = []
name = 'fake'
while name:
  name = raw_input('Enter a name (blank to end): ')
  guests.append(name)
guests.pop()                                        # remove the very last (blank) entry
print 'You entered', len(guests), 'guests.'
