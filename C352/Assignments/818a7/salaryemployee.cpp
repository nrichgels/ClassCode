#include "salaryemployee.h"
#include "employee.h"

#include <iomanip>
#include <string>
#include <iostream>
using namespace std;

SalaryEmployee::SalaryEmployee( const string& Name, const Date& BirthDate,
           const string& SocialSecurity, const int& EmployeeID, const double& Salary)
                        : Employee(Name, BirthDate, SocialSecurity, EmployeeID)
{
   salary = Salary;
}//End Constructor

void SalaryEmployee::setSalary( const double& Salary )
{
   salary = Salary;
}//End setSalary

double SalaryEmployee::getSalary() const
{
   return salary;
}//End getSalary

void SalaryEmployee::output1(ofstream& out) const
{
   out << left << setw(28) << getName() << setw(8) << getEmployeeId() << setw(17) << " " <<  getSalary() << endl;
}//End output

void SalaryEmployee::output2(ofstream& out) const
{
   out << left << setw(28) << getName() << setw(14) << getSS() << setw(12) << getBirthDate() 
   << getBirthDate().getAge() << endl;
}//End output2