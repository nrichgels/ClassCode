# Program: annotate.py
# Authors: Michael H. Goldwasser
#          David Letscher
#
# This example is discussed in Chapter 8 of the book
# Object-Oriented Programming in Python
#
from FileUtilities import openFileReadRobust, openFileWriteRobust

print 'This program annotates a file, by adding'
print 'Line numbers to the left of each line.\n'

source = openFileReadRobust()
annotated = openFileWriteRobust('annotated.txt')

# process the file
linenum = 1
for line in source:
  annotated.write('%4d  %s' % (linenum, line) )
  linenum += 1
source.close()
annotated.close()
print 'The annotation is complete.'
