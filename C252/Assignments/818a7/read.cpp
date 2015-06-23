// Author: Nathan Richgels
// File: main.cpp
// Date: 2/23/2012
// Class: CSIS252
// Assignment 5

#include <fstream>
#include <iostream>
#include <string>
using namespace std;
#include "structs.h"
#include "constants.h"
#include "employee.h"


void read(Employee Employees[], int& count)
{
   // Open the file data, so it can be read.
   ifstream infile;
   infile.open("data");

   // Initiate count.
   count=0;
   int mutator0;
   float mutator1;
   string mutator2;

   // Receive information about the first employee outside of the loop.
   infile >> mutator0;
   Employees[count].setID(mutator0);

   infile.ignore(80, '\n');
   getline(infile, mutator2);
   Employees[count].setName(mutator2);

   infile >> mutator1;
   Employees[count].setHours(mutator1);
   infile >> mutator1;
   Employees[count].setWage(mutator1);


   // Create a while loop which repeats the same steps until the whole file is
   // read, or until the maximum number of employees is hit.
   while(!infile.eof() && count<ARRAYMAX)
     {count++;
      infile >> mutator0;
      Employees[count].setID(mutator0);
      infile.ignore(80, '\n');
      getline(infile, mutator2);
      Employees[count].setName(mutator2);
      infile >> mutator1;
      Employees[count].setHours(mutator1);
      infile >> mutator1;
      Employees[count].setWage(mutator1);};

   if (!infile.eof())
      cout << "Employee limit reached." << endl;

}

