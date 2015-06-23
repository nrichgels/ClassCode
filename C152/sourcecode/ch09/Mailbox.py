# Program: Mailbox.py
# Authors: Michael H. Goldwasser
#          David Letscher
#
# This example is discussed in Chapter 9 of the book
# Object-Oriented Programming in Python
#
from cs1graphics import *

class Mailbox(Drawable):
  """A graphical primitive representing a Mailbox.

  The user can choose the color, open and close the door, and raise and lower the flag.
  """
  def __init__(self, flagUp=False, doorOpen=False, color='white'):
    """Creates a new mailbox instance.

    The reference point is initially at the bottom of the post.

    flagUp         boolean determining whether flag is initially raise (default False)
    doorOpen       boolean determining whether door is initially open (default False)
    color          color of the box and door (default white)
    """
    Drawable.__init__(self)                       # call the parent constructor

    # post sits on top of the origin
    self._post = Rectangle(16, 80, Point(0,-40))
    self._post.setFillColor('brown')

    # box sits on top of post, slightly left to offset door
    self._box = Rectangle(50, 30, Point(-3,-95))
    self._box.setFillColor(color)

    # door attaches to right-side of box
    self._door = Rectangle(6, 30, Point(25,-95))
    self._door.setFillColor(color)
    self._door.adjustReference(-3, 15)            # act as hinge connected to box
    self._doorOpen = doorOpen
    if doorOpen:
      self._door.rotate(90)

    self._flag = Polygon(Point(15,-100), Point(15,-106), Point(-15,-106),
                         Point(-15,-90), Point(-5,-90), Point(-5,-100))
    self._flag.setFillColor('red')
    self._flag.adjustReference(-3,-3)             # act as rivot holding flag
    self._flagUp = flagUp
    if flagUp:
      self._flag.rotate(90)

  def _draw(self):
    self._beginDraw()                             # required protocol
    self._post._draw()
    self._box._draw()
    self._door._draw()
    self._flag._draw()
    self._completeDraw()                          # required protocol

  def setColor(self, color):
    """Change the color of the box and door to indicated color.

    Note that the post and flag are unchanged.
    """
    self._box.setFillColor(color)
    self._door.setFillColor(color)

  def doorIsOpen(self):
    """Returns True if door is currently open; False otherwise"""
    return self._doorOpen
  
  def openDoor(self):
    """Opens the door.

    If door is already open, has no effect.
    """
    if not self._doorOpen:
      for i in range(90):                         # animate the motion
        self._door.rotate(1)
      self._doorOpen = True

  def closeDoor(self):
    """Closes the door.

    If door is already closes, has no effect.
    """
    if self._doorOpen:
      for i in range(90):                         # animate the motion
        self._door.rotate(-1)
      self._doorOpen = False

  def flagIsUp(self):
    """Returns True if the flag is currently raised; False otherwise"""
    return self._flagUp
  
  def toggleFlag(self):
    """Switches the flag to the opposite setting.

    That is, lowers the flag if currently raised; raises flag if currently lowered.
    """
    if self._flagUp:
      increment = -1
    else:
      increment = 1
    for i in range(90):                           # animate the motion
      self._flag.rotate(increment)
    self._flagUp = not self._flagUp

# unit test to demonstrate sample usage
if __name__ == "__main__":
  paper = Canvas(300,300)
  box = Mailbox()
  box.move(150,200)
  paper.add(box)
  raw_input('Press Return to Continue')

  box.toggleFlag()
  raw_input('Press Return to Continue')

  box.setColor('grey')
  raw_input('Press Return to Continue')

  box.toggleFlag()
  box.openDoor()
  raw_input('Press Return to Continue')

  box.scale(1.5)
  raw_input('Press Return to Continue')

  box.closeDoor()
  raw_input('Press Return to End')
  paper.close()
