# Program: Dictionary.py
# Authors: Michael H. Goldwasser
#          David Letscher
#
# This example is discussed in Chapter 13 of the book
# Object-Oriented Programming in Python
#
class DictWithLists:
  def __init__(self):
    self._keys = []
    self._values = []

  def _getIndex(self, k):                       # Returns len(self) if key not found
    i = 0
    while i < len(self._keys) and self._keys[i] != k:
      i += 1
    return i
        
  def __len__(self):
    return len(self._keys)

  def __contains__(self, k):
    return k in self._keys

  def __getitem__(self, k):
    ind = self._getIndex(k)
    if ind == len(self):
      raise KeyError(repr(k))                   # k not found
    return self._values[ind]

  def __setitem__(self, k, v):
    ind = self._getIndex(k)
    if ind < len(self):                         # reassign new value for existing key
      self._values[ind] = v
    else:                                       # new key/value pair
      self._keys.append(k)
      self._values.append(v)

  def clear(self):
    self._keys = []
    self._values = []

  def pop(self, k):
    ind = self._getIndex(k)
    if ind == len(self):
      raise KeyError(repr(k))                   # k not found
    self._keys.pop(ind)
    return self._values.pop(ind)

  def popitem(self):
    if len(self) == 0:
      raise KeyError('popitem(): dictionary is empty')
    return (self._keys.pop(), self._values.pop())

  def keys(self):
    return list(self._keys)                     # copy of internal list

  def values(self):
    return list(self._values)                   # copy of internal list

  def items(self):
    result = []
    for i in range(len(self)):
      result.append( (self._keys[i], self._values[i]) )
    return result

  def __repr__(self):
    mapping = []
    for k,v in self.items():
      mapping.append( repr(k) + ': ' + repr(v) )
    return '{' + ', '.join(mapping) + '}'

class DictWithHashing:
  def __init__(self):
    self._numItems = 0                          # no elements initially
    self._table = [None] * 7                    # quick footprint;
    for h in range(len(self._table)):           # real buckets created by loop
      self._table[h] = DictWithLists()          # bootstrap with simpler version

  def _getBucket(self, k):
    return self._table[ hash(k) % len(self._table) ]
  
  def __len__(self):
    return self._numItems

  def __contains__(self, k):
    bucket = self._getBucket(k)
    return k in bucket                          # is key actually in the bucket?

  def __getitem__(self, k):
    bucket = self._getBucket(k)
    if k not in bucket:                         # wasn't there
      raise KeyError(repr(k))
    return bucket[k]                            # retrieve associated value from bucket

  def __setitem__(self, k, v):
    bucket = self._getBucket(k)
    if k not in bucket:
      self._numItems +=1                        # k is a new key
    bucket[k] = v                               # assign/reassign value
    if self._numItems > 2.0*len(self._table):   # load factor exceed
      self._expandTable()

  def _expandTable(self):
    oldItems = self.items()                     # save list of existing contents!!!

    # re-create bigger table of empty buckets
    newSize = 2 * len(self._table) + 1          # will be pow(2,j)-1 for some j
    self._numItems = 0
    self._table = [None] * newSize              # bigger footprint
    for h in range(len(self._table)):
      self._table[h] = DictWithLists()          # empty bucket

    # reinsert contents from old to new
    for k,v in oldItems:
      self[k] = v

  def clear(self):
    for bucket in self._table:
      bucket.clear()
    self._numItems = 0

  def pop(self, k):
    bucket = self._getBucket(k)
    if k not in bucket:
      raise KeyError(repr(k))                   # wasn't there
    self._numItems -= 1
    return bucket.pop(k)

  def popitem(self):
    if self._numItems == 0:
      raise KeyError('popitem(): dictionary is empty')
    h = 0                                       # must look for a nonempty bucket
    while len(self._table[h]) == 0:
      h += 1
    self._numItems -= 1
    return self._table[h].popitem()

  def keys(self):
    allkeys = []                                # must gather keys from all buckets
    for bucket in self._table:
      allkeys.extend(bucket.keys())
    return allkeys

  def values(self):
    allvalues = []                              # must gather values from all buckets
    for bucket in self._table:
      allvalues.extend(bucket.values())
    return allvalues

  def items(self):
    allitems = []                               # must gather items from all buckets
    for bucket in self._table:
      allitems.extend(bucket.items())
    return allitems

  def __repr__(self):
    mapping = []
    for k,v in self.items():
      mapping.append( repr(k) + ': ' + repr(v) )
    return '{' + ', '.join(mapping) + '}'

