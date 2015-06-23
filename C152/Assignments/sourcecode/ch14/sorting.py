# Program: sorting.py
# Authors: Michael H. Goldwasser
#          David Letscher
#
# This example is discussed in Chapter 14 of the book
# Object-Oriented Programming in Python
#
def selectionSort(data):
  hole = 0                              # next index to fill
  while hole < len(data) -1:            # last item automatically ends in proper place
    small = hole
    walk = hole + 1
    while walk < len(data):
      if data[walk] < data[small]:
        small = walk                    # new minimum found
      walk += 1
    data[hole], data[small] = data[small], data[hole]
    hole += 1

def insertionSort(data):
  next = 1                         # index of next element to insert (first is trivially okay)
  while next < len(data):
    value = data[next]             # will insert this value in proper place
    hole = next
    while hole > 0 and data[hole-1] > value:
      data[hole] = data[hole-1]    # slide data[hole-1] forward
      hole -= 1                    # and the implicit hole one step backward
    data[hole] = value
    next += 1

def mergeSort(data):
  # create new temporary list for extra storage space
  _recursiveMergeSort(data, 0, len(data), [None] * len(data))

def _recursiveMergeSort(data, start, stop, tempList):
  if start < stop - 1:                               # more than one element to sort
    mid = (start + stop) // 2
    _recursiveMergeSort(data, start, mid, tempList)
    _recursiveMergeSort(data, mid, stop, tempList)
    _merge(data, start, mid, stop, tempList)

def _merge(data, start, mid, stop, temp):
  """Merge data[start:mid] and data[mid:stop] into data[start:stop].
  
  data[start:mid] and data[mid:stop] are presumed to be sorted.
  temp is presumed to be a list with same length as data (serves as a buffer)
  """
  # copy data into temporary buffer
  i = start
  while i < stop:
    temp[i] = data[i]
    i += 1

  mergedMark = start         # index into data[start:stop]
  leftMark = start           # index into temp[start:mid]
  rightMark = mid            # index into temp[mid:stop]
  
  # merge values back into original data list
  while mergedMark < stop:
    if leftMark < mid and (rightMark == stop or temp[leftMark] < temp[rightMark]):
      data[mergedMark] = temp[leftMark]
      leftMark += 1
    else:
      data[mergedMark] = temp[rightMark]
      rightMark += 1
    mergedMark += 1




from random import shuffle
def quicksort(data):
  shuffle(data)                             # in hope of getting good partitioning
  _recursiveQuicksort(data, 0, len(data))

def _recursiveQuicksort(data, start, stop):
  if start < stop-1:                        # more than one element to sort
    pivot = _quickPartition(data, start, stop)
    _recursiveQuicksort(data, start, pivot)
    _recursiveQuicksort(data, pivot+1, stop)

def _quickPartition(data, start, stop):
  """Rearrange data[start:stop] so that values are partitioned around a pivot value.

  Return index at which pivot element is eventually placed. At the conclusion,
    data[start:pivot] will have values less than or equal to pivot's
    data[pivot] is the pivot itself
    data[pivot+1:stop] will have values strictly greater than pivot's
  """
  # Algorithm proceeds with the following invariant,
  #   data[start:big] entries must be less than or equal to pivot value
  #   data[big:unknown] entries must be greater than pivot value
  #   data[unknown:stop] entries can be anything

  pivotVal = data[stop-1]          # rightmost element of range
  big = unknown = start            # initially, everything is unknown
  while unknown < stop:
    if data[unknown] <= pivotVal:
      data[big], data[unknown] = data[unknown], data[big]
      big += 1
    unknown += 1                   # in either case, one less unknown element
  return big - 1                   # index where pivot has just been placed

def _runTrials(N, trials, algorithm):
  okay = True
  cumTime = 0.0
  for t in range(trials):
    values = range(N // 2) * 2     # so that duplicates exist
    answer = sorted(values)
    random.shuffle(values)
    original = list(values)
    start = time.time()
    algorithm(values)
    stop = time.time()
    cumTime += (stop - start)
    if values != answer:
      okay = False
      print 'ERROR: incorrectly sorted.'
      print 'original order:',original
  return okay, cumTime/trials
    

if __name__ == '__main__':
    import random
    import time
    import sys

    # catalog of available algorithms
    algorithms = [
      ('Insertion Sort', insertionSort),
      ('Selection Sort', selectionSort),
      ('Merge Sort', mergeSort),
      ('Quicksort', quicksort),
      ('Python built-in', list.sort)
      ]

    N = None
    if len(sys.argv) > 1:
      try:
        N = int(sys.argv[1])
      except ValueError:
        pass
    while N is None:
      try:
        N = int(raw_input('Enter number N of elements to sort: '))
      except ValueError:
        print 'Invalid response'

    trials = None
    if len(sys.argv) > 2:
      try:
        trials = int(sys.argv[2])
      except ValueError:
        pass
    while trials is None:
      try:
        trials = int(raw_input('Enter number of trials: '))
      except ValueError:
        print 'Invalid response'

    alg = None
    if len(sys.argv) > 3:
      try:
        alg = int(sys.argv[3])
      except ValueError:
        pass
    while alg is None or not 0 <= alg < len(algorithms):
      try:
        print 'Algorithm choices'
        for i in range(len(algorithms)):
          print '  %d) %s' % (i,algorithms[i][0])
        alg = int(raw_input('Choose algorithm number: '))
      except ValueError:
        print 'Invalid response'

    success,avgTime = _runTrials(N,trials,algorithms[alg][1])
    if success:
        print 'Successfully completed %d trials with average time of %.4f seconds.' % (trials,avgTime)
    
    
