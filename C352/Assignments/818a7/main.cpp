#include "employees.h"
#include "hourlyemployee.h"
#include "salaryemployee.h"
#include "date.h"
#include "prototypes.h"

#include <iostream>
#include <fstream>
#include <string>
using namespace std;

//WRITE THE READEME
//DOCUMENT ALL .H FILES(INCLUDING DATE'S GETAGE FUNCTION
//TURN IN AND REAP REWARDS

int main(int argc,char *argv[])
{
   ifstream in;
   Employees employees;
   
   if( openFiles( argc, argv, in) )
   {
      read(in, employees);
   }
  /* HourlyEmployee Nathan("Nathan Richgels", Date(6, 8, 1993), "394-42-1248", 88888, 50, 7.25);
   SalaryEmployee Aragorn("Aragorn", Date(2, 14, 1942), "698-538-0201", 94323, 250000);
   SalaryEmployee Gimli("Gimli", Date(11, 25, 2000), "218-731-4913", 20410, 8000);
   HourlyEmployee Legolas("Legolas", Date( 9, 27, 1322 ), "740-34-9088", 12098, 47, 19.35);
   
   Employees employees;
   
   employees.insert(&Nathan);
   employees.insert(&Aragorn);
   employees.insert(&Gimli);
   employees.insert(&Legolas);
   employees.dump1();*/
}//End main