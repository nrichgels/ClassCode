// Author: Nathan Richgels
// File: main.cpp
// Date: 4/11/2012
// Class: CSIS252
// Assignment 10
#include <iostream>
#include "converter.h"
using namespace std;

int main()
{
   cout << "Testing DecimalToAnyBase: " << endl;

   cout << "2 DEC. to BIN. is " << Converter::DecimalToAnyBase(2, 2) << endl;

   cout << "140 DEC. to HEX. is " << Converter::DecimalToAnyBase(140, 16)
      << endl;

   cout << "8 DEC. to DEC. is " << Converter::DecimalToAnyBase(8, 10) << endl;

   cout << "-12 DEC. to BIN is " << Converter::DecimalToAnyBase(-12, 2)
      << endl;

   cout << "Testing AnyBaseToDecimal: " << endl;

   cout << "10 BIN. to DEC. is " << Converter::AnyBaseToDecimal("10", 2)
      << endl;

   cout << "8C HEX. to DEC. is " << Converter::AnyBaseToDecimal("8C", 16)
      << endl;

   cout << "8 DEC. to DEC. is " << Converter::AnyBaseToDecimal("8", 10)
      << endl;

   cout << "-1100 BIN. to DEC. is " << Converter::AnyBaseToDecimal("-1100", 2)
      << endl;
   return 0;
}
