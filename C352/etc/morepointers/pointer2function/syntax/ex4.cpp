// This is the same example as ex3.cpp except that the typedef
// statement is not used.  It also does not use a temp int in
// the add function.

#include <iostream>
using namespace std;

int add1(int x)
{
   return x+1;
}

int add2(int x)
{
   return x+2;
}

int add(int (*someFunction)(int),int y)
{
   return someFunction(y);
}

int main()
{
   int result;
   int num=4;
   int (*f)(int);
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
