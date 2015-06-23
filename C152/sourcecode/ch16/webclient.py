# Program: webclient.py
# Authors: Michael H. Goldwasser
#          David Letscher
#
# This example is discussed in Chapter 16 of the book
# Object-Oriented Programming in Python
#
from socket import socket

print 'Enter the web page you want to download.'
print 'Use the format http://domain.name/page/to/download'

url = raw_input()
server = url.split('/')[2]                   # e.g., domain.name
page = '/' + '/'.join(url.split('/')[3:])    # e.g., /page/to/download
connection = socket()
connection.connect( (server, 80) )
connection.send('GET %s HTTP/1.0\r\n\r\n' % page)

raw = connection.recv(1024)                  # read first block (header + some content)
sep = raw.index('\r\n\r\n')
header = raw[ :sep]
content = raw[sep+4: ]

length = 0                                   # just in case header doesn't say
for line in header.split('\n'):
  if line[:15] == 'Content-Length:':
    length = int(line[15:])

outputFile = file('download.html', 'w')
outputFile.write(content)                    # write out content we have seen thus far

contentRead = len(content)
while contentRead < length:                  # still more...
  content = connection.recv(1024)
  contentRead += len(content)
  outputFile.write(content)

outputFile.close()
connection.close()
