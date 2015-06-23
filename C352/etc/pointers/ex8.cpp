#include <iostream>

using namespace std;

class example
{
   public:
      example(int a, float b):x(a),y(b) 
         {}
      int getx()
         {return x;}
      float gety()
         {return y;}
   private:
      int x;
      float y;
};

int main()
{
   example n(5,7.3);
   cout << n.getx() << ' ' << n.gety() << endl;
   example *e;
   e=&n;
   cout << e->getx() << ' ' << e->gety() << endl;
//   delete e;
   e=NULL;
   e=new example(4,3.98);
   cout << e->getx() << ' ' << e->gety() << endl;
   delete e;
   e = NULL;
   return 0;
}
