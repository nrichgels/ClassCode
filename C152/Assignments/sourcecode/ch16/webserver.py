# Program: webserver.py
# Authors: Michael H. Goldwasser
#          David Letscher
#
# This example is discussed in Chapter 16 of the book
# Object-Oriented Programming in Python
#
from SocketServer import TCPServer, BaseRequestHandler

class WebHandler(BaseRequestHandler):
  def handle(self):
    command = self.request.recv(1024)
    if command[:3] == 'GET':
      pagename = command.split()[1][1:]           # remove leading '/' for filename
      try:
        requestedFile = file(pagename, 'r')
        content = requestedFile.read()
        requestedFile.close()
        header = 'HTTP/1.0 200 OK\r\n'
        header += 'Content-Length: %d\r\n\r\n' % len(content)
        self.request.send(header)
        self.request.send(content)
      except IOError:                             # could not open the file
        self.request.send('HTTP/1.0 404 Not Found\r\n\r\n')

webServer = TCPServer( ('localhost', 8080), WebHandler)
webServer.serve_forever()
