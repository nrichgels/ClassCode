# Program: DNAcount.py
# Authors: Michael H. Goldwasser
#          David Letscher
#
# This example is discussed in Chapter 4 of the book
# Object-Oriented Programming in Python
#
numA = numC = numG = numT = 0
for base in dna:
  if base == 'A':
    numA += 1
  elif base == 'C':
    numC += 1
  elif base == 'G':
    numG += 1
  else:                  # presumably a T
    numT += 1
