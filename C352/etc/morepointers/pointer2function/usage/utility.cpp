// This file contains utility functions that really don't do
// anything except output a message indicating they are executing.
// One of these four functions will be pointed to by the
// UtilityFunction member in the Person class.

#include <iostream>
using namespace std;

void function1()
{
   cout << "executing utility function 1\n";
}

void function2()
{
   cout << "executing utility function 2\n";
}

void function3()
{
   cout << "executing utility function 3\n";
}

void function4()
{
   cout << "executing utility function 4\n";
}

