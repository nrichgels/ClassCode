#!/usr/bin/python26

# Progammer: Nathan Richgels
# Demo Example 2.34
# Asks user for height and weight, and computes body mass index.

# Data Definition
# height- str- user's input for height
# feet- int- number of feet in user's height
# inches- int- number of inches in user's height
# tot_inches- int- user's height in inches

# Introduce yourself.
print 'Welcome to Rick\'s BMI calculator!'

# Request and get the user's height.
height=raw_input("Please enter your height as ft'in\" where ft and in are integer: ")

# Determine number of feet in user's height.
feet=int(height[0:height.index("'")])

# Determine inches in user's height.
# Calculate total inches of user's height.
# Request and get the user's weight in pounds.
# Calculate the user's body mass index.
# Report the calculated BMI. (ECHO INPUT)
