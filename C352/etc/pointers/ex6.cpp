#include <iostream>

using namespace std;

struct example
{
   int x;
   float y;
};

int main()
{
   example a;
   a.x = 7;
   a.y = 4.82;
   cout << a.x << ' ' << a.y << endl;

   example *p;
   p=&a;
   cout << p->x << ' ' << p->y << endl;
   cout << (*p).x << ' ' << (*p).y << endl; // same as p->x and p->y
   return 0;
}
