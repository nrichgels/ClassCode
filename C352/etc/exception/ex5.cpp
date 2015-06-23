// ex5.cpp 

/* This shows an example using the standard exception class range_error. 
   Note that when the exception is caught, the class method what() is
   used to output the message. */

#include <iostream>
#include <stdexcept>

using namespace std;

double divide(double num1,double num2) throw (range_error)
{
   if (num2 == 0)
      throw range_error("exception: division by 0");
   if (num1 < 0)
      throw range_error("exception: numerator must be >= 0");
   if (num2 < 0)
      throw range_error("exception: denominator must be >= 0");
   return num1/num2;
}
   
int main()
{
   double number1;
   double number2;
   double result;

   cout << "Enter positive two numbers: ";
   cin >> number1 >> number2;
   
   try 
   {
      result = divide(number1,number2);
      cout << "The quotient is: " << result << endl;
   }
   catch (range_error error) 
   {
      cout << error.what() << endl;
   }

   cout << "execution continues after the catch block\n";
   return 0;  // terminate normally

}  // end main

