# Program: OurList.py
# Authors: Michael H. Goldwasser
#          David Letscher
#
# This example is discussed in Chapter 11 of the book
# Object-Oriented Programming in Python
#
class OurList:
  """Our own implementation of a python-style list."""

  def __init__(self):
    """
    Constructs a new (empty) list.
    """
    self._head = None
    self._rest = None

  def _isEmpty(self):
    """
    Private utility method.

    Returns True if self represents an empty list; False otherwise
    """
    return self._rest is None
  
  def __len__(self):
    """
    Returns the number of elements in the list.
    """
    if self._isEmpty():
      return 0
    else:
      return 1 + len(self._rest)                  # recurse

  def count(self, value):
    """
    Returns the number of occurrences of given value in the list.
    """
    if self._isEmpty():
      return 0
    else:
      subtotal = self._rest.count(value)          # recursion
      if self._head == value:                     # additional match
        subtotal += 1
      return subtotal

  def __contains__(self, value):
    """
    Returns True if the list contains the value; False otherwise
    """
    if self._isEmpty():
      return False
    elif self._head == value:
      return True
    else:
      return value in self._rest                  # recurse

  def index(self, value):
    """
    Returns the leftmost index at which the value appears in the list.

    Throws a ValueError if value is not in the list.
    """
    if self._isEmpty():
      raise ValueError('OurList.index(x): x not in list')
    elif self._head == value:
      return 0
    else:                                         # look in remainder of the list
      return 1 + self._rest.index(value)

  def __getitem__(self, i):
    """
    Return the value at index i of the list.

    Note:  this implementation does not accept negative indices.
    """
    if self._isEmpty():
      raise IndexError('list index out of range')
    elif i == 0:
      return self._head
    else:
      return self._rest[i-1]                      # recurse
              
  def __setitem__(self, i, value):
    """
    Equivalent to self[i] = value

    Note:  this implementation does not accept negative indices.
    """
    if self._isEmpty():
      raise IndexError('list assignment index out of range')
    elif i == 0:
      self._head = value
    else:
      self._rest[i-1] = value                     # recurse

  def __repr__(self):
    """
    Returns a string representation of the list.
    """
    if self._isEmpty():
      return '[]'
    elif self._rest._isEmpty():
      return '[' + repr(self._head) + ']'
    else:
      return '[' + repr(self._head) + ', ' + repr(self._rest)[1:]   # remove extra [

  def append(self, value):
    """
    Add the given value to the end of the list.
    """
    if self._isEmpty():
      self._head = value                          # we now have one element
      self._rest = OurList()                      # followed by new empty list
    else:
      self._rest.append(value)                    # pass it on

  def insert(self, index, value):
    """
    Inserts the given value into the list immediately before the
    item with the given index in the original configuration.
    """
    if self._isEmpty():                           # inserting at end; similar to append
      self._head = value
      self._rest = OurList()
    elif index == 0:                              # new element goes here!
      shift = OurList()
      shift._head = self._head
      shift._rest = self._rest
      self._head = value
      self._rest = shift
    else:                                         # insert recursively
      self._rest.insert(index-1, value)

  def remove(self, value):
    """
    Removes the first occurrence of the value.

    Throws a ValueError if value is not in the list.
    """
    if self._isEmpty():
      raise ValueError('OurList.remove(x): x not in list')
    elif self._head == value:
      self._head = self._rest._head
      self._rest = self._rest._rest
    else:
      self._rest.remove(value)


if __name__ == "__main__":
  fruits = OurList()
  print fruits
  print len(fruits)

  fruits.append('apple')
  print fruits
  print len(fruits)

  fruits.append('banana')
  print fruits
  print len(fruits)

  fruits.append('cantaloupe')
  print fruits
  print len(fruits)

  fruits.append('banana')
  print fruits
  print len(fruits)

  print fruits.index('apple')
  print fruits.index('banana')
  print fruits.index('cantaloupe')

  print fruits[0]
  print fruits[1]
  print fruits[2]
  print fruits[3]

  print fruits.count('apple')
  print fruits.count('banana')
  print fruits.count('cantaloupe')
  print fruits.count('grapes')
  
  fruits.remove('banana')
  print fruits

  fruits.insert(2,'kiwi')
  fruits.insert(0,'orange')
  fruits.insert(20,'squash')
  print fruits
  

  print "Hey..we even get for loops automatically, due to indexing."
  for f in fruits:
    print f
        
