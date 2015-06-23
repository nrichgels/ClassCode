# Program: indexBasedDemo.py
# Authors: Michael H. Goldwasser
#          David Letscher
#
# This example is discussed in Chapter 4 of the book
# Object-Oriented Programming in Python
#
groceries = ['milk', 'cheese', 'bread', 'cereal']
count = 1
for item in groceries:
  print str(count) + '. ' + item
  count += 1
