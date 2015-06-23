// Author: Nathan Richgels
// File: converter.h
// Date: 4/11/2012
// Class: CSIS252
// Assignment 10
#ifndef __CONVERTER_H__
#define __CONVERTER_H__

#include <iostream>
using namespace std;

class Converter
{
   public:
      // Method: DecimalToAnyBase
      // description - Converts a Decimal based value to any other base
      // precondition - integer value and a Base value is given.
      // postcondition- A string of the new base is returned
      // method input - int: decimal integer
      // method output- string: newBase integer
      static string DecimalToAnyBase(int value, int newBase);

      // Method: AnyBasetoDecimal
      // description - Converts a value of any base to a Decimal value
      // precondition - integer value and current Base is given.
      // postcondition - Integer that is decimal basedis returned.
      // method input - string: Value to be converted, int: Current Base
      // method output - int: Decimal value of given string w/ given base.
      static int AnyBaseToDecimal(string value, int currentBase);
};

#endif
