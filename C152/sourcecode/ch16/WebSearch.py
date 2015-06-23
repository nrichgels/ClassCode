# Program: WebSearch.py
# Authors: Michael H. Goldwasser
#          David Letscher
#
# This example is discussed in Chapter 16 of the book
# Object-Oriented Programming in Python
#
from socket import socket

address = raw_input('Enter hostname for the search engine: ')
connection = socket()
connection.connect( (address, 9000) )

searchTerm = raw_input('Enter a term to search for: ')
connection.send(searchTerm)
response = connection.recv(1024)

totalLength = int(response.split('\n')[0][8:])
if totalLength > 0:
  result = '\n'.join(response.split('\n')[1:])
  while len(result) < totalLength:
    transmission = connection.recv(1024)
    result += transmission
  print result
else:
  print 'No matches found.'
