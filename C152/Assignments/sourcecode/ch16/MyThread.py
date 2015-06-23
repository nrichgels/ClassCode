# Program: MyThread.py
# Authors: Michael H. Goldwasser
#          David Letscher
#
# This example is discussed in Chapter 16 of the book
# Object-Oriented Programming in Python
#
from threading import Thread
from time import sleep

class MyThread(Thread):
  def run(self):
    print 'Second thread begins.'
    sleep(5)
    print 'Second thread is done.'

secondThread = MyThread()
secondThread.start()
print 'The program is done.'
