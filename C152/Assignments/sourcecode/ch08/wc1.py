# Program: wc1.py
# Authors: Michael H. Goldwasser
#          David Letscher
#
# This example is discussed in Chapter 8 of the book
# Object-Oriented Programming in Python
#
filename = raw_input('What is the filename? ')
source = file(filename)  # read-only access

text = source.read()     # read the entire contents as one string
numchars = len(text)
numwords = len(text.split())
numlines = len(text.split('\n'))

print numlines, numwords, numchars
source.close()
