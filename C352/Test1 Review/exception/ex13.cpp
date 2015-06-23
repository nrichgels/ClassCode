// ex13.cpp

/* This shows an example of rethrowing an exception.  Rethrowing an
   exception allows partial processing of an exception in one
   catch block that can be finished processing in another catch block */

#include <iostream>
#include <string>

using namespace std;


double divide(double num1,double num2) throw (string)
{
   try
   {
      if (num2 == 0)
         throw string("exception: division by 0");
      return num1/num2;
   }
   catch (string error)
   {
      cout << "in the divide function catch\n";
      throw;  // rethrow the exception
   }
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
   catch (string error) 
   {
      cout << "in the main function catch\n";
      cout << error << endl;
   }

   cout << "execution continues after the catch block\n";
   return 0;  // terminate normally

}  // end main

