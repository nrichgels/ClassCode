#!/usr/bin/python26

# Author: Nathan Richgels
#
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# base2dec is a function that an application programmer can use to convert
#a value from a base between 1 and 10 to it's integer decimal version.
# The first paramater (NOmValue), is an integer or string that will be directly
#changed to a decimal.
# The second paramater (OrigBase), is an integer or string that is the first
#parameter's base.


# Ask the user for a numerical integer value, and the base value.
def base2dec(NOmValue='', OrigBase='10'):
#-----------------------------------------------------------------------------------------
# DATA DICTIONARY:
# NOmValue- (str) Numerical Original Value.  What the user inputs to change
#to a decimal value.
#
# NOValue- (str) What the user inputs to change to a decimal value,
#ignoring the possible negative sign.
#
# OrigBase- (str) Original Base. The base that NOValue is hopefully centered on.
#
# absValue- (int) Until absValue is multiplied with the final value,
#the final value is x integers away from 0.
#
# Check- (str) The maximum sized string with the maximum amount of characters
#that our range of bases could use.
# BaseInt- (int) OrigBase integer form.
#
# CheckSec- (str) Secondary check list. If the user's input is true,
#this would contain all of the characters that could potentialy
#be in the user's integer.
#
# decValue- (int) Decimal Value of NOValue.
#------------------------------------------------------------------------------------------

    #Did the application programmer enter a string or integer?
    if not isinstance(NOmValue, (int, str)):
        raise TypeError("Paramater 1 is not a string.")
    if not isinstance(OrigBase, (int, str)):
       raise TypeError("Parameter 2 is not a string.")
    # Cover for the app programmer if he accedintally enters integers.
    NOmValue=str(NOmValue)
    OrigBase=str(OrigBase)

    #Make sure the user complied and entered input.
    if NOmValue=='':
        raise ValueError("Parameter 1 is an incalcable string.")
    elif NOmValue=='-':
        raise ValueError("Parameter 1 is an incalcable string.")

    # Determine if NOValue is positive or negative. Temporarily convert to
    #positive for the time being if it's not positive.
    if NOmValue[0]=="-":
        NOValue=NOmValue[1:len(NOmValue)]
        absValue=-1
    else:
        NOValue=NOmValue[0:len(NOmValue)]
        absValue=1
    # Check if OrigBase is a valid base for the user to use.

    if OrigBase== '':
        raise ValueError("Parameter 2 is a non-existant base.")
        
    BaseInt=0
    for index2 in range(len(OrigBase)):
        digit2=OrigBase[index2]
        dval2=ord(digit2)-ord('0')
        BaseInt+=dval2*10**(len(OrigBase)-1-index2)
    if BaseInt > 10 or BaseInt<=1:
        raise ValueError("Paramater 2's string must be within 1 and 10.")

    # Check if the numerical integer value is actually a number within the
    #base value.
    Check='0123456789'
    CheckSec=Check[0: BaseInt]

    for Test in NOValue:
        if Test not in CheckSec:
            raise ValueError("Paramater 1's string characters must be within the base's limit.")

    # Calculate the base changes.
    decValue=0
    if OrigBase=='2':
        for index in range(len(NOValue)):
            digit=NOValue[index]
            dval=ord(digit)-ord('0')
            decValue+=dval*2**(len(NOValue)-1-index)

    elif OrigBase=='3':
        for index in range(len(NOValue)):
            digit=NOValue[index]
            dval=ord(digit)-ord('0')
            decValue+=dval*3**(len(NOValue)-1-index)

    elif OrigBase=='4':
        for index in range(len(NOValue)):
            digit=NOValue[index]
            dval=ord(digit)-ord('0')
            decValue+=dval*4**(len(NOValue)-1-index)

    elif OrigBase=='5':
        for index in range(len(NOValue)):
            digit=NOValue[index]
            dval=ord(digit)-ord('0')
            decValue+=dval*5**(len(NOValue)-1-index)

    elif OrigBase=='6':
        for index in range(len(NOValue)):
            digit=NOValue[index]
            dval=ord(digit)-ord('0')
            decValue+=dval*6**(len(NOValue)-1-index)

    elif OrigBase=='7':
        for index in range(len(NOValue)):
            digit=NOValue[index]
            dval=ord(digit)-ord('0')
            decValue+=dval*7**(len(NOValue)-1-index)

    elif OrigBase=='8':
        for index in range(len(NOValue)):
            digit=NOValue[index]
            dval=ord(digit)-ord('0')
            decValue+=dval*8**(len(NOValue)-1-index)

    elif OrigBase=='9':
        for index in range(len(NOValue)):
            digit=NOValue[index]
            dval=ord(digit)-ord('0')
            decValue+=dval*9**(len(NOValue)-1-index)

    else:
        for index in range(len(NOValue)):
            digit=NOValue[index]
            dval=ord(digit)-ord('0')
            decValue+=dval*10**(len(NOValue)-1-index)

    return decValue*absValue

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# dec2BOX is a function that an application programmer can use to convert a
#decimal value to a base of 2, 8, or 16.
# The first paramater (StrDec) is the number that is being converted to a
#different base.
# The second paramater (StrBase) is the base that the decimal number will be
#converted to.  The second paramater (StrBase) is only valid when it is equal
#to '2', '8', '16', or the int versions of such.

