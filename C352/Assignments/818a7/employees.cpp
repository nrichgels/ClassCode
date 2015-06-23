#include "employees.h"
#include "employee.h"

#include <iomanip>
#include <fstream>
#include <string>
#include <iostream>
using namespace std;

Employees::Employees()
{
   count = 0;
   iterator = 0;
}//End Constructor

void Employees::insert(Employee *item)
{
   employeePointers[count] = item;
   count++;
}//End insert

void Employees::dump() const
{
   ofstream out;
   out.open( "payroll" );
   out << "NAME                        " << "ID #    " << "Hours   " << "Wage     " <<  "Gross Pay" << endl;
   out << "-------------------------   -----   -----   -------  ------------"<< endl;
   
   for(int i = 0; i<count; i++)
      (*employeePointers[i]).output1(out);
   out << endl;
   out.close();
   
   out.open( "employees" );
   out << "NAME                        " << "SS            " << "Birthday    " << "Age" << endl;
   out << "-------------------------   -----------   ---------   ---" << endl;
   for(int i = 0; i<count; i++)
      (*employeePointers[i]).output2(out);
   out << endl;
   out.close();
}//End method dump

