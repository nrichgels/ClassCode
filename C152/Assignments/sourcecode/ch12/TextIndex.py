# Program: TextIndex.py
# Authors: Michael H. Goldwasser
#          David Letscher
#
# This example is discussed in Chapter 12 of the book
# Object-Oriented Programming in Python
#
from ourStrip import ourStrip

class TextIndex:
  """Manage an index of words occurring in a work of text."""

  def __init__(self, contents, sourceLabel):
    """Construct a new index for the given document.

    contents         a single string representing the complete contents
    sourceLabel      a string which identifies the source of the contents
    """
    self._lines = contents.split('\n')
    self._label= sourceLabel

    # Now build a dictionary on the apparent words of the file.
    # Each word is mapped to an ordered list of line numbers at which that word occurs
    self._wordAt = {}
    for linenum in range(len(self._lines)):
      words = self._lines[linenum].split()
      for w in words:
        w = ourStrip(w)
        if w:                                     # not reduced to empty string
          if w not in self._wordAt:               # this is first occurrence of the word
            self._wordAt[w] = [ linenum ]
          elif self._wordAt[w][-1] != linenum:    # occurring on a new line for this word
            self._wordAt[w].append(linenum)

  def getLabel(self):
    """Return the string which serves as a layer for this document."""
    return self._label

  def getWords(self):
    """Return an unordered list of words appearing in this document."""
    return self._wordAt.keys()
    
  def getContext(self, word, maxOccur=10):
    """Return a string demonstrating occurrences of the word in context.

    Will show up to maxOccur distinct occurrences (default 10)
    """
    word = ourStrip(word)                         # clean query term
    output = []                                   # build list of lines to output
    if word in self._wordAt:
      occurrences = self._wordAt[word]            # list of line numbers
      for lineNum in occurrences[ : maxOccur]:    # limit the number of reported results
        startContext = max(lineNum - 1, 0)        # typically the previous line
        stopContext = min(lineNum + 2, len(self._lines))
        output.append('-' * 40)
        output.extend(self._lines[startContext : stopContext])
    return '\n'.join(output)


if __name__ == "__main__":
    sourcecode = file('TextIndex.py').read()
    fi = TextIndex(sourcecode,'TextIndex.py')     # index of our own source code
    print '============= ourStrip query ============='
    print fi.getContext( 'ourStrip' )             
    print '============= occurs query ============='
    print fi.getContext( 'occurs' )
