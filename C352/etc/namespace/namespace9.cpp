#include <iostream>
using namespace std;

namespace outer
{
   int x = 55;
   int y = 66;
   namespace inner
   {
      int x = 555;
      int y = 666;
   }
}

int main()
{
   int x = 5;
   int y = 6;
   cout << x << endl;
   cout << y << endl;
   cout << outer::x << endl;
   cout << outer::y << endl;
   cout << outer::inner::x << endl;
   cout << outer::inner::y << endl;
   using namespace outer;
   cout << x << endl;      // found in global namespace
   cout << y << endl;      // found in global namespace
   cout << inner::x << endl;
   cout << inner::y << endl;
   using namespace inner;
   cout << x << endl;      // found in global namespace
   cout << y << endl;      // found in global namespace
   cout << outer::x << endl;
   cout << outer::y << endl;
   cout << inner::x << endl;
   cout << inner::y << endl;
   return 0;
}
