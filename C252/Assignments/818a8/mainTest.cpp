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
   Date E1, E2;
   E1.setDate(6, 8, 1993);
   E2=E1;
   cout << E2 << endl;
   return 0;
}