def dec2BOX(StrDec='0', StrBase='2'):
#-------------------------------------------------------------------------------
# DATA DICTIONARY:
# StrDec-(str) The string hopefully containing a decimal integer that
#the user inputs
#
# StrBase- The base that the input will be converted to.
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
    if not isinstance(StrDec, (str, int)):
        raise TypeError("The first parameter is not a string or integer.")
    if not isinstance(StrBase, (str, int)):
        raise TypeError("The second paramater is not a string or integer.")
    
    StrDec=str(StrDec)
    StrBase=str(StrBase)
    # Get an integer from the user.  If the user doesn't give an integer, repeat the
    #instructions.  If the user doesn't input anything, close the program.
    Proof=0
    if StrDec=='':
        raise ValueError("No content entered.")

    # Detects if the user's input is valid, but negative.
    if StrDec[0]=="-":
        StrDec=StrDec[1:len(StrDec)]
        absValue='-'
    else:
        absValue=''
    for test in StrDec:
        if test not in '0123456789':
            Proof=Proof+1
    if not Proof==0:
        raise ValueError("Invalid characters found within string.")
        
    #       Detects if the user inputs '-'.  Will make the program decide to ask
    #the user to input a valid decimal number.
        if StrDec=='':
            raise ValueError("Number not detected for first paramater.")
            
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
    if StrBase=='2':
        return StrBin
    elif StrBase=='8':
        return StrOct
    elif StrBase=='16':
        return StrHex
    else:
        raise ValueError("Valid base was not selected.")


if __name__=="__main__":
    print "Test 1"
    raw_input("Press ENTER to test valid strings.")
    print 'base2dec("13", "4")'
    print base2dec("13", "4")
    print ""
    
    raw_input("Press ENTER to test valid integers.")
    print "base2dec(13, 4)"
    print base2dec(13, 4)
    print ""

    print "Test 2"
    EndTest=raw_input("Press ENTER to test illegal number type or press any key, then enter to skip.")
    if EndTest=="":
        print 'base2dec([3, 4, 5], "10")'
        print base2dec([3, 4, 5], "10")
    EndTest=raw_input("Press ENTER to test illegal base type or press any key, then enter to skip.")
    if EndTest=="":
        print 'base2dec("10", [3, 4, 5])'
        print base2dec("10", [3, 4, 5])
    print ""

    print "Test 3"
    EndTest=raw_input("Press ENTER to test non-number strings, or press any key, then enter to skip.")
    if EndTest=="":
        print "Non-number based characters:"
        print 'base2dec("abc", "10")'
        print base2dec("abc", "10")
        
    EndTest=raw_input("Press ENTER to test out of range numbers, or press any key, then enter to skip.")
    if EndTest=="":
        print "Out of range digits:"
        print 'base2dec("5", "4")'
        print base2dec("5", "4")
    print ""

    print "Test 4"
    EndTest=raw_input("Press ENTER to test non-number base strings, or press any key, then enter to skip.")
    if EndTest=="":
        print "Non-number base:"
        print 'base2dec("5", "abc")'
        print base2dec("5", "abc")

    raw_input("Press ENTER to test an out of range base.")
    print "Out of range base:"
    print 'base2dec("5", "11")'
    print base2dec("5", "11")
    print "End Test"
