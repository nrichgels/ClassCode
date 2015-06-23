// A void pointer can point to any data type. However they cannot be
// dereferenced.  This makes sense since the compiler would not know
// how many bytes to use in the dereferencing.  Therefore, before
// using what a void pointer is pointing to, it must first be cast to
// another pointer that is pointing to a specific data type.  In the
// below example, the size of the data type is used to determine which
// type to cast another pointer to.

#include <iostream>
using namespace std;

void print(void* data, int psize)
{
   if ( psize == sizeof(char) )
   { 
      char* pchar = static_cast<char*>(data); 
      cout << *pchar << endl; 
   }
   else if (psize == sizeof(int) )
   { 
      int* pint = static_cast<int*>(data); 
      cout << *pint << endl; 
   }
}

int main ()
{
   char a = 'x';
   int b = 1602;
   print(&a,sizeof(a));
   print(&b,sizeof(b));

   char* cp;
   int* ip;
   void* vp;
   cp = &a;
   ip = &b;
   vp = cp;
   cout << *static_cast<char*>(vp) << endl;
   vp = ip;
   cout << *static_cast<int*>(vp) << endl;
   return 0;
}
