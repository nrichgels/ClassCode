// Author: Nathan Richgels

#include <fstream>
#include <iostream>
using namespace std;

// The function Read will fill the memory inserts of the array.
// It will also update count to equal one more than the number of indexes in the array.
// Finally, by telling the function how many places there are in the array, it will  assure
// that the array won't overload.
void Read(ofstream& ofile, int array[], int places, int& count)
{
   ifstream infile;
   infile.open("data");

   int Sentinel; // The user's most recent input.
   count=0;  // Number of inputs in the array.

   // prompt the user, and also tell them how much input they can place.
   infile >> Sentinel;

   // Now, as long as the user doesn't enter the sentinel or completely fill the array,
   // the prompt will be repeated.
   while ((places-count)>0 && !infile.eof())
     {array[count]=Sentinel;
      infile >> Sentinel;

      // Whatever the user's most recent number is, it will be placed in the first available spot.
      // The spot that the next value is entered into is then increased by 1. 
      count++;};

   // If the user stops entering input because the array is full, explain to the user what happened.
   if (places-count==0)
     {ofile << "Ran out of space.  Array is now full." << endl;};

   infile.close();
}
