#include <iostream>
using namespace std;

typedef void (*fptr)(void);
// Let's parse the syntax of the above typedef.  The syntax is:
// typedef ReturnType (*FunctionPointer) (ParameterList);
// The syntax declares the name FunctionPointer as something that
// can store the address of any function whose return type is
// ReturnType, and whose arguments match those in ParameterList.
// In the actual typedef above, the newly created type name is 
// fptr that is a pointer to a function that returns void and takes 
// no arguments.

void func1()
{
   cout << "hello";
}

void func2()
{
   cout << " there\n";
}

void execute(fptr x)
{
   x();
}

int main()
{
   fptr f;
   f=func1;
   f();             // call to func1
   f=func2;
   f();             // call to func2
   execute(func1);
   execute(f);      // execute function takes pointer to func2
}
