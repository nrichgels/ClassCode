# Program: helloWidget.py
# Authors: Michael H. Goldwasser
#          David Letscher
#
# This example is discussed in Chapter 3 of the book
# Object-Oriented Programming in Python
#
from cs1graphics import *

paper = Canvas()
nameInput = TextBox(150, 30, Point(100,30))
paper.add(nameInput)
submit = Button('Enter name', Point(100,80))
paper.add(submit)
submit.wait()
welcome = Text('Hello, ' + nameInput.getMessage())
welcome.move(100, 150)
paper.add(welcome)
