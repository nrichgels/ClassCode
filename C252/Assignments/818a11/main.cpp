#include <iostream>
#include <iomanip>
using namespace std;
#include <fstream>
#include "prototypes.h"
#include "constants.h"

int main (int argc, char* argv[])
{
   ifstream in1;
   ifstream in2;
   in1.open(argv[1]);
   in2.open(argv[1]);
   ofstream out;
   out.open(argv[2]);

   if(CorrectFileAmount(argc))
     {while(!in2.eof())
        {outPalindrome(in2, out);
         if(palindrome(in1))
            out << "is a palindrome!";
         else
            if(!in1.eof())
               out << "is not a palindrome.";}}
   else
      {cout << "This program should have two additional files on command"
         << " line." << endl << "The User entered " << argc -1 << " additional"
         << " file(s) on command line." << endl;};

   in1.close();
   in2.close();
   out.close();
   return 0;
}
