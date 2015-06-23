// Author: Nathan Richgels
// File: main.cpp
// Date: 2/23/2012
// Class: CSIS252
// Assignment 5

#include <iomanip>
#include <fstream>
#include <iostream>
#include <string>
using namespace std;
#include "prototypes.h"
#include "constants.h"
#include "structs.h"

// Besides initiating some variables, main brings together all of the
// functions.
int main()
{
   SummaryData Totals;  // Creates a struct that holds summed-up information
   int count;  // Keeps track of how many uses spaces in an array
   EmployeeData Employees[ARRAYMAX]; // An array that holds info on employees.

   read(Employees, count);
   Totals= Summary(Employees, count);
   outputData(Employees, count, Totals);

   return 0;
}
