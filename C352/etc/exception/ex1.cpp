// ex1.cpp

/* This shows an example of throwing a string exception */

#include <iostream>
#include <string>

using namespace std;


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
         throw string("exception: division by 0");
      result = number1/number2;
      cout << "The quotient is: " << result << endl;
   }
   catch (string error) 
   {
      cout << error << endl;
   }

   cout << "execution continues after the catch block\n";
   return 0;  // terminate normally

}  // end main

