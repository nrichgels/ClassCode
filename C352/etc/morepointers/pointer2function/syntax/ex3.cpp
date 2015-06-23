#include <iostream>
using namespace std;

typedef int (*fptr)(int);
// The above typedef creates a type name fptr, that returns an int
// and has an int pass by value argument.  An object of type
// fptr can store the address of any function whose return type is
// int, and has an int pass by value argument.

int add1(int x)
{
   return x+1;
}

int add2(int x)
{
   return x+2;
}

int add(fptr fname,int y)
{
   int temp=fname(y);
   return temp;
}

int main()
{
   int result;
   int num=4;
   fptr f;
   f=add1;
   result=f(num);  // call to add1
   cout << "result = " << result << endl;
   f=add2;
   result=f(num);  // call to add2
   cout << "result = " << result << endl;

   result=add(f, num); // add function takes pointer to add2
   cout << "result = " << result << endl;
   result=add(add1,num);  // add function calls add1
   cout << "result = " << result << endl;
   result=add(add2,num);  // add function calls add2
   cout << "result = " << result << endl;
}
