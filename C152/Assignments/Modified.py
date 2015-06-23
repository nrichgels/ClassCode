#!/usr/bin/python
# Author:  Rick Walker
# Modified by: Nathan Richgels
# Class Exercise 2
# This script demonstrates use of basic cs1graphics classes and identifies
# the use of the Layer class as means to create more complex entities.
# It creates a stoplight image, lights the lights and rotates the stoplight
# to demonstrate the use of the Layer.

##########  Data Dictionary ####################################
# scene - Canvas - graphics window
# stoplight - Layer - the layer supporting the stoplight object group
# red - Circle - the stoplight's red light
# yellow - Circle - the stoplight's yellow light
# green - Circle - the stoplight's green light
# frame - Circle - the background/frame for the stoplight
# name - Text - for displaying name message
# message - Text - for displaying quit message at end of script
# sleeptime - int - time in seconds to pause animation
################################################################

# Imported modules
import time
from cs1graphics import *

# Constants
sleeptime = 1

# Create graphics window 
scene = Canvas(400, 400, 'light blue', "Rick & Nathan's Stoplight")

# Create and populate the Layer containing the stoplight
stoplight = Layer()
# Background
frame = Rectangle(60, 200)
frame.setFillColor('black')
stoplight.add(frame)
# Yellow light
yellow = Circle(25)
yellow.setFillColor('yellow')
yellow.setDepth(40)
stoplight.add(yellow)
# Red light
red = yellow.clone()
red.setFillColor('red')
red.move(0, -63)
stoplight.add(red)
# Green light
green = yellow.clone()
green.setFillColor('green')
green.move(0, 63)
stoplight.add(green)

# Relocate the stoplight to the middle of the drawing surface
#   and display it
stoplight.moveTo(200, 200)
scene.add(stoplight)
time.sleep(sleeptime)

# Green light lit
red.setFillColor('black')
yellow.setFillColor('black')
time.sleep(sleeptime)

# Yellow light lit
green.setFillColor('black')
yellow.setFillColor('yellow')
time.sleep(sleeptime)

# Red light lit
red.setFillColor('red')
yellow.setFillColor('black')
time.sleep(sleeptime)

# Rotate and display all lights on
green.setFillColor('green')
yellow.setFillColor('yellow')

stoplight.rotate(90)
time.sleep(sleeptime)
stoplight.rotate(90)
time.sleep(sleeptime)
stoplight.rotate(90)
time.sleep(sleeptime)
stoplight.rotate(90)
time.sleep(sleeptime)
stoplight.rotate(90)
time.sleep(sleeptime)

# Display name and quit
name = Text("Nathan Richgels", 24)
name.moveTo(200, 300)
scene.add(name)
message = Text("Click On Window To Quit", 16)
message.moveTo(200, 350)
scene.add(message)
scene.wait()
scene.close()

