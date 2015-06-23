# Program: echoserver.py
# Authors: Michael H. Goldwasser
#          David Letscher
#
# This example is discussed in Chapter 16 of the book
# Object-Oriented Programming in Python
#
from SocketServer import TCPServer, BaseRequestHandler

class EchoHandler(BaseRequestHandler):
  def handle(self):
    message = self.request.recv(1024)
    self.request.send(message)

# may need to customize localhost and port for your machine
echoServer = TCPServer( ('localhost', 9000), EchoHandler)
echoServer.serve_forever()
