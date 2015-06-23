# Program: Account.py
# Authors: Michael H. Goldwasser
#          David Letscher
#
# This example is discussed in Chapter 10 of the book
# Object-Oriented Programming in Python
#
class Account:
  def __init__(self, balance=0.0):
    self._balance = balance

  def __eq__(self, other):
    return self._balance == other._balance

  def __str__(self):
    return 'current balance is '+str(self._balance)

  def getBalance(self):
    return self._balance

  def deposit(self, amount):
    self._balance += amount

  def withdraw(self, request):
    if request > self._balance:
      raise ValueError('Insufficient Funds')
    self._balance -= value
    return value
