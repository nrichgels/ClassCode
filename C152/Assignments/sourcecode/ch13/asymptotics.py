# Program: asymptotics.py
# Authors: Michael H. Goldwasser
#          David Letscher
#
# This example is discussed in Chapter 13 of the book
# Object-Oriented Programming in Python
#
from time import time
testA = range(100000)
testB = range(1000000)
testC = range(10000000)
# small test
start = time()
testA.count(12345)
stop = time()
print 'testA time was', stop - start
# medium test
start = time()
testB.count(12345)
stop = time()
print 'testB time was', stop - start
# large test
start = time()
testC.count(12345)
stop = time()
print 'testC time was', stop - start
