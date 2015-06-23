#!/usr/bin/python26

# Author: Nathan Richgels
# base2dec is a function that an application programmer can use to convert
#a value from a base between 1 and 10 to it's integer decimal version.
# The first paramater (NOmValue), is an integer or string that will be directly
#changed to a decimal.
# The second paramater (OrigBase), is an integer or string that is the first
#parameter's base.


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


# Ask the user for a numerical integer value, and the base value.
def base2dec(NOmValue='', OrigBase='10'):
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
