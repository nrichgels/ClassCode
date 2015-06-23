#include <iostream>
using namespace std;

namespace space1
{
   void out();
}

namespace space2
{
   void out();
}

int main()
{
   {
      using namespace space1;
      out();
   }
   {
      using namespace space2;
      out();
   }
   return 0;
}

void space1::out()
{
   cout << "namespace space1\n";
}

void space2::out()
{
   cout << "namespace space2\n";
}
