#include <iostream>
using namespace std;

namespace first
{
   int x=5;
}
namespace second
{
   int x=10;
}

namespace first   // extend namespace first
{
   int y = 15;
}

int main()
{
   {
      using namespace second;
      cout << x << endl;
   }
   {
      using namespace first;
      cout << x << endl;
      cout << y << endl;
   }
   return 0;
}
