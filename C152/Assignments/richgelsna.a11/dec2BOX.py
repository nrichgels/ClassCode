#!/usr/bin/python26

# Author: Nathan Richgels
# Asmt 8
# Ask the User to enter a numerical value, and change the value to
#binary, octal, and hexidecimal form.

#-------------------------------------------------------------------------------
# DATA DICTIONARY:
# StrDec-(str) The string hopefully containing a decimal integer that
#the user inputs
#
# Value-(str) While this is false, some code will be looped.
#
# Proof-(int) If proof is 0 at a certain point of the script, Value will become
#true, but more importantly stop being false.
#
# absValue-(str) If the user's dec number is negative, this will assure to make
#the output to be negative.
#
# test-(str) A value that changes to different indexes of the user's original
#input
#
# change-(str) This will go through all of the indices of the
#user's string to convert it to an integer.
#
# digit-(str) becomes each character of the string.
#
# Str(-Bin, -Oct, -Hex)-(str) StrDec with a (Binary, Octal, Hexidecimal) base.
#
# (Bin-, Oct-, Hex-)Quot-(Int) The remaining quotient that's being converted to
#(Binary, Octal, Hexidecimal).
#
# (Bin-, Oct-, Hex-)Div-(Int) Quotient divided by divisor Aka (Binary, Octal,
#Hexidecimal) base.
#
# (Bin-, Oct, Hex-)Sub-(Int) Rounded down quotient multiplied by (2, 8, 16)
#then usedto subtract from the original quotient to get the remainder (which is
#a digit in the (binary, Octal, Hexidecimal) integer).
#
# HexSymbols- (list) The letters that could possibly symbolize a normally two
#digit integer.
#
# Hex Conv- (int) The remainder that will be converted to a proper string
#before being added to the Hexidecimal based string.
#
# HexIndex- (int) The index of the letter that the value (greater than 10)
#corresponds to.
#
# HexSymb- (str) The character that will represent a number.  Will be added
#farthest to the left of the Hexidecimal string (StrHex).
#-------------------------------------------------------------------------------

# Retrieve needed functions.
from base_con import *

# Get an integer from the user.  If the user doesn't give an integer, repeat the
#instructions.  If the user doesn't input anything, close the program.
Value='false'
while Value=='false':
    StrDec=raw_input("Please enter a decimal based integer or press ENTER to close program: ")
    Proof=0
    if StrDec=='':
        exit(0)

# Detects if the user's input is valid, but negative.
    if StrDec[0]=="-":
        StrDec=StrDec[1:len(StrDec)]
        absValue='-'
    else:
        absValue=''
    for test in StrDec:
        if test not in '0123456789':
            Proof=Proof+1
    if Proof==0:
        Value='true'
        
#       Detects if the user inputs '-'.  Will make the program decide to ask
#the user to input a valid decimal number.
        if StrDec=='':
            print "Valid number not detected."
            Value='false'
    else:
        print Proof, "illegible characters detected. Integer must be within base 10."
        
# Convert the decimal string input to an integer.
IntDec=0
IntDec=base2dec(StrDec, 10)
    
# For Binary:
#  Create some constants to be used to convert to binary.
BinQuot=IntDec+0
StrBin=''

#  Divide the integer by the upcoming base, quotient will be rounded down.
#  Multiply rounded down number by 2.
while BinQuot>0:
    BinDiv=BinQuot/2
    BinSub=BinDiv*2

#Subtract from quotient to get remainder, stringify the integer, and add it to
#the front of the developing binary number. Of course, not forgetting to make
#a new central quotient :)
    StrBin=str(BinQuot-BinSub)+StrBin
    BinQuot=BinQuot/2

#  Add the binary prompt and negative sign (if necessary) to the beginning.
StrBin=absValue+'0b'+ StrBin


# For Octal:
#  Create some constants to be used to convert to octal
OctQuot=IntDec+0
StrOct=''

#  Similar steps from Binary
while OctQuot>0:
    OctDiv=OctQuot/8
    OctSub=OctDiv*8
    StrOct=str(OctQuot-OctSub)+StrOct
    OctQuot=OctQuot/8
#  Add the Octal prompt and negative sign (if neccissary) to the beginning.
StrOct=absValue+'0'+StrOct


# For Hexadecimal:
#  Create some constants to be used to convert to Hexidecimal.
HexQuot=IntDec+0
StrHex=''
HexSymbols=['a', 'b', 'c', 'd', 'e', 'f']

#  Similar steps from Binary & Octal, except...
while HexQuot>0:
    HexDiv=HexQuot/16
    HexSub=HexDiv*16
    HexConv= HexQuot-HexSub
    
#   ...if remainder more than 9 is true, then assign a letter to the remainder,
#so there's a single digit representative for the remainder.
    if HexConv>9:
        HexIndex=HexConv-10
        HexSymb=HexSymbols[HexIndex]
        
#   ...if remainder more than 9 is false, simply convert the remainder to a str.
    else:
        HexSymb=str(HexConv)
    StrHex=HexSymb+StrHex
    HexQuot=HexQuot/16
StrHex=absValue+'0x'+StrHex



#Repeat what the user has told you, then print the user's answer, and exit!
print StrDec + " as a(n)..."
print "...binary number will yield " + StrBin+"."
print "...Octal number will yield " + StrOct+"."
print "...Hexadecimal number will yield " + StrHex+"."
print "Have a nice day!"
raw_input("Press ENTER to end the program.")
exit(0)
