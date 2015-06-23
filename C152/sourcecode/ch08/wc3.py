# Program: wc3.py
# Authors: Michael H. Goldwasser
#          David Letscher
#
# This example is discussed in Chapter 8 of the book
# Object-Oriented Programming in Python
#
filename = raw_input('What is the filename? ')
source = file(filename)

numlines = numwords = numchars = 0
for line in source:
  numchars += len(line)
  numwords += len(line.split())
  numlines += 1

print numlines, numwords, numchars
source.close()
