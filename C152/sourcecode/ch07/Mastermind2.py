# Program: Mastermind2.py
# Authors: Michael H. Goldwasser
#          David Letscher
#
# This example is discussed in Chapter 7 of the book
# Object-Oriented Programming in Python
#
from Mastermind import Mastermind
from TextInput import TextInput
from GraphicsOutput import GraphicsOutput

if __name__ == '__main__':
  palette = ('Red', 'Blue', 'Green', 'White', 'Yellow', 'Orange',
             'Purple', 'Turquoise')
  input = TextInput(palette)
  output = GraphicsOutput(palette)      # choose the graphics output this time
  game = Mastermind(input, output)
