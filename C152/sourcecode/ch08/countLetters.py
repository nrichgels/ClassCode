# Program: countLetters.py
# Authors: Michael H. Goldwasser
#          David Letscher
#
# This example is discussed in Chapter 8 of the book
# Object-Oriented Programming in Python
#
from FileUtilities import openFileReadRobust, openFileWriteRobust
from TallySheet import TallySheet

print 'This program counts the frequency of letters.'
print 'Only alphabetic characters are considered.\n'

sheet = TallySheet('A', 'Z')
source = openFileReadRobust()
character = 'FAKE'             # forces us inside the loop
while character:
  character = source.read(1)   # read single (ascii) character
  if character.isalpha():
    sheet.increment(character.upper())
source.close()    

tallyfile = openFileWriteRobust('frequencies.txt')
sheet.writeTable(tallyfile)
tallyfile.close()
print 'The tally has been written.'
