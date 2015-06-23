// ex12.cpp

/* Since the runtime_error exception is derived from the base class
   exception, the catch for the exception will always execute and
   not the runtime_error, even though the runtime_error exception
   was thrown.  Therefore, careful ordering is sometimes necessary. */

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
   catch (exception)
   {
      cout << "I'm in the exception catch\n";
   }
   catch (runtime_error error) 
   {
      cout << "I'm in the runtime_error catch\n";
   }

   cout << "execution continues after the catch block\n";
   return 0;  // terminate normally

}  // end main

