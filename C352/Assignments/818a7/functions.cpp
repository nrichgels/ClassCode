#include <fstream>
#include <iostream>
#include <string>
#include "hourlyemployee.h"
#include "salaryemployee.h"
#include "prototypes.h"

using namespace std;

void read(ifstream &in, Employees& employees)
{
   string someName;
   Date someDate;
   string someSS;
   int someID;
   char someChar;
   int someSalary;
   int someHours;
   SalaryEmployee *salaryPointer;
   HourlyEmployee *hourlyPointer;
   
   getline(in, someName);
   while(!in.eof() )
   {
      in >> someDate;
      in.ignore(80, '\n');
      getline(in, someSS);
      in >> someID;
      in.ignore(80, '\n');
      in >> someChar;
      in.ignore(80, '\n');
      
      if( someChar== 'S')
      {
         in >> someSalary;
         in.ignore(80, '\n');
         salaryPointer = new SalaryEmployee(someName, someDate, someSS, someID, someSalary);
         employees.insert( salaryPointer );
      }//End if statement
      
      if( someChar == 'H' )
      {
         in >> someHours;
         in.ignore(80, '\n');
         in >> someSalary;
         in.ignore(80, '\n');
         hourlyPointer = new HourlyEmployee(someName, someDate, someSS, someID, someHours, someSalary);
         employees.insert( hourlyPointer );
      }//End if statement
      getline(in, someName);
   }//End while loop
   
   in.close();
   employees.dump();
}//End read


bool openFiles(int argc, char *argv[], ifstream &input)
{
   if( argc != 2)
   {
      cout << "One file only please." << endl;
      return false;
   }//End if statement
   input.open(argv[1]);
   if (input.fail())
   {
      cout << "File was not able to be opened." << endl;
      return false;
   }
   return true;
}//End openFiles