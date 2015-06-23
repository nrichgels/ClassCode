# !/usr/bin/python26
# Nathan Richgels
# Class Exercise 9/23/11
# Intro to Computer Programming I
#
# Data Objects-
# scene- the canvas that will contain my assignment.
# StopLight- The Layer holding my Stoplight.
# Container- "Contains" the light.
# LightR- The Red light for the stoplight.
# LightY- The Yellow light for the stoplight.
# LightG- The Green light for the stoplight.
# Culprit- Text inserted into the canvas revealing the name of the
# one who made this program.
#
# Overall objective- Create a Stoplight that blinks from green
# to yellow to red. Stoplight then goes horizontal with all lights lit
# and displays my name underneath.

# Prepare the Program for the task at hand.
from cs1graphics import *
scene= Canvas(400, 400, 'darkCyan', 'Nathan Richgels')
from time import sleep
# Create a Layer containing the stoplight.
StopLight=Layer()
StopLight.adjustReference(200,200)
# Manufacture the border for the stoplight.
Container=Rectangle(150, 280, Point(200, 200))
Container.setFillColor('grey10')
# Create the three lights for the stoplight, and insert them.
LightR=Circle(35, Point(200, 120))
LightR.setDepth(49)
LightR.setFillColor('red')

LightY=LightR.clone()
LightY.setFillColor('yellow')
LightY.moveTo(200, 200)

LightG=LightR.clone()
LightG.setFillColor('green')
LightG.moveTo(200, 280)

StopLight.add(LightG)
StopLight.add(LightY)
StopLight.add(Container)
StopLight.add(LightR)

# add the layer to our scene.
scene.add(StopLight)

# Now we get to confuse traffic by making the lights
# change every 2 second intervals.
sleep(3)
LightR.setDepth(51)
LightY.setDepth(51)

sleep(2)
LightG.setDepth(51)
LightY.setDepth(49)

sleep(2)
LightY.setDepth(51)
LightR.setDepth(49)

# The traffic light will then snap and fall on it's side.  The person
# responsible might not return to the scene of the crime, but his name
# will be written all over it.  Or, in this case, under it.
# The whole layer will now be rotated.
sleep(2)
StopLight.rotate(90)
LightY.setDepth(49)
LightG.setDepth(49)

# Finally, the text will be displayed under the horzontal light.
Culprit=Text("Nathan Richgels", 32)
Culprit.moveTo(200, 325)
scene.add(Culprit)
