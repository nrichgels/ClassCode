#include <iostream>
using namespace std;

int main()
{
   int a=59;

   int* b;
   b = &a;
   cout << *b << endl;

   int** c; // c is a pointer to a pointer
   c = &b;  // c is assigned the address of an int pointer
   cout << **c << endl; 

// ... and so on
   int*** d;
   d = &c;
   cout << ***d << endl;

   return 0;
}
