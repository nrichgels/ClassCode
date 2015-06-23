// Author: Nathan Richgels
// File: employee.cpp
// Date: 3/72012
// Class: CSIS252
// Assignment 7

#include <iostream>
#include <iomanip>
using namespace std;
#include "employee.h"
#include "constants.h"


// Class methods
Employee::Employee(int ID, string Name, double Hours, double Wage)
{
   setID(ID);
   setName(Name);
   setHours(Hours);
   setWage(Wage);
}

void Employee::setID(int ID)
{
   EID=ID;
}

int Employee::ID()
{
   return EID;
}

void Employee::setName(string Name)
{
   name=Name;
}

string Employee::Name()
{
   return name;
}

void Employee::setWage(double Wage)
{
   wage=Wage;
}

double Employee::Wage()
{
   return wage;
}

void Employee::setHours(double Hours)
{
   hours=Hours;
}

double Employee::Hours()
{
   return hours;
}

double  Employee:: Gross()
{
   if (hours<=40)
      gross=hours*wage;
   else
      gross=(wage*40) + (wage * (hours-40)*1.5);
   return gross;
}

double Employee:: Fedtax()
{
   fedtax=Gross()*fedrate;
   return fedtax;
}

double Employee::Socsec()
{
   socsec=Gross()*socrate;
   return socsec;
}

double Employee::Net()
{
   net=Gross()-(Socsec()+Fedtax());
   return net;
}

//Overloaded operators:
bool Employee::operator==(const Employee& other) const
{
   return (name==other.name);
}

bool Employee::operator>=(const Employee& other) const
{
   return name>=other.name;
}

bool Employee::operator>(const Employee& other) const
{
   return name>other.name;
}

bool Employee::operator<=(const Employee& other) const
{
   return name<=other.name;
}

bool Employee::operator<(const Employee& other) const
{
   return name<other.name;

}

bool Employee::operator!=(const Employee& other) const
{
   return name!=other.name;
}
