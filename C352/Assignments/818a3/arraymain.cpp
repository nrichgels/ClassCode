#include <iostream>
#include "array.h"
using namespace std;
using namespace ArrayNameSpace;
const int endindex=3;
const int startindex=-3;

int main()
{
   Array<char> array('J','N');
   array['J'] = 'H';
   array['K'] = 'E';
   array['L'] = 'L';
   array['M'] = 'L';
   array['N'] = 'O';
   for (char c='J'; c<='N'; c++)
      cout << array[c];
   cout << endl;
   cout << "-------------\n";

   Array<int> numbers(startindex,endindex);

   for (int i=startindex; i<=endindex; i++)
      numbers[i] = i*10;
   for (int i=startindex; i<=endindex; i++)
      cout << "numbers[" << i << "] = " << numbers[i] << endl;

   cout << "-------------\n";
   Array<int> numbers2;  // the array has no locations
   numbers2.Resize(10);
   numbers2[0] = 88;

   numbers2 = numbers;
   for (int i=startindex; i<endindex; i++)
      cout << "numbers2[" << i << "] = " << numbers2[i] << endl;

   cout << "-------------\n";
   if (numbers == numbers2)
      cout << "Yeah Buddy!\n";
   else
      cout << "If you see this, your program has problems!!!\n";

   numbers2[startindex]=99;
   if (numbers < numbers2)
      cout << "Yeah Buddy!\n";
   else
      cout << "If you see this, your program has problems!!!\n";
// obviously you are to overload all the relational operators


   cout << "-------------\n";
   enum DaysOfWeek {Mon, Tue, Wed, Thu, Fri, Sat, Sun};

   Array<double> hoursWorked(Mon,Fri);
   hoursWorked[Mon] = 8;
   hoursWorked[Tue] = 8;
   hoursWorked[Wed] = 10;
   hoursWorked[Thu] = 10;
   hoursWorked[Fri] = 8;
   int total=0;
   for (DaysOfWeek day=Mon; day<=Fri; day=static_cast<DaysOfWeek>(day+1))
      total += hoursWorked[day];
   cout << "You worked " << total << " hours this week.  Good job!!!\n";
   cout << endl;
   return 0;

}
