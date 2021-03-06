// Author: Nathan Richgels
// File: main.cpp
// Date: 3/22/2012
// Class: CSIS252
// Assignment 8
#include <iostream>
using namespace std;
#include "date.h"

int main()
{
   cout << "This program is intended to debug and test the"
     << " \"date\" class" << endl << "that can be found in "
     << "this directory." << endl << endl;

   cout << "Method Testing:" << endl;
   cout << "Date Example1;" << endl;
   cout << "Date Example2(6, 8, 1993);" << endl << endl;
   Date Example1;
   Date Example2(6, 8, 1993);

   cout << "cout << Example1 << endl;" << endl;
   cout << Example1 << endl;
   cout << "cout << Example2 << endl;" << endl;
   cout << Example2 << endl << endl;

   cout << "Example1.setMonth(3);" << endl;
   Example1.setMonth(3);
   cout << "cout << Example1.getMonth() << endl;" << endl;
   cout << Example1.getMonth() << endl;
   cout << "Example1.setDay(22);" << endl;
   Example1.setDay(22);
   cout << "cout << Example1.getDay() << endl;" << endl;
   cout << Example1.getDay() << endl;
   cout << "Example1.setYear(2012);" << endl;
   Example1.setYear(2012);
   cout << "cout << Example1.getYear() << endl;" << endl;
   cout << Example1.getYear() << endl << endl;

   cout << "\nOperator Testing:" << endl;
   cout << "cout << Example1 << endl;" << endl;
   cout << Example1 << endl;
   cout << "\ncout << Example2 << endl;" << endl;
   cout << Example2 << endl << endl;

   cout << "Example1.setDate(3, 22, 2010)" << endl;
   cout << "Example2.setDate(3, 21, 2010)" << endl;
   cout << "Example1==Example2" << endl;
   if(Example1==Example2)
      cout << "True" << endl;
   else
      cout << "False" << endl;

   cout << "Example1>=Example2" << endl;
   if(Example1>=Example2)
      cout << "True" << endl;
   else
      cout << "False" << endl;

   cout << "Example1<=Example2" << endl;
   if(Example1<=Example2)
      cout << "True" << endl;
   else
      cout << "False" << endl;

   cout << "Example1>Example2" << endl;
   if(Example1>Example2)
      cout << "True" << endl;
   else
      cout << "False" << endl;

   cout << "Example1<Example2" << endl;
   if(Example1<Example2)
      cout << "True" << endl;
   else
      cout << "False" << endl;

   cout << "Example1!=Example2" << endl;
   if(Example1!=Example2)
      cout << "True" << endl << endl;
   else
      cout << "False" << endl << endl;


   cout << "Testing for invalid dates:" << endl;
   cout << "Example1.setDate(3, 0, 2012);" << endl;
   Example1.setDate(3, 0, 2012);
   cout << "\nExample1.setDate(3, 32, 2012);" << endl;
   Example1.setDate(3, 32, 2012);
   cout << "\nExample1.setDate(3, 31, 2012);" << endl << endl;
   Example1.setDate(3, 31, 2012);
   cout << "Example2.setDate(4, 31, 2012);" << endl;
   Example2.setDate(4, 31, 2012);
   cout << "\nExample1.setDate(2, 29, 2011);" << endl;
   Example1.setDate(2, 29, 2011);
   cout << "\ncout << Example1 << endl;" << endl;
   cout << Example1 << endl;
   cout << "\nExample.setDate(2, 29, 2012);" << endl;
   Example2.setDate(2, 29, 2012);
   cout << "\ncout << Example2 << endl;" << endl;
   cout << Example2 << endl;
   cout << "\nEnd of Test File" << endl;
   return 0;
}
