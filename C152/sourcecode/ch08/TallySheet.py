# Program: TallySheet.py
# Authors: Michael H. Goldwasser
#          David Letscher
#
# This example is discussed in Chapter 8 of the book
# Object-Oriented Programming in Python
#
class TallySheet:
  """Manage tallies for a collection of values.

  Values can either be from a consecutive range of integers, or a
  consecutive sequence of characters from the alphabet.
  """
  def __init__(self, minVal, maxVal):
    """Create an initially empty tally sheet.

    minVal    the minimum acceptable value for later insertion
    maxVal    the minimum acceptable value for later insertion
    """
    self._minV = minVal
    self._maxV = maxVal
    maxIndex = self._toIndex(maxVal)
    self._tallies = [0] * (maxIndex + 1)   # a list of counters, each initially zero

  def increment(self, val):
    """Increment the tally for the respective value.
    
    raise a TypeError if the given value is not of the proper type
    raise a ValueError if the given value is not within proper range
    """
    ind = self._toIndex(val)
    if not 0 <= ind < len(self._tallies):
      raise ValueError('parameter '+str(val)+' out of range')
    self._tallies[ind] += 1

  def getCount(self, val):
    """Return the total number of current tallies for the given value.

    raise a TypeError if the given value is not of the proper type
    raise a ValueError if the given value is not within proper range
    """
    ind = self._toIndex(val)
    if not 0 <= ind < len(self._tallies):
      raise ValueError('parameter '+str(val)+' out of range')
    return self._tallies[ind]

  def getTotalCount(self):
    """Return the total number of current tallies."""
    return sum(self._tallies)

  def _toIndex(self, val):
    """Convert from a native value to a legitimate index.

    Return the resulting index (such that _minV is mapped to 0)
    """
    try:
      if isinstance(self._minV, str):
        i = ord(val) - ord(self._minV)
      else:
        i = int( val - self._minV )
    except TypeError:
      raise TypeError('parameter '+str(val)+' of incorrect type')
    return i

  def writeTable(self, outfile):
    """Write a comprehensive table of results.

    Report each value, the count for that value, and the percentage usage.

    outfile   an already open file with write access.
    """
    outfile.write('Value  Count Percent \n----- ------ -------\n')
    total = max(self.getTotalCount(), 1)  # avoid division by zero
    for ind in range(len(self._tallies)):
      label = self._makeLabel(ind)
      count = self._tallies[ind]
      pct = 100.0 * count / total
      outfile.write('%s %6d %6.2f%%\n' % (label, count, pct))

  def _makeLabel(self, ind):
    """Convert index to a string in native range."""
    if isinstance(self._minV, int):
      return '%5d' % (ind + self._minV)
    else:
      return '  %s  ' % chr(ind + ord(self._minV))
