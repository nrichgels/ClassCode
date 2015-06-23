#include <iostream>

using namespace std;

int main()
{
   int numbers[] = {54,23,65,99,35};
   for (int i=0; i<5; i++)
      cout << numbers[i] << ' ';
   cout << endl;
   int *p;
   p=numbers;
   for (int i=0; i<5; i++)
      cout << p[i] << ' ';
   cout << endl;
   for (int i=0; i<5; i++)
      cout << *p++ << ' ';
   cout << endl;
   cout << p[-3] << endl;
   cout << endl;
   return 0;
}
