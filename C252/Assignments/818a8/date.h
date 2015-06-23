// Author: Nathan Richgels
// File: date.h
// Date: 3/22/2012
// Class: CSIS252
// Assignment 8
#ifndef __DATE_H__
#define __DATE_H__
class Date
{
   public:
      //Methods:

      // Method - constructor
      // description - Constructs a new Date object
      // precondition - none
      // postcondition - Date object is created and has a valid 
      //                 calendar date.
      // method input - int month, day, year
      // method output - none
      Date(int month=1, int day=1, int year=2000);

      // Method - getMonth
      // description - Returns month in the date object.
      // precondition - The date object has been initialized
      // postcondition - The month integer has been returned
      // method input - none
      // method output - month: int
      int getMonth() const;

      // Method - getYear
      // description - Returns year in the date object.
      // precondition - The date object has been initialized
      // postcondition - The year integer has been returned
      // method input- none
      // method output- year: int
      int getYear() const;

      // Method - getDay
      // description- returns day in the date object.
      // precondition - The date object has been inititalized
      // postcondition - The day integer has been returned
      // method input- none
      // method output - year: int
      int getDay() const;

      // Method - setMonth
      // description - sets the 'day' of the date object
      // preconditions - the date object has been initialized
      //               - the new 'month'int is greater than 0 or
      //                 less than 12.
      // postcondition - The 'month' of the object is updated as
      //                 specefied.
      // method input - month: int
      // method output - none
      void setMonth(int month);

      // Method - setyear
      // description - sets the 'year' of the date object
      // precondition - The date object has been initialized
      // postcondition - The 'year' of the object is updated
      //                 as specefied.
      // method input: year: int
      // method output: none
      void setYear(int year);

      // Method - setDay
      // description - sets the 'day' of the date object
      // preconditions - The date object has been initialized
      //               - The day exists within a month of the
      //                 society's currently used calendar.
      // postcondition - The 'day' of the object is updated as
      //                 specefied.
      // method input: day: int
      // method output: none
      void setDay(int day);

      // Method: setDate
      // description - sets the 'day', 'month', or 'year' of the
      //               date object.
      // preconditions - The date object has been initialized
      //               - The month and day exists within society's
      //                 currently used calendar.
      // postcondition - The 'month', 'day', and 'year' of the object
      //                 is updated as specefied.
      void setDate(int month, int day, int year);

      //Operator Overloads:
      bool operator== (const Date& other) const;
      bool operator>= (const Date& other) const;
      bool operator<= (const Date& other) const;
      bool operator>  (const Date& other) const;
      bool operator<  (const Date& other) const;
      bool operator!= (const Date& other) const;

   private:
      int m;
      int d;
      int y;
};

// Functions:

// function - centuryLeapYear
// description - Determines if a given year is divisible by 100. If
//               it is, it determines if the given year is
//               considered a leap year.
// precondition - none
// postcondition - Int of 1 is returned if the int given is a 
//                 'Leap Year'. Int of 0 is returned if a given year
//                 is an 'even century', & 2 is returned if a given
//                 year isn't a 'Leap Year' or 'Even Century'.
// input - year: int
// output - int
int centuryLeapYear(int Year);

// function - validDay
// description - Returns true if a date exists. If a date doesn't
//               exist, returns false.
// precondition - none
// postcondition - Determines if a given date exists or doesn't exist
// input - Month: int, Day: int, Year: int
bool validDay(int Month, int Day, int Year);

// Stream Operator Overloads:
ostream& operator<<(ostream& out, const Date&);
istream& operator>>(istream& in, Date&);
#endif
