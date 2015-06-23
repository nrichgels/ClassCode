#include <iostream>

using namespace std;

class example
{
   public:
      example()
         {}
      int getx()
         {return x;}
      float gety()
         {return y;}
      void setx(int n)
         {x=n;}
      void sety(float n)
         {y=n;}
   private:
      int x;
      float y;
};

int main()
{
   example *p=new example[10];
   for (int i=0; i<10; i++)
   {
      p[i].setx(i);
      p[i].sety(i*10);
   }
   for (int i=0; i<10; i++)
      cout << p[i].getx() << ' ' << p[i].gety() << endl;
   cout << endl;

   example *p2;
   p2=p;
   for (int i=0; i<10; i++)
   {
      cout << p2->getx() << ' ' << p2->gety() << endl;
      p2++;
   }
   cout << endl;
   delete [] p;
   p = NULL;

   p=new example;
   p->setx(3);
   p->sety(5.72);
   cout << p->getx() << ' ' << p->gety() << endl;
   delete p;
   p = NULL;
   return 0;
}
