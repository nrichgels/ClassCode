// Author: Nathan Richgels
// File: person.cpp
// Date: 3/28/2012
// Class: CSIS252
// Assignment 9
#include "date.h"
#include "itemtype.h"
#include <iostream>
#include <iomanip>
using namespace std;

Person::Person(string Name, Date BirthDate)
{
   bdate = BirthDate;
   name = Name;
}

Person::Person()
{}

void Person::setBirthdate(int month, int day, int year)
{
   bdate.setDate(month, day, year);
}

Date Person::Birthdate() const
{
   return bdate;
}

void Person::setName(string Name)
{
   name=Name;
}

string Person::Name() const
{
   return name;
}

int Person::getAge()
{
   int YrsOld;
   current.now();
   if(current.getMonth()<bdate.getMonth())
      YrsOld = current.getYear() - bdate.getYear()-1;
   else
     {if(current.getMonth()==bdate.getMonth())
        {if(current.getDay() >= bdate.getDay())
            YrsOld = current.getYear() - bdate.getYear();
         else
            YrsOld = current.getYear() - bdate.getYear()-1;}
      else
        {if(current.getMonth() > bdate.getMonth())
            YrsOld = current.getYear() - bdate.getYear();};};

   return YrsOld;
}

bool Person::operator==(const Person& other) const
{
   if(other.Name()==Name())
     {return(other.bdate==bdate);}

   else
      {return false;};
}

istream& operator>>(istream& in, Person& person)
{
   int MONTH, DAY, YEAR;
   char SLASH;
   in >> MONTH;
   in.ignore(1, '/');
   in >> DAY;
   in.ignore(1, '/');
   in >> YEAR;
   person.setBirthdate(MONTH, DAY, YEAR);
   return in;
}

ostream& operator<<(ostream& out, Person& person)
{
   out << left << setw(26) <<  person.Name()
   << right << setw(3) << person.getAge();
   return out;
}
