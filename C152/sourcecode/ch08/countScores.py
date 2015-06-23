# Program: countScores.py
# Authors: Michael H. Goldwasser
#          David Letscher
#
# This example is discussed in Chapter 8 of the book
# Object-Oriented Programming in Python
#
from FileUtilities import openFileReadRobust, openFileWriteRobust
from TallySheet import TallySheet

print 'This program tallies a set of integer scores.'
print 'There should be one integer per line.\n'

source = openFileReadRobust()
values = []
for line in source:
  try:
    val = int(line)
    values.append(val)
  except ValueError:
    pass                # ignore noninteger line
source.close()

small = min(values)
large = max(values)
sheet = TallySheet(small, large)
for v in values:
  sheet.increment(v)

tallyfile = openFileWriteRobust('frequencies.txt')
sheet.writeTable(tallyfile)
tallyfile.close()
print 'The tally has been written.'
