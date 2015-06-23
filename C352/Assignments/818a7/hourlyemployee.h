#ifndef __HOURLYEMPLOYEE_H__
#define __HOURLYEMPLOYEE_H__

#include "employee.h"
#include "date.h"
#include <string>
#include <iostream>
using namespace std;

class HourlyEmployee : public Employee
{
public:
   // Constructor
   // Creates an HourlyEmployee object with the given Name, Date of birth, 
   //  Social Security number, employee ID, Hours Worked, and Hourly Wage
   explicit HourlyEmployee(const string&,const Date&,const string&, const int&, const int&, const double&);
   
   // Sets how many hours the Employee has worked.
   // Preconditions: HourlyEmployee object has been initialized,
   //                first paramater is a legal integer.
   // Postconditins: The hours that the HourlyEmployee has worked in recorded
   void setHoursWorked(const int&);
   
   // Sets what the hourly wage of the employee is.
   // Preconditions: HourlyEmployee object has been initialized,
   //                first paramater is a legal double.
   // Postconditions: HourlyEmployee object's hourly wage has been recorded.
   void setWage(const double&);
   
   // Returns how many Hours the HourlyEmployee object has worked.
   // Preconditions: HourlyEmployee has been initialized.
   // Postconditions: Hours have been returned.
   int getHoursWorked() const;
   
   // Returns what the wage of the hourly employee is.
   // Preconditions: HourlyEmployee has been initialized.
   // Postconditions: Hourly wage has been returned.
   double getWage() const;
   
   // Returns how much the Employee has earned with given hours.
   // Preconditions:  HourlyEmployee has been intiialized.
   // Postcondition: Resulting Pay has been returned 
   //               (wage * hours) or (wage * 40) + 1.5 * (hours - 40) * (wage)
   //                                 if hoursWorked > 40
   double calculateEarnings();
   
   // Inserts HourlyEmployee's name, employee ID, hours Worked, wage, and pay
   //  into the given ofstream.
   // Preconditions: HourlyEmployee has been initialized, ofstream is given,
   //                ofstream has a valid file open.
   // Postcondition: HourlyEmployee's name, employee ID, hours worked, wage
   //                and pay are inserted into the ofstream.
   void output1(ofstream& out) const;
   
   // Inserts Name, Social Security, Birthdate, and age into the given ofstream
   // Preconditions: HourlyEmployee as been initialized. ofstream is given,
   //                ofstream has a valid file open.
   // Postconditions: HourlyEmployee's Social Security, Birthdate, and age are
   //                 inserted into the ofstream.
   void output2(ofstream& out) const;
private:
   double paycheck() const;
   int hoursWorked;
   double wages;
}; //End HourlyEmployee class
#endif