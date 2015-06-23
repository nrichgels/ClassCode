# Program: chatclient.py
# Authors: Michael H. Goldwasser
#          David Letscher
#
# This example is discussed in Chapter 16 of the book
# Object-Oriented Programming in Python
#
from socket import socket
from threading import Thread

class IncomingThread(Thread):
  def run(self):
    stillChatting = True
    while stillChatting:                     # wait for more incoming data
      transmission = server.recv(1024)       # 'server' will be defined globally at line 27
      lines = transmission.split('\n')[:-1]
      i = 0
      while i < len(lines):
        command = lines[i].split()[0]        # first keyword
        param = lines[i][len(command)+1: ]   # remaining information
        if command == 'GOODBYE':
          stillChatting = False
        elif command == 'NEW':
          print '==>', param, 'has joined the chat room'
        elif command == 'LEFT':
          print '==>', param, 'has left the chat room'
        elif command == 'MESSAGE':
          i += 1                            # need next line for content
          print '==>', param + ': ' + lines[i]
        elif command == 'PRIVATE':
          i += 1                            # need next line for content
          print '==>', param + ' [private]: ' + lines[i]
        i += 1

instructions = """
--------------------------------------------
Welcome to the chat room.

To quit, use syntax,
  quit

To send private message to 'Joe' use syntax,
  private Joe:how are you?

To send message to everyone, use syntax,
  hi everyone!
--------------------------------------------
"""

server = socket()                                   # shared by both threads
server.connect( ('localhost', 9000) )               # could be a remote host
username = raw_input('What is your name: ').strip()
server.send('ADD %s\n' % username )
incoming = IncomingThread()
incoming.start()

print instructions
active = True                                       # main thread for user input
while active:   
  message = raw_input()                             # wait for more user input
  if message.strip():
    if message.rstrip().lower() == 'quit':
      server.send('QUIT\n')
      active = False
    elif message.split()[0].lower() == 'private':
      colon = message.index(':')
      friend = message[7:colon].strip()
      server.send('PRIVATE %s\n%s\n' % (friend,message[1+colon: ]) )
    else:
      server.send('MESSAGE ' + message)
