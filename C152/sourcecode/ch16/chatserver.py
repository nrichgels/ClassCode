# Program: chatserver.py
# Authors: Michael H. Goldwasser
#          David Letscher
#
# This example is discussed in Chapter 16 of the book
# Object-Oriented Programming in Python
#
from SocketServer import ThreadingTCPServer, BaseRequestHandler

_socketLookup = dict()                                 # intentionally shared as global

def _broadcast(announcement):
  for connection in _socketLookup.values():            # uses the global dictionary
    connection.send(announcement)

class ChatHandler(BaseRequestHandler):
  def handle(self):
    username = 'Unknown'
    active = True
    while active:
      transmission = self.request.recv(1024)           # wait for something to happen
      if transmission:
        command = transmission.split()[0]
        data = transmission[1+len(command): ]          # the rest

        if command == 'ADD':
          username = data.strip()
          _socketLookup[username] = self.request
          _broadcast('NEW %s\n' % username)
        elif command == 'MESSAGE':
          _broadcast('MESSAGE %s\n%s\n' % (username,data) )
        elif command == 'PRIVATE':
          rcpt = data.split('\n')[0]
          if rcpt in _socketLookup:
            content = data.split('\n')[1]
            _socketLookup[rcpt].send('PRIVATE %s\n%s\n'%(username,content) )
        elif command == 'QUIT':
          active = False
          self.request.send('GOODBYE\n')                  # acknowledge
      else:
          active = False                                  # socket failed
    
    self.request.close()
    _socketLookup.pop(username)
    _broadcast('LEFT %s\n' % username)                    # inform others

myServer = ThreadingTCPServer( ('localhost', 9000), ChatHandler)
myServer.serve_forever()
