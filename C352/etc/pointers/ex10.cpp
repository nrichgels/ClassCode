#include <iostream>

using namespace std;

void func1(int x)
{
   cout << x << endl;
}

void func2(int* x)
{
   cout << *x << endl;
   *x = 8;
}

int main()
{
   int *p=new int(5);
   func1(*p);
   func2(p);
   cout << *p << endl;
   delete p;
   p = NULL;
   return 0;
}
