// File:
// Author: Nathan Richgels
// Code for function "sort" provided by: Dan Brekke
// Class: CSIS 252
// Program: Proves the author has a basic understanding of arrays and functions in C++.
// Date: 1/31/2012

#include <fstream>
#include <iostream>
using namespace std;
#include "constants.h"
#include "prototypes.h"

int main()
{
   int contains[ArrayLength], // The array that will be used in, edited, and analyzed by functions.
       Even[ArrayLength], // Has all of the even integers of contains (in no particular order).
       Odd[ArrayLength],  // Has all of the odd integers of contains (in no particular order).
       EvenCount, // The number of integers in Even.
       OddCount, // The number integers in Odd.
       count; // The number of integers in contains.

   // Now, we put our variables into all of the functions that will operate them, and print out
   // meaningful results.

   ifstream infile;
   ofstream outfile;
   infile.open("data");
   outfile.open("results");

   Read(outfile, contains, ArrayLength, count);
   EvenOddSplit(contains, Even, Odd, count-1, EvenCount, OddCount);
   sort(contains, count);
   outfile << "SORTED" << endl;
   arrayPrint(outfile, contains, count-1);
   outfile << endl << endl;
   average(outfile, contains, count-1);
   median(outfile, contains, count-1);
   outfile << endl << endl << "EVENS" << endl;
   arrayPrint(outfile, Even, EvenCount-1);
   outfile << endl << endl << "ODDS" << endl;
   arrayPrint(outfile, Odd, OddCount-1);

   outfile.close();
   infile.close();

   return 0;
}
