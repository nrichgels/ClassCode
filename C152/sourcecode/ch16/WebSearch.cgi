#!/usr/bin/python
#
# Program: WebSearch.cgi
# Authors: Michael H. Goldwasser
#          David Letscher
#
# This example is discussed in Chapter 16 of the book
# Object-Oriented Programming in Python
#
from socket import socket
from cgi import FieldStorage

# Display HTML header info
print 'Content-type: text/html\n\n'
print '<html>'
print '<head><title>Search results</title></head>'
print '<body>'
print '<h2>Search results</h2><hr>'

try:
  form = FieldStorage()
  searchTerm = form['term'].value

  connection = socket()
  connection.connect( ('localhost', 9000) )  # will need to adjust server name
  connection.send(searchTerm)
  response = connection.recv(1024)

  totalLength = int(response.split('\n')[0][8:])
  if totalLength > 0:
    result = '\n'.join(response.split('\n')[1:])
    while len(result) < totalLength:
      transmission = connection.recv(1024)
      result += transmission

    for line in result.split('\n'):
      if line.startswith('Document: '):
        filename = line[10:]
        print 'Document: <a href="%s">%s</a><br>' % (filename,filename)
      elif line == 40 * '=':
        print '<hr>'             # horizontal rule
      else:
        print line + '<br>'
  else:
    print 'No matches found.'
except:
  print 'Sorry.  Our server is not responding.'

# Display HTML footer info
print '</body></html>'
