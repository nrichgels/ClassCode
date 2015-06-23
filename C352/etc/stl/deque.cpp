#include <iostream>
#include <iterator>
#include <deque>
using namespace std;

int main()
{
   deque<int> q;
   ostream_iterator<int> screen(cout, " ");
   q.push_front(8);
   q.push_back(12);
   q.push_front(14);
   q.push_back(6);
   copy (q.begin(),q.end(),screen);
   cout << endl;
   cout << "---------\n";
   cout << q.size() << endl;
   cout << "---------\n";
   while (!q.empty())
   {
      cout << q.front() << ' ';
      q.pop_front();
   }
   cout << endl;
   cout << "---------\n";
   cout << q.size() << endl;
   return 0;
}
