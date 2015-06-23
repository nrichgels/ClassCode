// ex2.cpp

/* This example is a mess.  It shows multiple catch blocks with different
   data types being thrown.  It also includes miscellaneous other items */

#include <iostream>
#include <string>
using namespace std;

int main()
{
   int num;
   cout << "Enter an int in range of 6 to 9: ";
   cin >> num;
   
   try 
   {
      if (num >= 1 and num <= 5)
         throw num; // same as: throw int(num);
      if (num == 0)
         throw 2.83; // same as: throw double(2.83);
      if (num >= 10 && num<20)
         throw char('X');  // same as: throw 'X';
      if (num >= 100)
         throw "hello there"; // throw a C string (array of char)
      if (num < 0)
         throw string("error: negative input");
      if (num >= 20 && num < 100)
         throw short();  // this example does not throw a value
   }
   catch (int error)
   {
      cout << "in int catch block, ";
      switch (error)
      {
         case 1 : cout << "error code 1\n"; break;
         case 2 : cout << "error code 2\n"; break;
         case 3 : cout << "error code 3\n"; break;
         case 4 : cout << "error code 4\n"; break;
         case 5 : cout << "error code 5\n"; break;
      }
   }
   catch (string error)
   {
      cout << "in string catch block, string = " << error << endl;
   }
   catch (char) // no variable so can't use the thrown char 'X'
   {
      cout << "in char catch block\n";
   }
   catch (const char* error)
   {
      cout << "in c-string catch block, c-string = " << error << endl;
   }
   catch (double error)
   {
      cout << "in double catch block, double = " << error << endl;
   }
   catch (short)
   {
      cout << "in short catch block" << endl; 
   }
   catch(...)  // catch anything else, must be the last catch block
   {
      cout << "in ... catch block\n";
   }

   cout << "execution continues after the catch block\n";
   return 0;  // terminate normally

}  // end main

