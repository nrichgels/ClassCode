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
   cout << ns::x << endl;
   cout << y << endl;
   cout << z << endl;
   return 0;
}

/*
     named namespace     global namespace    unnamed namespace
     ---------------     ----------------    -----------------
     std                 main                y
        cout             z
        endl
        etc.
     ns
        x
*/
