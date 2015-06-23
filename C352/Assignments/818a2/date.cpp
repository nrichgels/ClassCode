#include <iostream>
#include <iomanip>
#include <string>
#include <ctime>
#include "date.h"
#include <sstream>

using namespace std;
using namespace DateNameSpace;

/*********************************Functions***********************************
 ****************************************************************************/
namespace DateNameSpace
{
bool leapyear(int Year)
{
      if((Year/100)*100==Year)
      {
         if((Year/400)*400==(Year))
            {return 1;}
         else
            {return 0;}
         
      }//End if((Year/100)*100==Year)
   else
   {
       if(Year/4==(Year+3)/4)
          return 1;
       else
          return 0;
   }//end else
}//End leapyear

int centuryLeapYear(int Year)
{
   if((Year/100)*100==Year)
      {if((Year/400)*400==(Year))
         {return 1;}
       else
        {return 0;}}
   else
     {return 2;}
}//End function centuryLeapYear

bool validDay(int Month, int Day, int Year) throw (DateException)
{
   if(Month==4 || Month==6 || Month==9 || Month==11)
   {
      if (Day>=1 && Day<=30)
         return 1;
      else
         throw DateException( "exception: Date is not within the given month's range of days." );
   }

   if(Month==1 || Month==3 || Month==5 || Month==7 || Month==8
                                     || Month==10 || Month==12)
   {
      if (Day>=1 && Day<=31)
         return 1;
      else
         throw DateException( "exception: Date is not within the given month's range of days." );
   }

   if(Month==2)
   {
       if(centuryLeapYear(Year)==1)
       {
          if (Day>=1 && Day<=29)
             return 1;
        
          else
             throw DateException( "exception: Date is not within the given month's range of days." );
       }//end if(centuryLeapYear(Year)==1)   

       if(centuryLeapYear(Year)==0)
       {
          if(Day>=1 && Day<=28)
             return 1;
          else
             throw DateException( "exception: Date is not within the given month's range of days." );
       }//End if(centuryLeapYear==0
        
       if(centuryLeapYear(Year)==2)
       {
          if(Year/4==(Year+3)/4)
          {
             if(Day>=1 && Day<=29)
                return 1;
             else
                throw DateException( "exception: Date is not within the given month's range of days." );
          }//End if(Year/4==(Year+3)/4)
          else 
          {
             if(Day>=1 && Day<=28)
                return 1;
             else
                throw DateException( "exception: Date is not within the given month's range of days." );
          }//End else
       };//End if(centuryLeapYear(Year==2))
   }//End if(Month==2)

   else
      throw DateException( "exception: A valid month has not been given." );
}//End function validDay

bool validDayBool(int Month, int Day, int Year)
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
}//End validDayBool



/*********************************DateException*******************************
 *********************************Class Methods*******************************/
DateException::DateException(const string& m)
{
   msg = m;
}

string DateException::what()
{
   return msg;
}

/*************************************Date************************************
 *********************************Static Members******************************/
formatType Date::currentFormat = NUMERIC;
arithmeticType Date::currentArithmetic = DAYS;



/*************************************Date************************************
 *********************************Class Methods*******************************/
Date::Date(const int& inMonth, const int& inDay, const int& inYear)
{
   if(validDay(inMonth, inDay, inYear))
   {
      month = inMonth;
      day = inDay;
      year = inYear;
   } //End validDay
}//End Constructor
   
Date::Date()
{
   setToday();
}//End Constructor

void Date::setDate(const int& inMonth, const int& inDay, const int& inYear)
{
   if(validDay(inMonth, inDay, inYear))
   {
      month = inMonth;
      day = inDay;
      year = inYear;
   }// End validDay
}//End setDate

Date Date::Today()
{
   /*stringstream converter;
   tm *current;
   time_t lt;
   lt = time('\0');
   current = localtime(&lt);
   converter <<  current->tm_year + 1900 << ' ' << current->tm_mon+1 << ' ' << current->tm_mday;

   string dateToday = converter.str();

   return dateToday;*/
   
   Date today;
   return today;
}//End setToday

void Date::setToday()
{
   tm *current;
   time_t lt;
   lt = time('\0');
   current = localtime(&lt);
   year = current->tm_year + 1900;
   month = current->tm_mon+1;
   day = current->tm_mday;

}//End setToday

int Date::getMonth() const
{
   return month;
}//End getMonth

int Date::getDay() const
{
   return day;
}//End getDay

int Date::getYear() const
{
   return year;
}//End getYear

void Date::outputFormat(const formatType& type)
{
   currentFormat = type;

}//End outputFormat

