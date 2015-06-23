#include <iostream>
using namespace std;

typedef void (*fptr)(int&);
// The above typedef creates a type name fptr, that returns void
// and has an int pass by reference argument.  An object of type
// fptr can store the address of any function whose return type is
// void, and has an int pass by reference argument.

void add1(int&x)
{
   x=x+1;
}

void add2(int&x)
{
   x=x+2;
}

// This function has arguments of a pointer to a function and a
// pass by reference int argument that either add1 or add2 requires.
// By calling x(y), this function will call either add1 or add2.
void add(fptr x,int& y)
{
   x(y);
}

int main()
{
   int num=4;
   fptr f;
   f=add1;
   f(num);  // call to add1
   cout << "num = " << num << endl;
   f=add2;
   f(num);  // call to add2
   cout << "num = " << num << endl;

   add(f, num); // add function takes pointer to add2
   cout << "num = " << num << endl;
   add(add1, num); // add function calls add1
   cout << "num = " << num << endl;
   add(add2, num); // add function calls add2
   cout << "num = " << num << endl;
}