if __name__ == '__main__':
  import time
  import random

  # prepare large-scale test
  largeList = []
  try:
    scrabble = file('scrabble.txt')
    for word in scrabble:
      largeList.append(word.rstrip())
      largeList.append(word.rstrip()[::-1])     # hopefully a few collisions?
    random.shuffle(largeList)
    scrabble.close()
  except IOError:
    largeList = []
      
  oldD = d = {}
  largeSize = -1
  for impl in (dict, DictWithLists, DictWithHashing):
    print '---------------------------------------------\nStarting test on class',impl

    if len(d) == largeSize:
      oldD = d
    d = impl()

    if len(d) != 0:
      print 'Error with len on empty dictionary.', impl

    d['A'] = 'U'
    d['C'] = 'G'
    d['G'] = 'C'
    d['T'] = 'A'

    if len(d) != 4:
      print 'ERROR: with len on nonempty dictionary.', impl

    print 'initial dictionary constructed.'
    print 'keys:',d.keys()
    print 'values:',d.values()
    print 'items:',d.items()
    print 'representaton:',d

    if 'A' not in d or 'C' not in d or 'G' not in d or 'T' not in d:
      print 'ERROR: Containment checks failed.', impl
      
    if d['A'] != 'U':
      print "ERROR: retrieving d['A'].", impl
    if d['C'] != 'G':
      print"ERROR: retrieving d['A'].", impl
    if d['G'] != 'C':
      print "ERROR: retrieving d['A'].", impl
    if d['T'] != 'A':
      print "ERROR: retrieving d['A'].", impl

    d['A'] = 65
    if d['A'] != 65:
      print "ERROR: retrieving remapped value of 'A'.", impl
      
    d['C'] = 67
    if d['C'] != 67:
      print "ERROR: retrieving remapped value of 'C'.", impl

    d['B'] = 66
    if 'B' not in d or d['B'] != 66:
      print "ERROR: retrieving newly added value of 'B'.", impl

    d.pop('G')
    d.pop('T')
    
    if 'G' in d or 'T' in d:
      print 'ERROR: Containment checks after pop failed.', impl

    print 'second version of dictionary.'
    print 'keys:',d.keys()
    print 'values:',d.values()
    print 'items:',d.items()
    print 'representaton:',d

    # medium scale trial
    d.clear()
    try:
      source = file('Dictionary.py')
      starttime = time.time()
      for line in source:
        d[line] = len(line)
      stoptime = time.time()
      print 'medium scale test processed %d unique lines in %f seconds' % (len(d),stoptime-starttime)
      source.close()
    except IOError:
      pass
    
    # large-scale trial
    if impl != DictWithLists:
      d.clear()
      starttime = time.time()
      for word in largeList:
        d[word] = len(word)
      stoptime = time.time()
      print 'large-scale test processed %d unique words in %f seconds' % (len(d),stoptime-starttime)
      largeSize = len(d)

      if oldD:
        print 'starting large-scale pop test.'
        while len(oldD) > 1:
        #while len(d) > 1 and len(d) == len(oldD):    # too slow to repeatedly recompute length for binary tree
          k,v = oldD.popitem()
          d.pop(k)
        if len(d) != len(oldD):
          print 'ERROR: sizes no longer match',len(d), len(oldD)
        else:
          k1,v1 = oldD.popitem()
          k2,v2 = d.popitem()
          if (k1,v1) != (k2,v2):
            print 'ERROR: pop phase of large-scale test led to mismatch'
            print '    '+repr(k1)+':'+repr(v1)
            print '    '+repr(k2)+':'+repr(v2)
          else:
            print 'large-scale pop test succeeded.'
    else:
      print '(intentionally bypassing large-scale test for %s)' % (str(impl))
