# Program: DeluxeTV1.py
# Authors: Michael H. Goldwasser
#          David Letscher
#
# This example is discussed in Chapter 9 of the book
# Object-Oriented Programming in Python
#
from Television import Television

class DeluxeTV(Television):
  """A television that maintains a set of favorite channels."""

  def __init__(self):
    """Creates a new DeluxeTV instance.

    The power is initially off, yet when turned on the TV is tuned to channel 2
    with a volume level of 5. The set of favorite channels is initially empty.
    """
    Television.__init__(self)                    # parent constructor
    self._favorites = []

  def addToFavorites(self):
    """Adds the current channel to the list of favorites, if not already there.

    If power is off, there is no effect.
    """
    if self._powerOn and self._channel not in self._favorites:
      self._favorites.append(self._channel)

  def removeFromFavorites(self):
    """Removes the current channel from the list of favorites, if present.

    If power is off, there is no effect.
    """
    if self._powerOn and self._channel in self._favorites:
      self._favorites.remove(self._channel)

  def jumpToFavorite(self):
    """Jumps to the "next" favorite channel as per the following rules.

    In general, this method jumps from the current channel setting to the next higher
    channel which is found in the set of favorites. However if no favorites are numbered
    higher than the current channel, it wraps around to the lowest favorite. If there are
    no favorites, the channel remains unchanged.

    Returns the resulting channel setting.

    If power is off, there is no effect.
    """
    if self._powerOn and len(self._favorites)>0:
      closest = max(self._favorites)             # a guess
      if closest <= self._channel:               # no bigger channel exist
        closest = min(self._favorites)           # wrap around to min
      else:                                      # let's try to get closer
        for option in self._favorites:
          if  self._channel < option < closest:
            closest = option                     # a better choice
      self.setChannel(closest)                   # rely on inherited method
      return closest


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
        
        
