#include <iostream>

using namespace std;

int main()
{
   int *p;
   p=new int;
   *p = 7;
   cout << *p << endl;
   delete p;
   cout << *p << endl;  // dangling pointer (points to unallocated memory)
   p = NULL;
   return 0;
}
