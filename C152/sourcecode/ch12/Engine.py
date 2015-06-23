# Program: Engine.py
# Authors: Michael H. Goldwasser
#          David Letscher
#
# This example is discussed in Chapter 12 of the book
# Object-Oriented Programming in Python
#
from ourStrip import ourStrip
from TextIndex import TextIndex

class Engine:
  """Support word searches within a collection of text documents."""

  def __init__(self):
    """Create a new search engine.

    By default, the initial corpus is empty.
    """
    self._corpus = {}         # maps each document label to the associated index
    self._hasWord = {}        # maps each word to a set of labels

  def addDocument(self, contents, sourceLabel):
    """Add the given document to the corpus (if not already present).

    contents          a single string representing the complete contents
    sourceLabel       a string which identifies the source of the contents
    """
    if sourceLabel not in self._corpus:
      newIndex = TextIndex(contents, sourceLabel)
      self._corpus[sourceLabel] = newIndex
      for word in newIndex.getWords():
        if word in self._hasWord:
          self._hasWord[word].add(sourceLabel)
        else:
          self._hasWord[word] = set([sourceLabel])       # new set with one entry

  def lookup(self, term):
    """Return a set of labels for those documents containing the search term."""
    term = ourStrip(term)
    if term in self._hasWord:
      return set(self._hasWord[term])                    # intentionally return a copy
    else:
      return set()

  def getContext(term, docLabel, maxOccur=10):
    """Search a single document for a word, returning a string demonstrating context.
    
    docLabel        the name of the underlying document to search
    maxOccur        maximum number of distinct occurrences to display (default 10)
    """
    return self._corpus[docLabel].getContext(term, maxOccur)

  def makeReport(self, term, maxDocuments=10, maxContext=3):
    """Produce a formatted report about the occurrences of a term within the corpus.

    Return a string summarizing the results.  This will include names of all documents
    containing the term as well as a demonstration of the context.
    
    term             the word of interest
    maxDocuments  the maximum number of files to report (default 10)
    maxContext       maximum number of occurrences to show per document (default 3)
    """
    output = []                                          # lines of output
    sources = self.lookup(term)
    num = min(len(sources), maxDocuments)
    labels = list(sources)[ :num]                        # choose first so many labels
    for docLabel in labels:
      output.append('Document: ' + docLabel)
      context = self._corpus[docLabel].getContext(term, maxContext)
      output.append(context)
      output.append('=' * 40)
    return '\n'.join(output)

if __name__ == '__main__':
  wizard = Engine()

  # Phase 1:  load original files
  print 'Enter filenames to catalog, one per line.'
  print '(enter a blank line when done)'
  filename = raw_input('File: ')
  while filename:
    try:
      source = file(filename)
      wizard.addDocument(source.read(), filename)
    except IOError:
      print 'Sorry. Unable to open file', filename
    filename = raw_input('File: ')

  # Phase 2:  let user enter queries
  print
  print 'Ready to search.  Enter search terms, one per line.'
  print 'Enter a blank line to end.'
  term = raw_input('Term: ')
  while term:
    documents = wizard.lookup(term)
    if documents:   # found the term
      print 'Containing files are:'
      print '\n'.join(documents)

      report = wizard.makeReport(term)
      print
      print 'Sample report:'
      print report
    else:
      print 'Term not found'
    term = raw_input('Term: ')
