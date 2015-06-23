#include <iostream>

using namespace std;

int* func()
{
   int *temp;
   temp=new int(8);
   return temp;
}

void swappointers(int* &x, int *&y)
{
   int *temp;
   temp=x;
   x=y;
   y=temp;
}

int main()
{
   int *p1=new int(5);
   int *p2;
   p2=func();
   cout << "p1 points to " << *p1 << endl;
   cout << "p2 points to " << *p2 << endl << endl;
   swappointers(p1,p2);
   cout << "p1 now points to " << *p1 << endl;
   cout << "p2 now points to " << *p2 << endl;
   delete p1;
   delete p2;
   p1 = NULL;
   p2 = NULL;
   return 0;
}
