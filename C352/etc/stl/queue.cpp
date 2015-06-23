// This program contains an example of using the STL queue.  The STL 
// queue has push and pop rather than unique names for the queue 
// insert and delete.  The queue does not have an iterator.
#include <iostream>
#include <queue>
using namespace std;

int main()
{
   queue<int> q;
   cout << "enqueueing " << 3 << endl;
   q.push(3);
   cout << "enqueueing " << 8 << endl;
   q.push(8);
   cout << "enqueueing " << 2 << endl;
   q.push(2);
   cout << "enqueueing " << 7 << endl;
   q.push(7);
   cout << "enqueueing " << 5 << endl;
   q.push(5);
   cout << "queue size = " << q.size() << endl;
   cout << "queue contents\n";
   int num;
   while (!q.empty())
   {
      num = q.front();
      q.pop();
      cout << num << endl;
   }
   return 0;
}
