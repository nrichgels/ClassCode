# Program: date.py
# Authors: Michael H. Goldwasser
#          David Letscher
#
# This example is discussed in Chapter 2 of the book
# Object-Oriented Programming in Python
#
monthNames = ('January', 'February', 'March', 'April',
                'May', 'June', 'July', 'August', 'September',
                'October', 'November', 'December')

# get input from user
original = raw_input('Please enter a date (MM-DD-YYYY): ')

pieces   = original.split('-')
month    = pieces[0]                     # this is a string of numerals (e.g., '10')
day      = pieces[1]
year     = pieces[2]

alternate = monthNames[int(month)-1] + ' ' +  day + ', ' + year
print alternate
