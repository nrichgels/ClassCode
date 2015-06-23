// ex6.cpp

/* This shows an example of the standard exception class out_of_range.
   This is different from the previous examples because as you can see,
   there is no throw in this code.  That means the substr string
   function throws the exception. */

#include <iostream>
#include <string>
#include <stdexcept>

//using namespace std;
using std::cout;
using std::endl;
using std::string;
using std::out_of_range;
using std::length_error;

int main()
{
   string s = "hello there";

   try 
   {
      cout << s.substr(18,5) << endl;
   }
   catch (out_of_range error) 
   {
      cout << "out_of_range exception - " << error.what() << endl;
   }

   cout << "execution continues after the catch block\n";
   return 0;  // terminate normally

}  // end main

