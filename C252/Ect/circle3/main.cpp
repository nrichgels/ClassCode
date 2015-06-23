// File:     main.cpp
// Author:   Dan Brekke
// Date: 

// Description
// This program will test the circle class

#include <iostream>
#include <iomanip>
#include "circle.h"
#include "arrayListType.h"
using namespace std;

void func(arrayListType x)
{
}


int main()
{
   cout << showpoint << fixed << setprecision(2);
   Circle c(3);
   arrayListType list(10);
   list.insertEnd(c);
   c.setRadius(2);
   list.insertEnd(c);
   c.setRadius(7);
   list.insertAt(1,c);
   list.print();

   list = list;

   for (int i=0; i<list.listSize(); i++)
   {
      list.retrieveAt(i,c);
      cout << "area: " << c.area() << endl;
   }

   arrayListType list2;
   cerr << "address of list " << &list << endl;
   cerr << "address of list2 " << &list2 << endl;
   list2 = list;

   func(list);
   return 0;
}
