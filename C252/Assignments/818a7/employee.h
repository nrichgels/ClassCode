// Author: Nathan Richgels
// File: employee.h
// Date: 3/72012
// Class: CSIS252
// Assignment 7

#ifndef _EMPLOYEE_H_
#define _EMPLOYEE_H_


class Employee
{
   public:
      // methods:

      // method - constructor
      // description - construct a new employee object.
      // precondition - none
      // postcondition - Employee object created and initialized to
      // specified ID #, Name, hours, & wage (or all 0 by default.)
      // method input - ID #, Name, hours, wage
      // mehtod output - none
      Employee(int=0, string="0", double=0, double=0);

      // method - setID
      // description - changes the Employee object's ID.
      // precondition - The employee object is initialized.
      // postcondition - The employee's ID is changed to specefied ID.
      // method input - ID: Integer
      // mehtod output - none
      void setID(int);

      // method - ID
      // description - Returns the int value of the Employee object's ID.
      // precondition - Employee object has been initialized
      // postcondition - Employee object's ID is returned
      // method input - None
      // method output - ID: Integer
      int ID();

      // method - setName
      // description - Changes the Employee object's Name.
      // precondition - Employee object has been initialized
      // postcondition - Employee object's name is changed to specefied Name.
      // method input - Name: String
      // method output - none
      void setName(string);

      // method - Name
      // description - Returns the string value of the Employee object's Name.
      // precondition - Employee Object has been initialized
      // postcondition - Employee Object's name has been returned.
      // method input - None
      // method output - Name: String
      string Name();

      // method - setWage
      // description - Changes the Employee object's hourly wage.
      // precondition - Employee object has been initialized.
      // postcondition - Employee object's hourly wage is changed to specefied
      //                 wage.
      // method input - Wage: Double
      // method output - none
      void setWage(double);

      // method - Wage
      // description - Returns the hourly wage of the employee
      // precondition - Employee object has been initialized.
      // postcondition - Employee object's hourly wage is returned.
      // method input - none
      // method output - Wage: Double
      double Wage();

      // method - setHours
      // description - Changes the employee's hours worked.
      // precondition - Employee object has been initialized.
      // postcondition - Employee object's hours has been changed to specefied
      //                 hours.
      // method input - Hours: Double
      // method output - none
      void setHours(double);

      // method - Hours
      // description - Returns the Hours worked of the Employee object.
      // precondition - Employee object has been initialized.
      // postcondition - Employee object's hours have been returned.
      // method input - none
      // method output - Hours: Double
      double Hours();

      // method - Gross
      // description - Returns the total gross of the Employee object.
      // precondition - Employee object has been initialized.
      // postcondition - Employee object's gross have been returned.
      // method input - none
      // method output - Gross: Double
      double Gross();

      // method - Fedtax
      // description - Returns the Fed Tax witheld of the Employee object.
      // precondition - Employee object has been initialized.
      // postcondition - Employee object's Fed Tax witheld have been returned.
      // method input - none
      // method output - Fedtax: Double
      double Fedtax();

      // method - Socsec
      // description - Returns the Social security witheld of the Employee
      //               object.
      // precondition - Employee object has been initialized.
      // postcondition - Employee object's Social Security tax witheld have 
      //                 been returned.
      // method input - none
      // method output - Socsec: float
      double Socsec();

      // method - Net
      // description - Returns the Gross minus the tax of the Employee object.
      // precondition - Employee object has been initialized
      // postcondition - Employee object's Net wage has been returned.
      // method input - none
      // method output - Net: float.
      double Net();

      // operator overloads:
      bool operator==(const Employee& other) const;
      bool operator>=(const Employee& other) const;
      bool operator>(const Employee& other) const;
      bool operator<=(const Employee& other) const;
      bool operator<(const Employee& other) const;
      bool operator!=(const Employee& other) const;

   private:
      int EID;      //corresponds to ID & setID methods
      string name;  //corresponds to Name & setName methods, and operator overloads.
      double hours; //corresponds to Hours & setHours methods
      double wage;  //corresponds to Wage & setWage methods
      double gross; //corresponds to Gross method
      double fedtax;//corresponds to Fedtax method
      double socsec;//corresponds to Socsec method
      double net;   //corresponds to Net method
};

#endif
