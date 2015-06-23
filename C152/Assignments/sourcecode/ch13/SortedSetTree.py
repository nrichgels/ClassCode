# Program: SortedSetTree.py
# Authors: Michael H. Goldwasser
#          David Letscher
#
# This example is discussed in Chapter 13 of the book
# Object-Oriented Programming in Python
#
class SortedSet:
  """Maintains an ordered set of objects (without duplicates)."""

  def __init__(self):
    """Default constructor creates an empty SortedSet."""
    self._element = None
    self._left = None
    self._right = None
    self._size = 0

  def __len__(self):
    """Count the number of elements in the sorted set."""
    return self._size

  def _tracePath(self, value):
    """Returns a list representing the path traversed, from top to bottom, when searching for value"""
    if len(self) == 0 or value == self._element:
      return [ self ]
    elif value < self._element:
      return [ self ] + self._left._tracePath(value)
    else:
      return [ self ] + self._right._tracePath(value)

  def __contains__(self, value):
    """Determine if the element is in the sorted set."""
    path = _tracePath(value)
    return  path[-1]._size > 0    # check the end of the path

  def insert(self, value):
    """Adds given element to the sorted set.

    value   element to be added to the set.
    """
    path = self._tracePath(value)
    endOfPath = path[-1]
    if endOfPath._size == 0:      # this is a new element
      for location in path:       # this subtree and all those above
        location._size += 1       # must have size increase by one element
      endOfPath._element = value
      endOfPath._left = SortedSet()
      endOfPath._right = SortedSet()

  def index(self, value):
    """Return index of value.

    Raises a ValueError if value not found.
    """
    if len(self) == 0:
      raise ValueError('SortedSet.index(x): x not in list')
    elif value == self._element:
      return len(self._left)
    elif value < self._element:
      return self._left.index(value)
    else:
      return 1 + len(self._left) + self._right.index(value)

  def __getitem__(self, index):
    """Get the element of the sorted set at the given index."""
    index = self._cleanupIndex(index)   # handles negative indices properly
    if index == len(self._left):
      return self._element
    elif index < len(self._left):
      return self._left[index]
    else:  # look in right subtree, but discount the left elements and root when counting
      return self._right[index - (1 + len(self._left))]

  def remove(self, value):
    """Remove an element from the sorted set."""
    path = self._tracePath(value)
    endOfPath = path[-1]
    if endOfPath._size > 0:       # element was found
      for location in path:
        location._size -= 1       # these trees will each decrease by one element
      # Now we must get rid of it
      if len(endOfPath._left) == 0:
        endOfPath._promoteChild(endOfPath._right)
      elif len(endOfPath._right) == 0:
        endOfpath._promoteChild(endOfPath._left)
      else:                       # substitute maximum value removed from left subtree
        endOfpath._element = endOfpath._left.pop() 

  def pop(self, index=None):
    """Pop element at given index (last by default)."""
    if index is None:
      index = len(self) - 1
    value = self[index]
    self.remove(value)            # reuse existing behavior, for convenience
    return value

  def _cleanupIndex(self, index):
    """Interpret index using standard Python conventions.

    Negative indices are converted to positive and illegal indices cause IndexError.
    """
    if index < 0:
      index += len(self)          # support Python's notion of negative index
    if not 0 <= index < len(self):
      raise IndexError('SortedSet index out of range')
    return index
    
  def _promoteChild(self, child):
    self._element = child._element
    self._left = child._left
    self._right = child._right

  def __str__(self):
    """Return a string representation of the sorted set."""
    answer = '['
    if self._size > 0:
      if len(self._left) > 0:
        answer += str(self._left)[1:-1] + ', '
      answer += str(self._element)
      if len(self._right) > 0:
        answer += ', ' + str(self._right)[1:-1]
    answer += ']'
    return answer

  def _dump(self):
    """Outputs a preorder traversal of the tree"""
    print 'Element is: %s\nSize is: %d\n' % (self._element, self._size)
    if len(self) > 0:
      self._left._dump()
      self._right._dump()

if __name__ == '__main__':
  # unit tests
  s = SortedSet()
  s.insert(5)
  print 'after insert(5): ', s
  s.insert(3)
  print 'after insert(3): ', s
  s.insert(12)
  print 'after insert(12):', s
  s.insert(5)
  print 'after insert(5): ', s
  s.insert(9)
  print 'after insert(9): ', s
  s.insert(1)
  print 'after insert(1): ', s
  s.insert(20)
  print 'after insert(20):', s
  s.insert(1)
  print 'after insert(1): ', s
  s.insert(20)
  print 'after insert(20):', s

  print 's[3] is', s[3]
  print 'Do not dare try s[3] = 7: ',
  try:
    s[3] = 7
  except RuntimeError:
    print 'RuntimeError was caught (as expected).'

  s.pop(3)
  print 'after pop(3):    ', s
  s.remove(12)
  print 'after remove(12):', s

  t = SortedSet()
  t.insert(5)
  t.insert(1)
  t.insert(20)
  t.insert(17)
  t.insert(10)
  t.insert(5)
  print 't is', t

  try:
    print 's.index(4) is a problem...', s.index(4)
  except ValueError:
    print 'ValueError was caught (as expected).'
  try:
    print 'SortedSet().index(4) is a problem...', SortedSet().index(4)
  except ValueError:
    print 'ValueError was caught (as expected).'


  print 'for loops are available (e.g., to print t)'
  for item in t:
    print item

  demo = SortedSet()
  for c in 'PYTHONRULES':
    demo.insert(c)

  echo = []
  for c in demo:
    echo.append(c)
  if echo != sorted('PYTHONRULES'):
    print 'UNEXPECTED ERROR after insertion and iteration'

  indices = []
  for c in demo:
    indices.append(demo.index(c))
  if indices != range(len(demo)):
    print 'UNEXPECTED ERROR involving computation of indices'
