#include <fstream>
#include <iostream>
using namespace std;


// Simply finds the average of every spot in the array.
void average(ofstream& outfile, int Array[], int filledIndex)

{
   int count=filledIndex+1; // Number of ints in the array.
   float sum=0; // All the ints in the array added together.

   // Get the total of every integer inside of an index of an array.  sum is a float so a more exact
   // representation of an average is achieved.
   for (int i=0; i<=filledIndex; i++)
      sum=sum + Array[i];

   // Divide the sum by the amount of spots filled in the array to get the average.
   outfile << "The average is " << sum/count << "." << endl;
}
