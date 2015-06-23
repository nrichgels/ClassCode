// ex11.cpp

/* This shows an example of a user created exception class. 
   One of four possible exceptions could occur.  This example
   differs from ex10.cpp in that the string is stored.  */

#include <iostream>
#include <string>

using namespace std;

class DivisionError
{
   public:
      DivisionError(const string& m="")
      { msg = m; }

      string what()
      { return msg; }

   private:
      string msg;
};

double divide(double num1,double num2) throw (DivisionError)
{
   if (num2 == 0)
      throw DivisionError("exception: division by 0");
   if (num1 < 0)
      throw DivisionError("exception: numerator must be >= 0");
   if (num2 < 0)
      throw DivisionError("exception: denominator must be >= 0");
   if (num1 < num2)
      throw DivisionError("exception: numerator must be >= denominator");
   return num1/num2;
}
   
int main()
{
   double number1;
   double number2;
   double result;

   cout << "Enter two positive numbers: ";
   cin >> number1 >> number2;
   
   try 
   {
      result = divide(number1,number2);
      cout << "The quotient is: " << result << endl;
   }
   catch (DivisionError error) 
   {
      cout << error.what() << endl;
   }

   cout << "execution continues after the catch block\n";
   return 0;  // terminate normally

}  // end main

