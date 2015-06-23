#include <iostream>

using namespace std;

int main()
{
   int *p;
   p=new int[10];
   cout << "allocated 10 ints\n";
   for (int i=0; i<10; i++)
      p[i] = (i+1) * 10;
   for (int i=0; i<10; i++)
      cout << p[i] << ' ';
   cout << endl;
   delete [] p;
   p = NULL;
   return 0;
}
