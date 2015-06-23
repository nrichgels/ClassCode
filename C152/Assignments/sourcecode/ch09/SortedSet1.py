# Program: SortedSet1.py
# Authors: Michael H. Goldwasser
#          David Letscher
#
# This example is discussed in Chapter 9 of the book
# Object-Oriented Programming in Python
#
class SortedSet(list):
  """
  Maintains an ordered set of objects (without duplicates).
  """

  def __init__(self, initial=None):
    """
    Default constructor creates an empty SortedSet.

    If initial sequence is given as parameter, creates initial
    configuration using those elements, with duplicates removed.
    """
    list.__init__(self)                    # calls the parent constructor
    if initial:
      self.extend(initial)

  def indexAfter(self, value):
    """
    Find first index of an element strictly larger than given value.

    If no element is greater than given value, this returns the
    length of the set.
    """
    walk = 0
    while walk < len(self) and value >= self[walk]:
      walk += 1
    return walk

  def insert(self, value):
    """
    Adds given element to the sorted set.

    If the value is already in the set, this has no effect.
    Otherwise, it is added in the proper location.

    value   element to be added to the set.
    """
    if value not in self:                  # avoid duplicates
      place = self.indexAfter(value)
      list.insert(self, place, value)      # the parent's method
          
  def append(self, object):
    """
    Identical to insert(object).
    """
    self.insert(object)

  def extend(self, other):
    """
    Extends the set by inserting elements from the other set
    """
    for element in other:
      self.insert(element)
      
  def __add__(self, other):
    """
    Returns new set which is union of this set and the other.
    """
    result = SortedSet(self)               # creates new copy of self
    result.extend(other)                   # add other elements to this copy
    return result

  def sort(self):
    """
    This has no effect, as set is already sorted.
    """
    pass
  
  def reverse(self):
    """
    SortedSets cannot be reversed.

    This always raises a RuntimeError.
    """
    raise RuntimeError('SortedSet cannot be reversed')

  def __setitem__(self, index, object):
    """
    Direct manipulation of elements of a SortedSet is disallowed.

    This always raises a RuntimeError.
    """
    raise RuntimeError('This syntax not supported by SortedSet')
    

if __name__ == '__main__':
  # unit tests
  s = SortedSet()
  s.insert(5)
  print 'after insert(5): ', s
  s.append(3)
  print 'after append(3): ', s
  s.insert(12)
  print 'after insert(12):', s
  s.insert(5)
  print 'after insert(5): ', s
  s.append(9)
  print 'after insert(9): ', s
  s.append(1)
  print 'after append(1): ', s
  s.append(20)
  print 'after append(20):', s
  s.append(1)
  print 'after append(1): ', s
  s.append(20)
  print 'after append(20):', s
  s.reverse()
  print 'after reverse(): ', s
  s.sort()
  print 'after sort():    ', s

  print 's[3] is', s[3]
  print 'Do not dare try s[3] = 7: ',
  try:
    s[3] = 7
  except RuntimeError:
    print 'RuntimeError was caught.'

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
