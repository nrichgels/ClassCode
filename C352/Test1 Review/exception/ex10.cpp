// ex10.cpp

/* This shows an example of a user defined exception class. */

#include <iostream>
#include <string>

using namespace std;

class DivisionByZero
{
   public:
      char* what()
      {
         return "Division by zero error";
      }
};

int main()
{
   double number1;
   double number2;
   double result;

   cout << "Enter two numbers: ";
   cin >> number1 >> number2;
   
   try
   {
      if (number2 == 0)
         throw DivisionByZero();
      result = number1/number2;
      cout << "The quotient is: " << result << endl;
   }
   catch (DivisionByZero error) 
   {
      cout << error.what() << endl;
   }

   cout << "execution continues after the catch block\n";
   return 0;  // terminate normally

}  // end main

