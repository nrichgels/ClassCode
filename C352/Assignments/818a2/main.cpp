// File:      main.cpp
// Author:    Dan Brekke

// This file contains the main function that shows what should compile
// for program 2.

#include <iostream>
#include <iomanip>
#include <string>
#include "date.h"
using namespace std;
using namespace DateNameSpace;

int main()
{

/*************** AT MINIMUM, GET THIS STUFF TO WORK FIRST ******************/
/*************** IT CAN BE TURNED IN FOR 50% CREDIT ******************/

   Date d1;  // initialized to the current date
   cout << d1 << endl;  // default format is NUMERIC, 1/29/2013
   Date::outputFormat(TEXT); 
   cout << d1 << endl;  // January 29, 2013
   Date::outputFormat(FULLTEXT); 
   cout << d1 << endl;  // Tuesday, January 29, 2013
   Date::outputFormat(NUMERIC); 
   cout << d1 << endl;  // 1/29/2013
   Date::outputFormat(FULLNUMERIC); 
   cout << d1 << endl;  // Monday, 1/29/2013

// Your Date class should throw exceptions whenever a possible error
// could occur

   try
   {
      d1.setDate(13,5,2000);
   }
   catch (DateException error)
   {
      cout << error.what() << endl;
      cout << "    d1 is still " << d1 << endl;
   }

   try
   {
      d1.setDate(2,29,1999);
   }
   catch (DateException error)
   {
      cout << error.what() << endl;
      cout << "    d1 is still " << d1 << endl;
   }

   d1.setDate(4,15,2000);
   cout << d1 << endl;;

   Date d2;
   Date d3(1,1,1);
   d3.setDate(7,20,1969);
   cout << d3.getMonth() << '-' << d3.getDay() << '-' << d3.getYear() << endl;
   Date d4(11,11,2011);
   d3 = Date::Today();
   d4.setToday();
   if (d2==d3 && d2==d4 && d3==d4)
      cout << "That's right, they're all equal\n";
   else
      cout << "my program has problems";
// Overload all relational operators

   Date LincolnBirthday(2,12,1809);
   Date LincolnDeath;
   LincolnDeath.setDate(4,15,1865);
   cout << "Abraham Lincoln was born on a "
        << LincolnBirthday.getDayOfWeek() << " and died on a "
        << LincolnDeath.getDayOfWeek() << ".\n";


/*************** NEXT LEVEL FOR 25% MORE CREDIT ******************/
  
   cout << "----------------------------------------------------------\n";
   Date today; // current date
   d2 = today;
   cout << d2 << endl;
   d3 = d2++;
   cout << d2 << endl;
   cout << d3 << endl;
   d3 = ++d2;
   cout << d2 << endl;
   cout << d3 << endl;
   d2--;
   d3 = --d2;
   cout << d2 << endl;
   cout << d3 << endl;


/*************** NEXT LEVEL FOR 25% MORE CREDIT ******************/


/*   cout << "----------------------------------------------------------\n";
   Date::Arithmetic(YEARS);  // the default is DAYS
   Date FluxCapacitor(11,5,1955);  // November 5, 1955
   cout << "Dr. Emmett L. Brown conceived the possibility of time travel "
        << today-FluxCapacitor << " years ago\n";
   cout << "Dr. Emmett L. Brown conceived the possibility of time travel "
        << Date::Today()-FluxCapacitor << " years ago\n";
   cout << "Abraham Lincoln lived to be " 
        << LincolnDeath-LincolnBirthday << " years old\n";
// if the object occurs after the argument, the result is negative        
   cout << "Abraham Lincoln was born " 
        << LincolnBirthday-LincolnDeath
        << " years after his death\n";
//return 0;

   cout << "Abraham Lincoln would be "
        << today-LincolnBirthday << " years old right now\n";
   Date::Arithmetic(DAYS);
   cout << "Abraham Lincoln lived " 
        << LincolnDeath-LincolnBirthday << " days\n";
// if the object occurs after the argument, the result is negative        
   cout << "Abraham Lincoln was born " 
        << LincolnBirthday - LincolnDeath << " days after his death\n";
   cout << "Abraham Lincoln died " 
        << today-LincolnDeath << " days ago\n";
   cout << "It's " << LincolnBirthday.daysUntil() // the year doesn't matter
        << " days until Abraham Lincoln's birthday.\n";

   cout << "d2 is " << d2 << endl;
   Date::Arithmetic(DAYS);
   d2++;  // add 1 day
   Date::Arithmetic(YEARS);
   d2++;  // add 1 year
   ++d2;  // add 1 year
   cout << "d2 is now " << d2 << endl;
   if (d2 > d3)  
      cout << "Yes\n";  // Yes, since d2 occurs after d3
   else
      cout << "my program has problems";
   d3 = d2--;  // subtract 1 year from d2, d3 is the original value of d2
   Date::Arithmetic(DAYS);
   --d2;  // subtract 1 day
   cout << "d2 is now " << d2 << endl;
   cout << "d3 is " << d3 << endl;
   
   d3.setDate(7,20,1969);
   d2 = d3;
   Date::Arithmetic(DAYS);
   d3 = d3 + 7;  // add 7 days
   cout << "d3 is now " << d3 << endl;
   d3 = d3 - 7;  // subtract 7 days
   cout << "d3 is now " << d3 << endl;
   Date::Arithmetic(YEARS);
   d3 = d3 + 10;  // add 10 years
   cout << "d3 is now " << d3 << endl;
   cout << "d2 is " << d2 << endl;
   int num;
   num = d3-d2;
   cout << "num is " << num << endl;
   d2++;
   num = d3-d2;
   cout << "num is " << num << endl;
   num = d2-d3;
   cout << "num is " << num << endl;
   Date::Arithmetic(DAYS);
   num = d3-d2;
   cout << "num is " << num << endl;

// Arithmetic that doesn't make sense
//   d2 = d3+d4;
//   d2 = d3*d4;
//   d2 = d3/d4;
//   d2 = d3%d4;

*/
/********************************* BONUS *********************************/

/*   cout << "*************************** BONUS!!! ************************\n";
   Date::Arithmetic(MONTHS);
   cout << "d3 is " << d3 << endl;
   d3++;
   cout << "d3 is now " << d3 << endl;
   d3 = d3 + 11;
   cout << "d3 is now " << d3 << endl;
   --d3;
   cout << "d3 is now " << d3 << endl;
   d3.setDate(1,31,2000);
   cout << "d3 is " << d3 << endl;
   d3++;
   cout << "d3 is now " << d3 << endl;

   d1.setDate(12,31,2005);
   d2.setDate(1,1,2006);
   cout << "d1 = " << d1 << "   d2 = " << d2 << endl;
   cout << "d2 - d1 = " << d2-d1 << endl; // should be 0
   Date::Arithmetic(DAYS);
   d2=d2+29;  // add 29 days making is 1/30/2006
   Date::Arithmetic(MONTHS);
   cout << "d2 - d1 = " << d2-d1 << endl; // should be 0
   Date::Arithmetic(DAYS);
   d2++;

   Date::Arithmetic(MONTHS);
   cout << "d1 = " << d1 << "   d2 = " << d2 << endl;
   cout << "d2 - d1 = " << d2-d1 << endl; // should be 1
   cout << "d1 - d2 = " << d1-d2 << endl; // should be -1
   d2.setDate(1,31,2006);
   d1.setDate(3,28,2006);
   cout << "d1 = " << d1 << "   d2 = " << d2 << endl;
   cout << "d1 - d2 = " << d1-d2 << endl; // should be 1
   cout << "d2 - d1 = " << d2-d1 << endl; // should be -1
*/
   return 0;
}
