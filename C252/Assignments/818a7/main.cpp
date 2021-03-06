// Author: Nathan Richgels
// Sort function provided by: Dan Brekke
// File: main.cpp
// Date: 3/72012
// Class: CSIS252
// Assignment 7

#include <iostream>
#include <iomanip>
using namespace std;
#include "employee.h"
#include "structs.h"
#include "constants.h"
#include "prototypes.h"

int main()
{
   Employee Employees[ARRAYMAX];
   SummaryData summary;
   int count;

   read(Employees, count);
   sort(Employees, count);
   summary=Summary(Employees, count);
   outputData(Employees, count, summary);
   return 0;
}
