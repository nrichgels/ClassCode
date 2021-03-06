#include <fstream>
#include <iostream>
using namespace std;

// Finds and reports the middle term, or if there is no middle term, groups the centermost two
// terms together, then averages and reports them.
void median(ofstream& outfile, int Array[], int filledIndex)
{
   int even,     // Boolean- could be true or false, if true, there are an even amount of spots taken up in the array.
       count,    // The number of spots taken up in the given Array.
       quotient; // Slightly lower than the halfway point of the Array.


   count=filledIndex+1; //The filledIndex is how many indices there are, while count is how many spots are taken up.
   quotient=count/2;  // Half of the total number of spots taken up, rounded down if the total # of spots is an odd number.

   // Determines if the number of spots taken up is even.
   if (count>(quotient*2))
      even=0;
   else
      even=1;

   // If it is even, this method is used.
   if (even==true)
     {float Average;

      // Adds the index of one smaller than the "half way point", and one larger than the "halfway point".
      // then divided by two to get the Average.
      Average=(Array[quotient-1]+Array[quotient])/2.0;
      outfile  << "The median is "<< Average << "." << endl;};

   // If not even, this method is used.
   // If the number of places in the array is odd, when the integer is divided it's automatically rounded down,
   // which is convieniently the same index the median is in.
   if (even==false)
     {outfile << "The median is " << Array[(quotient)] << "." << endl;};
}
