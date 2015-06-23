# Program: easywebclient.py
# Authors: Michael H. Goldwasser
#          David Letscher
#
# This example is discussed in Chapter 16 of the book
# Object-Oriented Programming in Python
#
from urllib import urlopen

print 'Enter the web page you want to download.'
print 'Use the format http://domain.name/page/to/download'
url = raw_input()

content = urlopen(url).read()

outputFile = file('download.html','w')
outputFile.write(content)
outputFile.close()
