// This is an example of a pointer to a templated function.
// The pointer can point to a function that returns void and takes
// a single argument of the templated type.

#include <iostream>
using namespace std;

template<class T>
struct FunctionPointer
{
   typedef void (*fptr)(T);
};

void func(int num)
{
   cout << num << endl;
}

void func2(double num)
{
   cout << num << endl;
}

struct example
{
   int x;
   double y;
};

void func3(example e)
{
   cout << e.x << ' ' << e.y << endl;
}

int main()
{
   FunctionPointer<int>::fptr f1;
   f1 = func;
   f1(3);
   FunctionPointer<double>::fptr f2;
   f2 = func2;
   f2(53.32);
   FunctionPointer<example>::fptr f3;
   f3 = func3;
   example x; x.x=23; x.y=43.23;
   f3(x);
   return 0;
}

