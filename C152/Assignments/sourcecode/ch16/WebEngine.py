# Program: WebEngine.py
# Authors: Michael H. Goldwasser
#          David Letscher
#
# This example is discussed in Chapter 16 of the book
# Object-Oriented Programming in Python
#
from Engine import Engine
from urllib import urlopen
from socket import gethostname
from SocketServer import TCPServer, BaseRequestHandler

def recursiveCrawl(pageURL, wizard, maxDepth, knownPages = set()):
  print 'Crawling', pageURL
  knownPages.add(pageURL)

  try:
    contents = urlopen(pageURL).read()
    wizard.addDocument(removeHTMLTags(contents), pageURL)
    if maxDepth > 0:     # look for pages linked from this one
      links = getLinks(contents, pageURL)
      for newURL in links:
        if newURL not in knownPages:
          recursiveCrawl(newURL, wizard, maxDepth-1, knownPages)
  except:
    pass     # if anything goes wrong, ignore the current page but do not crash

def removeHTMLTags(html):
  text = ''
  insideTag = False
  for c in html:
    if not insideTag and c != '<':
      text += c
    elif not insideTag:
      insideTag = True
    elif c == '>':
      insideTag = False
  return text

def getLinks(contents, page):
  links = []
  indexStart = 0
  length = len(contents)
  while indexStart < length:
    indexStart = contents.find('href="', indexStart)
    if indexStart > -1:
      indexEnd = contents.find('"', indexStart + 6)
      link = contents[indexStart+6:indexEnd]
      if link[:7].lower() != 'http://':    # look for relative URLs
        if link[0] == '/':                 # this link is relative to the current domain
          link = 'http://' + page.split('/')[2] + link
        else:                              # this link is relative to the current URL
          link = '/'.join(page.split('/')[:-1]) + '/' + link
      if link[-5:].lower()=='.html' or link[-4:].lower()=='.htm' or link[-1]=='/':
        links.append(link)
      indexStart = indexEnd + 1
    else:
      indexStart = length

  return links

# Server for searching
class SearchHandler(BaseRequestHandler):
  def handle(self):
    searchTerm = self.request.recv(1024)
    searchResult = wizard.makeReport(searchTerm)

    self.request.send('Length: ' + str(len(searchResult)) + '\n')
    self.request.send(searchResult + '\n')

startingPage = raw_input('Enter the URL of the initial web page: ')
searchDepth = int(raw_input('Enter the maximum crawling depth: '))

# First crawl the web to build the index
wizard = Engine()
recursiveCrawl(startingPage, wizard, searchDepth)

localHost = gethostname()  # or you may hardwire your computer's host name
searchServer = TCPServer( (localHost, 9000), SearchHandler)
print
print 'Starting the server on', localHost
searchServer.serve_forever()
