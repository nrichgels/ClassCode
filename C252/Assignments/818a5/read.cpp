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


void read(EmployeeData Employees[], int& count)
{
   // Open the file data, so it can be read.
   ifstream infile;
   infile.open("data");

   // Initiate count.
   count=0;

   // Receive information about the first employee outside of the loop.
   infile >> Employees[count].Eid;
   infile.ignore(80, '\n');
   getline(infile, Employees[count].name);
   infile >> Employees[count].hours;
   infile >> Employees[count].wage;

   // Calculate gross.  If hours worked are less than or equal to 40,
   // gross is hourly wage * number of hours.
   // Otherwise, gross is 40 * number of hours + times and a half
   // for any remaining hours.
   if(Employees[count].hours<=40)
      Employees[count].gross = Employees[count].wage * Employees[count].hours;
   else
      {Employees[count].gross= (Employees[count].wage*40)+
      (Employees[count].wage*1.5*(Employees[count].hours - 40));};

   // Calculate how much fedtax is, social security, and net pay, which is
   // the gross pay subracted by the sum of the taxes.
   Employees[count].FedTax = Employees[count].gross * FED;
   Employees[count].SocSec = Employees[count].gross * SS;
   Employees[count].netpay = Employees[count].gross - (Employees[count].FedTax
   +  Employees[count].SocSec);

   // Create a while loop which repeats the same steps until the whole file is
   // read, or until the maximum number of employees is hit.
   while(!infile.eof() && count<ARRAYMAX)
     {count++;
      infile >> Employees[count].Eid;
      infile.ignore(80, '\n');
      getline(infile, Employees[count].name);
      infile >> Employees[count].hours;
      infile >> Employees[count].wage;

      if(Employees[count].hours<=40)
         Employees[count].gross = Employees[count].wage *
         Employees[count].hours;
      else
         {Employees[count].gross= (Employees[count].wage*40)+
         (Employees[count].wage*1.5*(Employees[count].hours - 40));};

      Employees[count].FedTax = Employees[count].gross * FED;
      Employees[count].SocSec = Employees[count].gross * SS;
      Employees[count].netpay = Employees[count].gross -
      (Employees[count].FedTax +  Employees[count].SocSec);};
}

