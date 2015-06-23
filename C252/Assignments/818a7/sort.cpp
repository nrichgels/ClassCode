//Use the provided sort function to rewrite the array into something that is ordered.
#include <iostream>
#include <iomanip>
using namespace std;
#include "employee.h"

void sort(Employee numbers[], int n)
{
   Employee temp;
   int small;
   for (int i=0; i<n-1; i++)  // put n-1 ints in their correct spot
      {small=i;
      for (int j=i+1; j<n; j++)  // loop to find the smallest
         if (numbers[j]!=numbers[small])
         {if (numbers[j] < numbers[small])
            small=j;
      temp = numbers[i];
      numbers[i] = numbers[small];
      numbers[small] = temp;}
         else
            {if (numbers[j].ID() < numbers[small].ID())
            small=j;
         temp = numbers[i];
         numbers[i] = numbers[small];
         numbers[small] = temp;};};
}

