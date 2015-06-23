#include "hourlyemployee.h"
#include <string>
#include <iostream>
#include <iomanip>
using namespace std;

HourlyEmployee::HourlyEmployee( const string& Name, const Date& BirthDate, const string& SocialSecurity,
                                    const int& EmployeeID, const int& HoursWorked, const double& Wage) : Employee(Name, BirthDate, SocialSecurity, EmployeeID)
{
   hoursWorked = HoursWorked;
   wages = Wage;
}//End constructor

void HourlyEmployee::setHoursWorked(const int& HoursWorked)
{
   hoursWorked = HoursWorked;
}//End setHoursWorked

void HourlyEmployee::setWage(const double& Wages)
{
   wages = Wages;
}//End setWage

int HourlyEmployee::getHoursWorked() const
{
   return hoursWorked;
}//End getHoursWorked

double HourlyEmployee::getWage() const
{
   return wages;
}//End getWage

double HourlyEmployee::paycheck() const
{
   if( getHoursWorked() <= 40 )
   {
      return( getHoursWorked() * getWage() );
   }
   else
   {
      return( (40 * getWage()) + ((getHoursWorked() - 40) * 1.5 * getWage()) );
   }//End else
}//End paycheck

void HourlyEmployee::output1(ofstream& out) const
{
   out << left << setw(28) << getName() << setw(8) << getEmployeeId() << setw(8) << getHoursWorked() << setw(9) 
   << getWage() << paycheck() << endl;
}//End outupt()

void HourlyEmployee::output2(ofstream& out) const
{
   out << left << setw(28) << getName() << setw(14) << getSS() << setw(12) << getBirthDate() 
   << getBirthDate().getAge() << endl;
}//End output2