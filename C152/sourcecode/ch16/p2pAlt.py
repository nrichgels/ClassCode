# Program: p2pAlt.py
# Authors: Michael H. Goldwasser
#          David Letscher
#
# This example is discussed in Chapter 16 of the book
# Object-Oriented Programming in Python
#
from socket import socket, gethostname
from threading import Thread
from SocketServer import TCPServer, BaseRequestHandler

def manageConversation():
  IncomingThread().start()      # start secondary thread for monitoring incoming traffic
  
  print
  print 'Enter a message and hit return to send it.'
  print 'Type quit to stop the program.'
  print
  active = True                            # primary thread handles user's direct input
  while active:   
    message = raw_input()                                    # wait for more user input
    try:
      if message.rstrip().lower() == 'quit':
        peer.send('QUIT\n')
        active = False
      else:
        peer.send(message+'\n')
    except:
      print 'connection to peer was lost'
      active = False
  peer.close()

class IncomingThread(Thread):
  def run(self):
    connected = True
    while connected:      
      transmission = peer.recv(1024)
      if transmission:                                       # successful transmission
        lines = transmission.rstrip('\n').split('\n')
        i = 0
        while i < len(lines):
          if lines[i] == 'QUIT':                             # peer is leaving
            print name, 'has quit'
            connected = False                     
          elif lines[i].startswith('CONNECT '):
            name = lines[i][8:]
            print name, 'is connected'
          else:
            print name+':', lines[i]                         # an actual message
          i += 1
      else:
        print 'connection to peer was lost'
        connected = False                                    # socket failed
    peer.close()

class RegistrationHandler(BaseRequestHandler):
  def handle(self):
    global peer
    peer = self.request                                      # socket to peer
    peer.send('CONNECT %s\n' % username)                   # announce our identity
    manageConversation()
          
username = raw_input('What is your name: ').strip()
print 'Enter the Internet address (e.g., computer.domain.com)'
print 'of the computer to which you want to connect,'
print 'or hit return to wait for an incoming connection.'
address = raw_input()
if address:
  peer = socket()
  peer.connect((address, 9000))
  peer.send('CONNECT %s\n' % username)                       # announce our presence
  manageConversation()
else:    # Start server to await incoming connection
  localHost = gethostname()  # or you may hardwire your computer's hostname
  incomingServer = TCPServer( (localHost, 9000), RegistrationHandler)
  print 'Waiting for connection at', localHost
  incomingServer.handle_request()
