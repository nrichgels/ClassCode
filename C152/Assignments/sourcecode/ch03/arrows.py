# Program: arrows.py
# Authors: Michael H. Goldwasser
#          David Letscher
#
# This example is discussed in Chapter 3 of the book
# Object-Oriented Programming in Python
#
from cs1graphics import *
from time import sleep

scene = Canvas()
scene.setBackgroundColor('skyBlue')
grass = Rectangle(200, 80, Point(100,160))
grass.setFillColor('green')
grass.setBorderColor('green')
grass.setDepth(100)
scene.add(grass)
sun = Circle(20, Point(50,30))
sun.setFillColor('yellow')
scene.add(sun)

target = Layer()
outside = Circle(30)
outside.setFillColor('white')
outside.setDepth(49)
target.add(outside)
middle = Circle(20)
middle.setFillColor('blue')
middle.setDepth(48)
target.add(middle)
inside = Circle(10)
inside.setFillColor('red')
inside.setDepth(47)
target.add(inside)
legs = Path(Point(-25,45), Point(0,0), Point(25,45))
legs.setBorderWidth(2)
target.add(legs)
target.move(160,110)
target.setDepth(75)           # in front of grass; behind arrows
scene.add(target)

# prepare three arrows, but do not yet add to scene
arrow1 = Layer()
tip = Polygon(Point(0,0), Point(-8,5), Point(-5,0), Point(-8,-5))
tip.setFillColor('white')
arrow1.add(tip)
shaft = Path(Point(-30,0), Point(-5,0))
shaft.setBorderWidth(2)
shaft.setDepth(51)
arrow1.add(shaft)
fletching = Polygon(Point(-30,0), Point(-33,-3), Point(-40,-3),
                    Point(-36,0), Point(-38,3), Point(-36,3))
fletching.setFillColor('white')
arrow1.add(fletching)
arrow1.move(15,120)           # initial position
arrow2 = arrow1.clone()
arrow3 = arrow1.clone()

dialogue = Text('Click target to fire an arrow')
dialogue.move(100,170)
scene.add(dialogue)

target.wait()                 # wait indefinitely for user event on target
scene.add(arrow1)
arrow1.rotate(-20)
sleep(0.25)
arrow1.move(41,-15)
arrow1.rotate(7)
sleep(0.25)
arrow1.move(41,-5)
arrow1.rotate(7)
sleep(0.25)
arrow1.move(41,5)
arrow1.rotate(7)
sleep(0.25)
arrow1.move(41,17)
arrow1.rotate(7)

target.wait()                 # wait indefinitely for user event on target
scene.add(arrow2)
arrow2.rotate(-40)
sleep(0.25)
arrow2.move(39,-22)
arrow2.rotate(17)
sleep(0.25)
arrow2.move(39,-12)
arrow2.rotate(17)
sleep(0.25)
arrow2.move(39,3)
arrow2.rotate(17)
sleep(0.25)
arrow2.move(39,13)
arrow2.rotate(17)

target.wait()                 # wait indefinitely for user event on target
scene.add(arrow3)
arrow3.rotate(-30)
sleep(0.25)
arrow3.move(37,-26)
arrow3.rotate(10)
sleep(0.25)
arrow3.move(37,-11)
arrow3.rotate(10)
sleep(0.25)
arrow3.move(37,6)
arrow3.rotate(10)
sleep(0.25)
arrow3.move(37,21)
arrow3.rotate(10)
dialogue.setMessage('Good shooting!')

scene.wait()                  # wait for user event anywhere on canvas
scene.close()
