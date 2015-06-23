#include <iostream>
using namespace std;

namespace space1
{
   void out()
   {
      cout << "namespace space1\n";
   }
}

namespace space2
{
   void out()
   {
      cout << "namespace space2\n";
   }
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

