#ifndef __EMPLOYEES_H__
#define __EMPLOYEES_H__

#include "employee.h"
#include "hourlyemployee.h"
#include "salaryemployee.h"
#include <string>
using namespace std;

const int MAX = 100;
class Employees
{
public:
   //Constructor
   //Initializes an empty Employees object
   explicit Employees();
   
   // Stores a pointer to an employee (or a class that has inherited an employee
   // preconditions: Employee class has been initialized,
   //                first paramater's type is inherited from an employee.
   // postconditions: The employee object is stored.
   void insert(Employee*);
   
   // Uses the output methods of all employee-inherited classes, and passes
   //   any output to the file "payroll" in this directory.
   // preconditions: output methods are correctly overloaded.
   // postconditions: file payroll is written out.
   void dump() const;
private:
   Employee* employeePointers[MAX];
   int count;
   int iterator;
}; //End class Employees

#endif