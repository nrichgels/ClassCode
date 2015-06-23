# Program: DeluxeTV2.py
# Authors: Michael H. Goldwasser
#          David Letscher
#
# This example is discussed in Chapter 9 of the book
# Object-Oriented Programming in Python
#
from Television import Television
from SortedSet import SortedSet

class DeluxeTV(Television):
  """
  Just like a standard television, but with additional support for
  maintaining and using a set of favorite channels.
  """

  def __init__(self):
    """
    Creates a new Television instance.

    The power is initially off.  Upon the first time the TV is turned on,
    it will be set to channel 2, and a volume level of 5.

    The television maintains a list of favorite channels, initially empty.
    """
    Television.__init__(self)                     # parent constructor
    self._favorites = SortedSet()

  def addToFavorites(self):
    """
    Adds the current channel to the list of favorites, if not already there.

    If power is off, there is no effect.
    """
    if self._powerOn:
      self._favorites.append(self._channel)

  def removeFromFavorites(self):
    """
    Removes the current channel from the list of favorites, if present.

    If power is off, there is no effect.
    """
    if self._powerOn and self._channel in self._favorites:
      self._favorites.remove(self._channel)

  def jumpToFavorite(self):
    """
    Jumps to the 'next' favorite channel as per the following rules.

    In general, this behavior jumps from the current channel
    setting to the next higher channel which is found in the set
    of favorites.  However if there are no such higher channels,
    it jumps to the overall minimal favorite.  If there are no
    favorites at all, this has no effect on the channel setting.

    Returns the resulting channel setting.

    If power is off, there is no effect.
    """
    if self._powerOn and len(self._favorites)>0:
      resultIndex = self._favorites.indexAfter(self._channel)
      if resultIndex == len(self._favorites):
        result = self._favorites[0]               # wrap around
      else:
        result = self._favorites[resultIndex]
      self.setChannel(result)
      return result


###############################################################################
# unit testing follow
###############################################################################
if __name__ == '__main__':
  mytv = DeluxeTV()
  mytv.togglePower()
  mytv.setChannel(6)
  mytv.addToFavorites()
  mytv.setChannel(12)
  mytv.addToFavorites()
  mytv.setChannel(24)
  mytv.addToFavorites()
  mytv.setChannel(19)
  mytv.addToFavorites()
  mytv.channelDown()
  mytv.addToFavorites()
  mytv.setChannel(19)
  mytv.removeFromFavorites()
  for c in range(Television._minChannel, Television._maxChannel + 1):
    mytv.setChannel(c)
    predicted = c - c % 6 + 6
    if predicted > 24:
      predicted = 6
    jumped = mytv.jumpToFavorite()
    if not (jumped == predicted == mytv._channel):
      print 'ERROR:  jumpToFavorite from base of %s returned %s' % (c,jumped)
        
        
