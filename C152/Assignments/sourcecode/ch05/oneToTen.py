# Program: oneToTen.py
# Authors: Michael H. Goldwasser
#          David Letscher
#
# This example is discussed in Chapter 5 of the book
# Object-Oriented Programming in Python
#
number = 0                                          # not valid
while not 1 <= number <= 10:
  number = int(raw_input('Enter a number from 1 to 10: '))
  if not 1 <= number <= 10:
    print 'Your number must be from 1 to 10.'
print number, 'has been chosen'

print
print "--- version which handles invalid strings ---"
print

number = 0                                          # not valid
while not 1 <= number <= 10:
  try:
    number = int(raw_input('Enter a number from 1 to 10: '))
    if not 1 <= number <= 10:
      print 'Your number must be from 1 to 10.'
  except ValueError:
    print 'That is not a valid integer.'
print number, 'has been chosen'

print
print "--- version which handles EOF ---"
print

number = 0                                          # not valid
while not 1 <= number <= 10:
  try:
    number = int(raw_input('Enter a number from 1 to 10: '))
    if not 1 <= number <= 10:
      print 'Your number must be from 1 to 10.'
  except ValueError:
    print 'That is not a valid integer.'
  except EOFError:
    print 'Why did you do that?'
    print 'We will choose for you.'
    number = 7
  except KeyboardInterrupt:
    print 'Can we catch a keyboard interrupt?'
    print 'Yes.'
    number = 8
print number, 'has been chosen'
