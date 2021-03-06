// ex8.cpp

/* This shows an example of throwing a bad_alloc exception after
   dynamic memory is exhausted. */

#include <iostream>
#include <string>
#include <stdexcept>

using namespace std;


int main()
{
   int *p;
   int i = 0;
   try
   {
      while (true)
      {
         p=new int[1000000000];
         cout << "allocated 1 billion ints\n";
	 i++;
      }
   }
   catch (bad_alloc error)
   {
      cout << "allocation exception - " << error.what() << endl;
   }

   cout << "Allocated " << (i * 1000000000) << " billion ints." << endl;
   return 0;
}
