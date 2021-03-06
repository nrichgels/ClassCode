// Author: Nathan Richgels
// File: main.cpp
// Date: 1/31/2012
// Class: CSIS352
// Assignment 1
#include <iostream>
using namespace std;
#include "money.h"
/*
bool operator==(double d, const Money& m)
{
   return m==d;
}
*/
          
int main()
{
   Money m1;  // initially 0;
   Money m2(34.43);
   Money m3(753);
   Money::setFieldSize(12);
   Money::setFormat(General);  // General is the default
   cout << m2 << endl;
   Money::setFormat(Currency);
   cout << m2 << endl;
   Money::setFormat(Accounting);
   cout << m2 << endl;
   cout << (m1 == m2) << endl;  // relational operators
   cout << (m2 == 34.43) << endl;
//   cout << (34.43 == m2) << endl;  nah
   m1 = m2;  // default operator = will handle this
   m1 = 54.23; // need to overload the = operator
   m3 = m1 + m2;
   cout << m3 << endl;
   m3 = m1 + 10;
   m3 = m2 - m1;
   m3 = m2 - 10;
   m3 = m2 * 2;
//   m3 = m1 * m2;  nah
   m3 = m2 / 2;
//   m3 = m1 / m2;  nah
// m3 = m2 % 2;
   double d;
//   d = m2;  can't
   d = m2.Value();
   cout << d << endl;
   cout << m2.getDollars() << endl;
   cout << m2.getCents() << endl;
   
// BONUS STUFF
   Money::setFormat(NoDollarSign);
   cout << m2 << endl;
   Money::setFormat(DollarSign);
   cout << m2 << endl;
   m2 = m2+.1;
   Money::setFormat(Truncate);
   cout << m2 << endl;
   Money::setFormat(Round);
   cout << m2 << endl;
   Money m4;
   m4 = 23445634.59;
   Money::setFormat(Cents);
   Money::setFieldSize(20);
   cout << m4 << endl;
   Money::setFormat(Commas);
   cout << m4 << endl;
   Money::setFormat(NoCommas);
   cout << m4 << endl;
   
   
   return 0;
}
