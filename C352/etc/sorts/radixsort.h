#include <queue>
using namespace std;

int digit(int which, int val)
{
   int divisor = 1;
   for (int i=0; i<which; i++)
      divisor *= 10;
   int remainder = val%divisor;
   divisor /= 10;
   return remainder/divisor;
}

void RadixSort(int numbers[],int count)
{
   queue<int> queues[10];
   bool done=false;
   int whichdigit = 1;
   int whichqueue;
   while (!done)
   {
      done = true;
      for (int i=0; i<count; i++)
      {
         whichqueue = digit(whichdigit,numbers[i]);
         if (whichqueue != 0)
            done = false;
         queues[whichqueue].push(numbers[i]);
      }
      int j=0;
      for (int i=0; i<10; i++)
      {
         while (!queues[i].empty())
         {
            numbers[j] = queues[i].front();
            queues[i].pop();
            j++;
         }
      }
      whichdigit++;
   }
}
