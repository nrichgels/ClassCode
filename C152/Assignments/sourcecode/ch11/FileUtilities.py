# Program: FileUtilities.py
# Authors: Michael H. Goldwasser
#          David Letscher
#
# This example is discussed in Chapter 8 of the book
# Object-Oriented Programming in Python
#
"""A few utility functions for opening files."""
def openFileReadRobust():
  """Repeatedly prompt user for filename until successfully opening with read access.
  
  Return the newly open file object.
  """
  source = None
  while not source:                  # still no successfully opened file
    filename = raw_input('What is the filename? ')
    try:
      source = file(filename)
    except IOError:
      print 'Sorry. Unable to open file', filename
  return source

def openFileWriteRobust(defaultName):
  """Repeatedly prompt user for filename until successfully opening with write access.

  Return a newly open file object with write access.

  defaultName     a suggested filename. This will be offered within the prompt and 
                  used when the return key is pressed without specifying another name.
  """
  writable = None
  while not writable:                # still no successfully opened file
    prompt = 'What should the output be named [%s]? '% defaultName
    filename = raw_input(prompt)
    if not filename:                 # user gave blank response
      filename = defaultName         # try the suggested default
    try:
      writable = file(filename, 'w')
    except IOError:
      print 'Sorry. Unable to write to file', filename
  return writable

def readWordFile():
  """Open and read a file of words.

  Return the list of strings.
  The file format is expected to be with one word specified per line.
  """
  print "About to read list of words from file."
  wordfile = openFileReadRobust()

  words = list()
  for entry in wordfile:
    words.append(entry.rstrip('\n'))

  return words
    
