#include <iostream>

using namespace std;

struct example
{
   int x;
   float y;
};

int main()
{
   example *p;
   p=new example;
   p->x = 9;
   p->y=2.87;
   cout << p->x << ' ' << p->y << endl;
   delete p;
   p = NULL;
   return 0;
}
