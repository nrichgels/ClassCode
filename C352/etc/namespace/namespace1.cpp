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

int main()
{
   cout << second::x << endl;
   cout << first::x << endl;
   {
      using namespace second;
      cout << x << endl;
   }
   {
      using namespace first;
      cout << x << endl;
   }
   return 0;
}
