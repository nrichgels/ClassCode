// Author: Nathan Richgels
// File: date.cpp
// Date: 3/22/2012
// Class: CSIS252
// Assignment 8
#include <iostream>
#include <iomanip>
using namespace std;
#include "date.h"



//Functions:
int centuryLeapYear(int Year)
{
   if((Year/100)*100==Year)
      {if((Year/400)*400==(Year))
         {return 1;}
       else
        {return 0;}}
   else
     {return 2;}
}

bool validDay(int Month, int Day, int Year)
{
   if(Month==4 || Month==6 || Month==9 || Month==11)
      return (Day>=1 && Day<=30);

   if(Month==1 || Month==3 || Month==5 || Month==7 || Month==8
                                     || Month==10 || Month==12)
      return (Day>=1 && Day<=31);

   if(Month==2)
     {if(centuryLeapYear(Year)==1)
         return (Day>=1 && Day<=29);

      if(centuryLeapYear(Year)==0)
         return (Day>=1 && Day<=28);

      if(centuryLeapYear(Year)==2)
        {if(Year/4==(Year+3)/4)
            return (Day>=1 && Day<=29);
         else 
            return (Day>=1 && Day<=28);};}

   else
      return 0;
}

//Class Methods:
Date::Date(int month, int day, int year)
{
   m=1;
   d=1;
   y=2000;
   setDate(month, day, year);

}

int Date::getMonth() const
{
   return m;
}

int Date::getDay() const
{
   return d;
}

int Date::getYear() const
{
   return y;
}

void Date::setMonth(int month)
{
   if(validDay(month, d, y))
      m=month;
   else
      cout << "Date doesn't exist in modern calendar." << endl;
}

void Date::setDay(int day)
{
   if(validDay(m, day, y))
      d=day;
   else
      cout << "Date doesn't exist in modern calendar." << endl;
}

void Date::setYear(int year)
{
   if(validDay(m, d, year))
      y=year;
   else
      cout << "Date doesn't exist in modern calendar." << endl;
}

void Date::setDate(int month, int day, int year)
{
   m=1;
   d=1;
   y=2000;
   setMonth(month);
   setYear(year);
   setDay(day);


}

//Class bool overloads:

bool Date::operator==(const Date& other) const
{
   if(y==other.y)
     {if(m==other.m)
         return d==other.d;
      else
         return m==other.m;};
   return y==other.y;
}

bool Date::operator>=(const Date& other) const
{
   if(y==other.y)
     {if(m==other.m)
         return d>=other.d;
      else
         return m>=other.m;};
   return y>=other.y;
}

bool Date::operator<=(const Date& other) const
{
   if(y==other.y)
     {if(m==other.m)
         return d<=other.d;
      else
         return m<=other.m;};
   return y<=other.y;

}

bool Date::operator<(const Date& other) const
{
   return !(*this>=other);
}

bool Date::operator>(const Date& other) const
{
   return !(*this<=other);
}

bool Date::operator!=(const Date& other) const
{
   return !(*this==other);
}

// Stream operator overloads:
ostream& operator<<(ostream& out, const Date& date)
{
   int ect=0;
   if (date.getMonth()<10)
      out<< ect << date.getMonth();
   else
      out << date.getMonth();

   out << "/";

   if (date.getDay()<10)
      out << ect <<  date.getDay() << "/" <<  date.getYear();
   else
      out << date.getDay() << "/" << date.getYear();
}

istream& operator>>(istream& in, Date& date)
{
   int MONTH, DAY, YEAR;
   char SLASH;
   in >> MONTH;
   in.ignore(1, '/');
   in >> DAY;
   in.ignore(1, '/');
   in >> YEAR;
   date.setYear(YEAR);
   date.setMonth(MONTH);
   date.setDay(DAY);
   return in;
}


