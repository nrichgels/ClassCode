// ex9.cpp

/* This shows an example of throwing a range_error or overflow_error. 
   What would happen if we got rid of the try and catch blocks? */

#include <iostream>
#include <string>
#include <stdexcept>

using namespace std;

int factorial(int n) throw (range_error,overflow_error)
{
   if (n<0)
      throw range_error("range_error: n must be positive for n!");
   int result=1;
   for (int i=1; i<=n; i++)
   {
      result *= i;
      if (result <= 0)
         throw overflow_error("overflow_error: n too large for n!");
   }
   return result;
}

int main()
{
   int num;
   cout << "Enter an int: ";
   cin >> num;
   
   try 
   {
      cout << num << "! = " << factorial(num) << endl;
   }
   catch (range_error error) 
   {
      cout << error.what() << endl;
   }
   catch (overflow_error error) 
   {
      cout << error.what() << endl;
   }

   cout << "execution continues after the catch block\n";
   return 0;  // terminate normally

}  // end main

