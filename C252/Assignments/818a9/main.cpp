// Author: Nathan Richgels
// File: main.cpp
// Date: 3/28/2012
// Class: CSIS252
// Assignment 9
#include <iostream>
using namespace std;
#include <iomanip>
#include <fstream>
#include "itemtype.h"
#include "arrayListType.h"

int main( int argc, char *argv[])
{
   int count=0;
   string Name;
   ifstream in;
   in.open(argv[1]);

   arrayListType BirthdayList;
   Person birthday;
   getline(in, Name);

   birthday.setName(Name);
   in >> birthday;
   in.ignore(80, '\n');
   BirthdayList.insertEnd(birthday);
   count ++;

   while(!in.eof() && count<BirthdayList.maxListSize())
     {getline(in, Name);
      birthday.setName(Name);
      if(!in.eof())
        {in >> birthday;
         in.ignore(80, '\n');
         BirthdayList.insertEnd(birthday);
         count++;};};

   if(count==BirthdayList.maxListSize())
      cout << "Wasn't able to read whole file." << endl;

   cout << left << setw(26) << "Name" << "Age" << endl;
   cout << "_________________________ ___" << endl;
   BirthdayList.print();
   in.close();

   return 0;
}
