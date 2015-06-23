#include <iostream>

using namespace std;

int main()
{
   int x=6;
   int y=27;
   int* p;
   p=&x;
   cout << *p << endl;
   *p=17;
   cout << x << endl;
   cout << "the address of x is:      " << &x << endl;
   cout << "p is pointing at address: " << p << endl;
   return 0;
}
