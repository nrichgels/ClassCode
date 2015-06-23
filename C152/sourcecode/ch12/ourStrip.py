# Program: ourStrip.py
# Authors: Michael H. Goldwasser
#          David Letscher
#
# This example is discussed in Chapter 12 of the book
# Object-Oriented Programming in Python
#
def ourStrip(w):
  """
  Return a lowercase version of the word with all non-alphabetic
  symbols stripped away form the boundaries, but with such symbols
  remaining in the interior of a word.

  Typical examples of this behavior include:
      ourStrip("don't")           -->   "don't"
      ourStrip('end.')            -->   'end'
      ourStrip('jack-o-lantern')  -->   'jack-o-lantern'
      ourStrip('"Stop!"')         -->   'stop'
      ourStrip('"&%^$*%*%"')      -->   ''
  """
  first = 0                                           # locate first desirable character
  while first < len(w) and not w[first].isalpha():
    first += 1

  last = len(w)-1                                     # locate last desirable character
  while last > first and not w[last].isalpha():
    last -= 1

  return w[first:last+1].lower()                      # intentionally lowercase


if __name__ == "__main__":

    if ourStrip("don't") != "don't":
        print """PROBLEM: ourstrip("don't") is""", ourStrip("don't")
    if ourStrip('end.') != 'end':
        print """PROBLEM: ourstrip('end.') is""", ourStrip('end.')
    if ourStrip('jack-o-lantern') != 'jack-o-lantern':
        print """PROBLEM: ourstrip('jack-o-lantern') is""", ourStrip('jack-o-lantern')
    if ourStrip('"Stop!"') != 'stop':
        print """PROBLEM: ourstrip('"Stop!"') is""", ourStrip('"Stop!"')
    if ourStrip('"&%^$*%*%*"') != '':
        print """PROBLEM: ourstrip('"&%^$*%*%*"') is""", ourStrip('"&%^$*%*%*"')
