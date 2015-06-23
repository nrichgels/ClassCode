# Program: SortedSet2.py
# Authors: Michael H. Goldwasser
#          David Letscher
#
# This example is discussed in Chapter 9 of the book
# Object-Oriented Programming in Python
#
class SortedSet:
  """Maintains an ordered set of objects (without duplicates)."""

  def __init__(self, initial=None):
    """Default constructor creates an empty SortedSet.

    If initial sequence is given as parameter, creates initial
    configuration using those elements, with duplicates removed.
    """
    self._items = list()
    if initial:
      self.extend(initial)          # extend the set (not the list)

  def indexAfter(self, value):
    """Find first index of an element strictly larger than given value.

    If no element is greater than given value, this returns the length of the set.
    """
    walk = 0
    while walk < len(self._items) and value >= self._items[walk]:
      walk += 1
    return walk

  def insert(self, value):
    """Adds given element to the sorted set.

    If the value is already in the set, this has no effect.
    Otherwise, it is added in the proper location.

    value   element to be added to the set.
    """
    if value not in self._items:
      place = self.indexAfter(value)
      self._items.insert(place, value)

  def extend(self, other):
    """Extends the set by inserting elements from the other set."""
    for element in other:
      self.insert(element)

  def __add__(self, other):
    """Returns new set which is union of this set and the other."""
    result = SortedSet(self)        # creates new copy of self
    result.extend(other)            # add other elements to this copy
    return result

  def index(self, value):
    """Returns index of value.

    Raises a ValueError if value not found.
    """
    return self._items.index(value)

  def remove(self, element):
    """Remove an element from the sorted set."""
    self._items.remove(element)

  def pop(self, index=None):
    """Pop element at given index (last by default)."""
    return self._items.pop(index)

  def __contains__(self, element):
    """Determine if the element is in the sorted set."""
    return element in self._items

  def __getitem__(self, index):
    """Get the element of the sorted set at the given index."""
    return self._items[index]
      
  def __len__(self):
    """Count the number of elements in the sorted set."""
    return len(self._items)

  def __eq__(self, other):
    """Determine if two sets are equivalent."""
    return self._items == other._items

  def __lt__(self, other):                  # lexicographic comparison
    return self._items < other._items

  def __str__(self):
    """Return a string representation of the sorted set."""
    return str(self._items)


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

  t = SortedSet([5, 1, 20, 17, 10, 5])
  print 't is', t

  print 's + t is ', s+t
  print 'though s is still ', s
  print 'and t is still    ', t

  s.extend(t)
  print 'after s.extend(t), s is ', s
  
  print 's.index(1) is', s.index(1)
  print 's.index(17) is', s.index(17)
  print 's.index(20) is', s.index(20)
  try:
    print 's.index(4) is a problem...', s.index(4)
  except ValueError:
    print 'ValueError was caught.'
  try:
    print 'SortedSet().index(4) is a problem...', SortedSet().index(4)
  except ValueError:
    print 'ValueError was caught.'


  print 'for loops are available (e.g., to print t)'
  for item in t:
    print item
