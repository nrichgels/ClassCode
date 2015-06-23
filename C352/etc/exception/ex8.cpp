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
   try
   {
      while (true)
      {
         p=new int[1000000000];
         cout << "allocated 1 billion ints\n";
      }
   }
   catch (bad_alloc error)
   {
      cout << "allocation exception - " << error.what() << endl;
   }
   return 0;
}
