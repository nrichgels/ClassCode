#include <iostream>
#include <iterator>
#include <queue>
using namespace std;

int main()
{
   priority_queue<int> q;  // maintained in greatest order
   q.push(8);
   q.push(12);
   q.push(14);
   q.push(6);
   while (!q.empty())
   {
      cout << q.top() << ' ';
      q.pop();
   }
   cout << endl;
   return 0;
}
