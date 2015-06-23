# Program: gettime.py
# Authors: Michael H. Goldwasser
#          David Letscher
#
# This example is discussed in Chapter 16 of the book
# Object-Oriented Programming in Python
#
from socket import socket

connection = socket()
server = 'time.nist.gov'
connection.connect( (server, 13) )

fields = connection.recv(1024).split()
date = fields[1]
time = fields[2]

print 'Date (YY-MM-DD) is %s, time is %s (UTC)' % (date,time)
