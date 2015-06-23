#!/usr/bin/python
#
# Program: processForm.cgi
# Authors: Michael H. Goldwasser
#          David Letscher
#
# This example is discussed in Chapter 16 of the book
# Object-Oriented Programming in Python
#
from cgi import FieldStorage

form = FieldStorage()

print 'Content-type: text/html\n'   # includes extra blank line
print '<html><head>'
print '<title>', form['firstName'].value + "'s Page</title></head>"
print '<body><h1>'
print 'Hello', form['firstName'].value, form['lastName'].value
print '</h1></body></html>'
