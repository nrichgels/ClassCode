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

