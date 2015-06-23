#include "employee.h"
#include <string>
#include <iostream>
using namespace std;

Employee::Employee(const string& name, const Date& BirthDate, const string& SocialSecurity, const int& EmployeeID)
                                          : Person(name, BirthDate, SocialSecurity)
{
   employeeId = EmployeeID;
}//End Constructor

Employee::Employee()
{
   
}//End Constructor

void Employee::setEmployeeId(const int& EmployeeID)
{
   employeeId = EmployeeID;
}//End setEmployeeId

int Employee::getEmployeeId() const
{
   return employeeId;
}
