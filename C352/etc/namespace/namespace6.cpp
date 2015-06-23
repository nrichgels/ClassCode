#include <iostream>
using namespace std;

namespace ns
{
   int x=5;
}

namespace // unnamed namespace
{
   int y=10;
}

int main()
{
   int z=15;
   int y=20;
   cout << ns::x << endl;
   cout << ::y << endl;  // use the unnamed namespace variable y
   cout << z << endl;
   cout << y << endl;    // by default, uses the global namespace y
   return 0;
}

/*
     named namespace     global namespace    unnamed namespace
     ---------------     ----------------    -----------------
     std                 main                y
        cout             z
        endl             y
        etc.
     ns
        x
*/
