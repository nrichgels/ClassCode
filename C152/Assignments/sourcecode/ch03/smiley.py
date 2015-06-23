# Program: smiley.py
# Authors: Michael H. Goldwasser
#          David Letscher
#
# This example is discussed in Chapter 3 of the book
# Object-Oriented Programming in Python
#
from cs1graphics import *
paper = Canvas()

head = Circle(75, Point(100,100))
head.setFillColor('yellow')
head.setDepth(60)
paper.add(head)

mouth = Circle(40, Point(100,110))
mouth.setFillColor('black')
mouth.setBorderWidth(0)
mouth.setDepth(52)
paper.add(mouth)

mouthCover = Circle(40, Point(100,100))
mouthCover.setFillColor('yellow')
mouthCover.setBorderWidth(0)
mouthCover.setDepth(51)
paper.add(mouthCover)

nose = Polygon(Point(100,90), Point(92,110), Point(108,110))
nose.setFillColor('black')
paper.add(nose)

leftEye = Circle(10, Point(70,80))
leftEye.setFillColor('black')
rightEye = Circle(10, Point(130,80))
rightEye.setFillColor('black')
paper.add(leftEye)
paper.add(rightEye)

leftEyebrow = Path(Point(60,65), Point(70,60), Point(80,65))
leftEyebrow.setBorderWidth(3)
leftEyebrow.adjustReference(10,15)       # set to center of left eyeball
leftEyebrow.rotate(-15)
paper.add(leftEyebrow)

rightEyebrow = leftEyebrow.clone()
rightEyebrow.flip()                      # still relative to eyeball center
rightEyebrow.move(60,0)                  # distance between eyeball centers
paper.add(rightEyebrow)
