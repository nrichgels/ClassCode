// Author: Nathan Richgels
// File: main.cpp
// Date: 2/23/2012
// Class: CSIS252
// Assignment 5

#include <iostream>
#include <string>
using namespace std;
#include "employee.h"
#include "structs.h"

SummaryData Summary(Employee Employees[], int count)
{
   double Gross=0,  // Total amount of untaxed pay.
          FedTax=0, // Total amount of federal tax.
          SS=0,  // Total amount of Social Security tax.
          Net=0; // Total amount of taxed pay.
   SummaryData Totals;  //The struct that will be returned.

   // A for loop that goes through every employee in an EmployeeData array,
   // and sums up Gross, fedtax, SS, and Netpay.
   for(int i=0; i<count; i++)
     {Gross= Gross + Employees[i].Gross();
      FedTax= FedTax + Employees[i].Fedtax();
      SS= SS + Employees[i].Socsec();
      Net= Net + Employees[i].Net();};

   // Assigns the totals to each category in the struct.
   Totals.Gross=Gross;
   Totals.FedTax=FedTax;
   Totals.SocSec=SS;
   Totals.netPay=Net;

   return Totals;
}
