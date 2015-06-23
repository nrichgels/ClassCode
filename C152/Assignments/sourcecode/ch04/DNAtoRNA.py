# Program: DNAtoRNA.py
# Authors: Michael H. Goldwasser
#          David Letscher
#
# This example is discussed in Chapter 4 of the book
# Object-Oriented Programming in Python
#
dnaCodes = 'ACGT'
rnaCodes = 'UGCA'

dna = raw_input('Enter a DNA sequence: ')
rnaList = []
for base in dna:
  whichPair = dnaCodes.index(base)            # index into dnaCodes
  rnaLetter = rnaCodes[whichPair]             # corresponding index into rnaCodes
  rnaList.append(rnaLetter)
rna = ''.join(rnaList)                        # join on empty string
print 'Transcribed into RNA:', rna
