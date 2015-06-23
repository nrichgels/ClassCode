// Author: Nathan Richgels, Dr. Brekke
// File: main.cpp
// Date: 3/26/2013
// Class: CSIS352
// Assignment 5

//  This main function declares an object of type SortedList which is
//  a derived class from the STL list.
#include <iostream>
#include "sortedlist.h"
using namespace std;

void func(int& x)  // function to be passed to the traverse method
{
   cout << x << ' ';
}

void func2(const SortedList<int>& y)
{
   cout << "indexing, const reference: ";
   for (int i=0; i<y.size(); i++)
      cout << y[i] << ' ';
   cout << endl;
}

int main()
{
   SortedList<int> x;
   x.insert(5); // insert item into the sorted list
   x.insert(7);
   x.insert(9);
   x.insert(12);
   x.insert(3);
   x.insert(9);
   x.insert(17);
   x.insert(2);
   x.insert(9);
   cout << "original list: ";
   x.traverse(func);  // pass a pointer to a function to traverse entire list
   
   cout << "\n---------\n";
   if (x.empty())   // check to see if list is empty
      cout << "list is empty\n";
   else
      cout << "list is not empty\n";
   cout << "first: " << x.front() << endl; // return the first in list
   cout << "last: " << x.back() << endl;  // return the last in list
   cout << "size: " << x.size() << endl;  // return the number of items 
   int searchKey = 7;
   if (x.inList(searchKey))   // check to see if an item is in the list
      cout << searchKey << " is in the list\n";
   else
      cout << searchKey << " is not in the list\n";
   searchKey = 8;
   if (x.inList(searchKey))   // check to see if an item is in the list
      cout << searchKey << " is in the list\n";
   else
      cout << searchKey << " is not in the list\n";
   searchKey = 9;
   cout << searchKey << " is in the list " << x.count(searchKey) << " times\n";
   cout << 8 << " is in the list " << x.count(8) << " times\n";
   cout << "---------\n";
   x.erase(7);  // removes the first occurance
   x.remove(9);  // removes all occurances
   cout << "updated list: ";
   x.traverse(func);
   cout << "\n---------\n";
   
   cout << "output list with getNextItem: ";
   x.reset();     // resets the list to begin a traversal
   while (!x.endOfList())  // returns true if entire list has been traversed
      cout << x.getNextItem() << ' ';  // return next item in the traversal
   cout << endl;
   x.erase(88);  // no error
   x.remove(88); // no error
   cout << "indexing: ";
   for (int i=0; i<x.size(); i++)
      cout << x[i] << ' ';
   cout << endl;
   cout << "---------\n";
   searchKey = 7;
   x.insert(searchKey);
   x.insert(searchKey);
   x.insert(searchKey);
   x.insert(searchKey);
   cout << "list with a bunch of 7's: ";
   x.traverse(func);
   cout << endl;
   int position = x.index(searchKey);  // index of first occurrence or -1
   while (position != -1)
   {
      cout << x[position] << " found at position " << position << endl;
      position = x.index(position+1,searchKey); // start search at 1st arg
   }
   x.remove(searchKey);
   cout << searchKey << " removed: ";
   x.traverse(func);
   cout << "\n---------\n";
   func2(x);
   cout << "---------\n";
   SortedList<int> y;
   y = x;
   x.clear();   // empty the list
   cout << "x is now empty, see?: ";
   x.traverse(func);
   cout << "\nassignment to y worked, see?: ";
   y.traverse(func);
   cout << "\n---------\n";
   x.insert(7);
   x.insert(14);
   x.insert(3);
   x.insert(8);
   cout << "new x list: ";
   x.traverse(func);
   cout << endl;
   cout << "y list: ";
   y.traverse(func);
   x.merge(y);  // merge SortedList y into SortedList x
   cout << "\nx as a merged list: ";
   x.traverse(func);
   cout << endl;
   return 0;
}

