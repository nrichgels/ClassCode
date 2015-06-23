// ex7.cpp

/* This shows an example of the standard exception classes out_of_range
   and length_error.  The substr function will throw a length_error
   exception if the string exceeds the maximum length.  However since the
   maximum string length is more than 4 billion chars, we can't really
   do a short (time wise) example to demonstrate this.  Therefore, I
   throw my own length_error exception. */

#include <iostream>
#include <string>
#include <stdexcept>

//using namespace std;
using std::cout;
using std::cin;
using std::endl;
using std::string;
using std::out_of_range;
using std::length_error;

int main()
{
   string s = "hello there";
   int start, len;
   cout << "enter start char and substr length: ";
   cin >> start >> len;
   try 
   {
      if (start+len > s.length() )
         throw length_error("exceeds end of string");
      // note that the above will throw a length_error exception
      // before the substr function would throw an out_of_range
      cout << s.substr(start,len) << endl;
   }
   catch (out_of_range error) 
   {
      cout << "out_of_range exception - " << error.what() << endl;
   }
   catch (length_error error)
   {
      cout << "length_error exception - " << error.what() << endl;
   }

   cout << "execution continues after the catch block\n";
   return 0;  // terminate normally

}  // end main

