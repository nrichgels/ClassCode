#include <iostream>

namespace outer
{
   int x=5;
   namespace inner
   {
      int y = 10;
   }
}

int main()
{
   using std::cout;
   cout << outer::x << std::endl;
   cout << outer::inner::y << std::endl;
   using namespace outer;
   cout << x << std::endl;
   cout << inner::y << std::endl;
   using namespace inner; // or using namespace outer::inner;
   cout << y << std::endl;
   return 0;
}
