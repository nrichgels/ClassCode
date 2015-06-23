#ifndef __EMPLOYEE_H__
#define __EMPLOYEE_H__

#include "person.h"
#include <string>
#include <iostream>
#include <fstream>
using namespace std;

class Employee: public Person
{
public:
   // Constructor
   // Creates an Employee object with given name, birth date, Social Security number, and ID
   explicit Employee(const string& name,const Date& BirthDate, const string& SocialSecurity,const int& EmployeeId);
   
   // Constructor
   // Creates an employee object with no valid members
   explicit Employee();
   
   // Method sets the Employee's id number
   // preconditions: Employee is initialized, an integer is passed.
   // postconditions: employee has a valid id number
   void setEmployeeId(const int&);
   
   // Method retrieves employee ID
   // preconditions: employee is initialized and has been given an id number
   // postconditions: employee id number is returned
   int getEmployeeId() const;
   
   // Virtual method that is used to reveal information in inherited classes.
   virtual void output1(ofstream& out) const=0;
   
   // Virtual method that is used to reveal information in inherited classes.
   virtual void output2(ofstream& out) const=0;
private:
   int employeeId;
};//end class Eployee

#endif