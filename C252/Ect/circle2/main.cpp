// File:     main.cpp
// Author:   Dan Brekke
// Date: 

// Description
// This program will test the circle class

#include <iostream>
#include <iomanip>
#include "circle.h"
using namespace std;
/*
bool operator==(const Circle& leftside, const Circle& rightside)
{
    return leftside.radius() == rightside.radius();
}

ostream& operator << (ostream& out, const Circle& c)
{
//   out << "Area: " << c.area() << endl;
   out << c.area();  // better
   return out; 
}
*/

int main()
{
   cout << showpoint << fixed << setprecision(2);
   Circle c(3);
   Circle c2;
   cin >> c2;
   if (c == c2)
      cout << "they're equal\n";
   else
      cout << "Not equal\n";
   cout << "Area: " << c << endl;

   return 0;
}
