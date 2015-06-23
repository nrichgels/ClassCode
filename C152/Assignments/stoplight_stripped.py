#!/usr/bin/python
# Author:  Rick Walker
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
# message - Text - for diplaying name message of end of script
################################################################

# Imported modules
import time
from cs1graphics import *

# Constants
sleeptime = 1

# Create graphics window 
scene = Canvas(400, 400, 'light blue', "Rick's Stoplight", False)

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

# Create a list of lights so that the lights are
# easily referenced by a for loop
lights = [green, yellow, red]

# Relocate the stoplight to the middle of the drawing surface
#   and display it
stoplight.moveTo(200, 200)
scene.add(stoplight)
scene.refresh()

# Something magic should happen here!!!


time.sleep(sleeptime)

# Display name
message=Text("Click On Window to Quit", 20)
message.moveTo(200, 350)
scene.add(message)
scene.refresh()
scene.wait()
scene.close()