string Date::getDayOfWeek() const
{
   int dayOfWeek;
   int months;
   int centuries;
   centuries = (3-year/100%4)*2;
   switch (month)
   {
      case 1  : if (leapyear(year))
                   months = 6;
                else
                   months = 0; break;
      case 2  : if (leapyear(year))
                   months = 2;
                else
                   months = 3; break;
      case 3  : months = 3; break;
      case 4  : months = 6; break;
      case 5  : months = 1; break;
      case 6  : months = 4; break;
      case 7  : months = 6; break;
      case 8  : months = 2; break;
      case 9  : months = 5; break;
      case 10 : months = 0; break;
      case 11 : months = 3; break;
      case 12 : months = 5; break;
   }//End switch block
   dayOfWeek = (centuries+year%100+year%100/4+months+day)%7;

   switch (dayOfWeek)
   {
      case 0 : return( "Sunday" );
      case 1 : return( "Monday" );
      case 2 : return( "Tuesday" );
      case 3 : return( "Wednesday" );
      case 4 : return( "Thursday" );
      case 5 : return( "Friday" );
      case 6 : return( "Saturday" );
   }//End switch block
}//End getDayOfWeek

string Date::getMonthString() const
{
   switch (month)
   {
      case 1 : return( "January" );
      case 2 : return( "February" );
      case 3 : return( "March" );
      case 4 : return( "April" );
      case 5 : return( "May" );
      case 6 : return( "June" );
      case 7 : return( "July" );
      case 8 : return( "August" );
      case 9 : return( "September" );
      case 10 : return( "October" );
      case 11 : return( "November" );
      case 12 : return( "December" );
   }//End switch
}//End getMonth



/***************************************Date**********************************
 *********************************Operator overloads**************************/
bool Date::operator==(const Date& date) const
{
   return( (getDay() == date.getDay()) && (getMonth() == date.getMonth()) && (getYear() == date.getYear()) );
}//End operator overload ==

const Date Date::operator++()
{
   //If the user of the class is incrememinting by Days:
   if(currentArithmetic == DAYS)
   {
      //If the next day in the month and year exists, increment the day
      if(validDayBool(month, day+1, year)
      {
            day = day +1;
            return *this;
      }//end validDay if statement
      
      //else, if the next month in the year exists, put the value of day to 1,
      //and increment the month
      else if(validDayBool(month+1, 1, year)
      {
         day = 1;
         month = month + 1;
      }//End elif validDay statement
      
      //else, if the next month doesn't exist within the year, increment the year
      //and put the value of day and month to 1
      else if(validDayBool(1, 1, year+1)
      {
         month = 1;
         day = 1;
         year = year +1;
      }//End elif validDay statement
   }//End if currentArithmetic if statement



   //If the user of the class is incrementing by months:
   if(currentArithmetic == MONTHS)
   {
      //if one month from now is a valid day, increment by one month
      if( validDayBool(month +1, day, year)
      {
         month = month + 1;
      }//End validDayBool if statement

      //if the next month in the year doesn't exist, set the month to 1 and increment
      //the year.
      else if( (month +1) == 13 )
      {
         month = 1;
         year++;
      }//End month+1 elif statement

      //else, if the current day doesn't exist next month, subtract the day until
      //the day of next month does exist.  And then increment the month.
      else 
      {
         while(!validDayBool(month+1, day, year)
         {
            day--;
         }//End while loop
         month++;
      }//End else statement
   }//End currentArithmetic if statement


   //If the user of the class is incrementing by years:
   if(currentArithmetic == YEARS)
   {
      //if the next year falls on a valid date, increment the year
      if( validDayBool(month, day, year+1))
      {
         year++;
      }//End if validDayBool statement
      
      //else, decrement the day and increment the year
      else
      {
         day--;
         year++;
      }//End else statement
   }//End currentArithmetic statement
}//End operator++ overload 

void Date::operator=(const string& dateIn)
{
int i;
   stringstream converter;

   int tempYear;
   int tempMonth;
   int tempDay;

   converter << dateIn;
   converter >> year;
   converter >> month;
   converter >> day;   
}//End opeartor= overload

/*****************************************************************************
 *********************************Ostream overloads***************************/
ostream& operator<<(ostream& out, const Date& obj)
{
   if( Date::currentFormat == NUMERIC )
      out << obj.getMonth() << '/' << obj.getDay() << '/' << obj.getYear();
   
   if( Date::currentFormat == FULLNUMERIC )
      out << obj.getDayOfWeek() << ", " << obj.getMonth() << '/' << obj.getDay() << '/' <<obj.getYear();
      
   if( Date::currentFormat == TEXT )
      out << obj.getMonthString() << ' ' << obj.getDay() << ", " << obj.getYear();
   
   if( Date::currentFormat == FULLTEXT )
      out << obj.getDayOfWeek() << ", " << obj.getMonthString() << ' ' << obj.getDay() << ", " <<obj.getYear();
   return out;
}//End ostream overload for class Date

}//End DateNameSpace