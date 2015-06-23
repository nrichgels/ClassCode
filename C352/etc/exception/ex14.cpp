// ex14.cpp

/* This shows an example of rethrowing an exception.  In this case
   a different object (in this case string) is thrown.  */

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
      cout << "in the divide function catch, string is: " << error << endl;
      throw string("something else");  // rethrow the exception
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
      cout << "in the main function catch, string is: " << error << endl;
   }

   cout << "execution continues after the catch block\n";
   return 0;  // terminate normally

}  // end main

