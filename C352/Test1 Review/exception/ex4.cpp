// ex4.cpp

/* This shows an example of throwing a runtime_error exception.
   The runtime_error exception class is derived class from the
   exception class found in stdexcept.  See the README for the
   hierarchy of C++ exception classes.  All exception classes
   have a what() method that returns the C string thrown to it. */

#include <iostream>
#include <stdexcept>

using namespace std;

double divide(double num1,double num2) throw (runtime_error)
{
   if (num2 == 0)
      throw runtime_error("exception: division by 0");
   return num1/num2;
}
   
int main()
{
   double number1;
   double number2;
   double result;

   cout << "Enter two numbers: ";
   cin >> number1 >> number2;
   
   try 
   {
      result = divide(number1,number2);
      cout << "The quotient is: " << result << endl;
   }
   catch (runtime_error error) 
   {
      cout << error.what() << endl;
   }

   cout << "execution continues after the catch block\n";
   return 0;  // terminate normally

}  // end main

