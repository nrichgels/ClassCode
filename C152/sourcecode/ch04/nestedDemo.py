# Program: nestedDemo.py
# Authors: Michael H. Goldwasser
#          David Letscher
#
# This example is discussed in Chapter 4 of the book
# Object-Oriented Programming in Python
#
for chapter in ('1', '2'):
  print 'Chapter ' + chapter
  for section in ('a', 'b', 'c'):
    print '  Section ' + chapter + section
print 'Appendix'
