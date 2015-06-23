#include <ctime>
#include <iostream>
using namespace std;

bool leapyear(int year);  // must be linked into executable

int main()
{
// this section gets and output the current date and time
   tm *current;
   time_t lt;
   lt = time('\0');
   current = localtime(&lt);
   int year = current->tm_year + 1900;
   int month = current->tm_mon+1;
   int day = current->tm_mday;
   int hour = current->tm_hour;
   int minute = current->tm_min;
   int second = current->tm_sec;
   cout << "current year: " << year << endl;
   cout << "current month: " << month << endl;
   cout << "current day: " << day << endl;
   cout << "current hour: " << hour << endl;
   cout << "current minute: " << minute << endl;
   cout << "current second: " << second << endl;

// this section gets and outputs the day of the week for the current date
// (or whatever date that would be stored in month, day, and year)
// The algorithm is valid for the Gregorian calendar which began on
// September 14, 1752.
   int centuries;
   int months;
   int dayofweek;
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
   }
   dayofweek = (centuries+year%100+year%100/4+months+day)%7;

   cout << "today is ";
   switch (dayofweek)
   {
      case 0 : cout << "Sunday\n"; break;
      case 1 : cout << "Monday\n"; break;
      case 2 : cout << "Tuesday\n"; break;
      case 3 : cout << "Wednesday\n"; break;
      case 4 : cout << "Thursday\n"; break;
      case 5 : cout << "Friday\n"; break;
      case 6 : cout << "Saturday\n"; break;
   }

   return 0;
}
