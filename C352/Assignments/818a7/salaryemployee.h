#ifndef __SALARYEMPLOYEE_H__
#define __SALARYEMPLOYEE_H__

#include "employee.h"
#include <string>
#include <iostream>
using namespace std;

class SalaryEmployee : public Employee
{
public:
   // Constructor
   // Creates a SalaryEmployee object with the given name, Date of birth, 
   //  social security number, employee ID number, and salary.
   explicit SalaryEmployee( const string&, const Date&, const string&, const int&, const double&);
   
   // Sets the salary of the SalaryEmployee object.
   // preconditions: SalaryEmployee object has been intiialzed,
   //                first argument is a legal double.
   // postconditions: the SalaryEmployee's salary is set to given double.
   void setSalary(const double& Salary);
   
   // Returns the salary of the SalaryEmployee object
   // preconditions: SalaryEmployee object has been initialized
   // postconditions: the SalaryEmployee object's salary has been returned.
   double getSalary() const;
   
   // Inserts SalaryEmployee's name, employee ID, salary into the given 
   //  ofstream.
   // Preconditions: SalaryEmployee has been initialized, ofstream is given,
   //                ofstream has a valid file open.
   // Postcondition: SalaryEmployee's name, employee ID, and salary are
   //                inserted into the ofstream.
   void output1(ofstream& out) const;
   
   // Inserts Name, Social Security, Birthdate, and age into the given ofstream
   // Preconditions: SalaryEmployee as been initialized. ofstream is given,
   //                ofstream has a valid file open.
   // Postconditions: SalaryEmployee's Social Security, Birthdate, and age are
   //                 inserted into the ofstream.
   void output2(ofstream& out) const;
private:
   double salary;
}; //End SalaryEmployee class

#endif