// File:
// Author: Nathan Richgels
// Code for function "sort" provided by: Dan Brekke
// Class: CSIS 252
// Program: Proves the author has a basic understanding of arrays and functions in C++.
// Date: 1/31/2012


// The purpose of this program is array processing and proving that the author has a basic understanding of the use of functions.

#include <iostream>
using namespace std;


const int ArrayLength=30;  //The length of the central array, or any array that is a product of the original array.

//Use the provided sort function to rewrite the array into something that is ordered.
void sort(int numbers[], int n)
{
   int temp;
   int small;
   for (int i=0; i<n-1; i++)  // put n-1 ints in their correct spot
      {small=i;
      for (int j=i+1; j<n; j++)  // loop to find the smallest
         if (numbers[j] < numbers[small])
            small=j;
      temp = numbers[i];
      numbers[i] = numbers[small];
      numbers[small] = temp;}
}


// The function Read will fill the memory inserts of the array.
// It will also update count to equal one more than the number of indexes in the array.
// Finally, by telling the function how many places there are in the array, it will  assure
// that the array won't overload.
void Read(int array[], int places, int& count)
{
   int Sentinel; // The user's most recent input.
   count=0;  // Number of inputs in the array.

   // prompt the user, and also tell them how much input they can place.
   cout << "Please enter up to " << places-count << " values to enter into an Array: ";
   cin >> Sentinel;
   cout << endl;

   // If the user enters -999 before the loop, they haven't entered anything into the array.
   // Hence, we will prevent them from entering the sentinel value.
   while (Sentinel==-999)
     {cout << endl << "No values entered into Array.\nPlease enter a valid value: ";
      cin >> Sentinel;
      cout << endl;};

   // Now, as long as the user doesn't enter the sentinel or completely fill the array,
   // the prompt will be repeated.
   while ((places-count)>0 && Sentinel!=-999)
     {array[count]=Sentinel;

      // Whatever the user's most recent number is, it will be placed in the first available spot.
      // The spot that the next value is entered into is then increased by 1. 
      count++;

      // Re-prompt the user, and tell them while telling them how many times they can enter values.
      cout << "Please enter up to " << places-count << " more values or enter -999 to end: ";
      cin >> Sentinel;
      cout << endl;};

   // If the user stops entering input because the array is full, explain to the user what happened.
   if (places-count==0)
     {cout << "Ran out of space, array is now filled." << endl;};
}


// EvenOddSplit will produce 2 arrays seperating even and odd numbers.
// Much like the Read function, EvenOddSplit will also keep track of how many total entries that are in the array, and return it.
// This function assumes that the two arrays that the programmer provides enough memory set aside to place everything in each array.
// Unfortunately, to do all of these steps, the function requires a lot of input.
void EvenOddSplit(int Array[], int EvenArray[], int OddArray[], int filledIndex, int& EvenPlace, int& OddPlace)
{
   int quotient; // A value in the array divided by 2.

   EvenPlace=0;  // The count of how many even numbers there are, set at 0 before the count begins.
   OddPlace=0;   // The count of how many odd numbers tehre are, set at 0 before the count begins.

   // This process iterates for every index in the cental Array.
   for (int i=0; i<=filledIndex; i++)
     {quotient=Array[i]/2;

      // Since divisions in c++ are rounded down for integers, if you divide integer1 by intger2
      // and the quotient is multiplied again by integer2, and the result is smaller than integer1, then integer1
      // must be odd. Therefore we can put integer1 in an array for even integers only.
      if (Array[i]==quotient*2)
        {EvenArray[EvenPlace]=Array[i];
         EvenPlace++;}
      else
        {OddArray[OddPlace]=Array[i];
         OddPlace++;};};
}


// This function outputs on screen what is in each individual "slot" of an array,
// in a list-like manner.
void arrayPrint(int Array[], int filledIndex)
{
   // Place a line of tildes(~) to signal the start of the Array.
   cout << "~~~~~~~~~~~~~~~~~~~~~~~~~" << endl;

   // Make a loop that is done executing once i has taken the place of every value in the given array.
   for (int i=0; i<=filledIndex; i++)
      // For every value of i, report the value of the array at spot i in the array.
     {cout << "Array[" << i << "]-->" << Array[i] << endl;};

   // Place a line of tildes(~) to signal that the output beyond this point is not
   // a continous part of the array.
   cout << "~~~~~~~~~~~~~~~~~~~~~~~~~" << endl;
}


// Simply finds the average of every spot in the array.
void average(int Array[], int filledIndex)

{
   int count=filledIndex+1; // Number of ints in the array.
   float sum=0; // All the ints in the array added together.

   // Get the total of every integer inside of an index of an array.  sum is a float so a more exact
   // representation of an average is achieved.
   for (int i=0; i<=filledIndex; i++)
      sum=sum + Array[i];

   // Divide the sum by the amount of spots filled in the array to get the average.
   cout << "The average is " << sum/count << "." << endl;}


// Finds and reports the middle term, or if there is no middle term, groups the centermost two
// terms together, then averages and reports them.
void median(int Array[], int filledIndex)
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
      cout << "The median is "<< Average << "." << endl;};

   // If not even, this method is used.
   // If the number of places in the array is odd, when the integer is divided it's automatically rounded down,
   // which is convieniently the same index the median is in.
   if (even==false)
     {cout << "The median is " << Array[(quotient)] << "." << endl;}
}



int main()
{
   int contains[ArrayLength], // The array that will be used in, edited, and analyzed by functions.
       Even[ArrayLength], // Has all of the even integers of contains (in no particular order).
       Odd[ArrayLength],  // Has all of the odd integers of contains (in no particular order).
       EvenCount, // The number of integers in Even.
       OddCount, // The number integers in Odd.
       count; // The number of integers in contains.

   // Now, we put our variables into all of the functions that will operate them, and print out
   // meaningful resuls.
   Read(contains, ArrayLength, count);
   EvenOddSplit(contains, Even, Odd, count-1, EvenCount, OddCount);
   sort(contains, count);
   cout << "SORTED" << endl;
   arrayPrint(contains, count-1);
   cout << endl << endl;
   average(contains, count-1);
   median(contains, count-1);
   cout << endl << endl << "EVENS" << endl;
   arrayPrint(Even, EvenCount-1);
   cout << endl << endl << "ODDS" << endl;
   arrayPrint(Odd, OddCount-1);

   return 0;
}
