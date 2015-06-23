#include <iostream>
#include "base.h"
#include "derived.h"
using namespace std;

int main()
{
   Base b1(5);
   Derived d1(3,6);
   Base* bp;
   Derived* dp;
   bp = &b1;
   bp->print();
   dp = &d1;
   dp->print();
   cout << "-----------\n";
   bp = &d1;
   bp->print();
//   dp = &b1;  // error.
   return 0;
}
