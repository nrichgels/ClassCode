// This program contains an example of using the STL set.
#include <iostream>
#include <set>
#include <algorithm>
#include <iterator>
using namespace std;

int main()
{
   set<int> s; // try multiset for the below multiple 12s
   if (s.empty())
      cout << "set is empty\n";
   else
      cout << "set is not empty\n";

   s.insert(34);
   s.insert(12);
   s.insert(12);
   s.insert(12);
   s.insert(12);
   s.insert(12);
   s.insert(9);
   s.insert(5);
   s.insert(29);
   if (s.empty())
      cout << "set is empty\n";
   else
      cout << "set is not empty\n";

   set<int>::iterator i;
   i = s.find(34);
   cout << *i << endl;

   cout << s.count(12) << endl;

   cout << "---------\n";
   int num;
   num = 2;
   if (s.find(num)==s.end())
      cout << num << " is not in set\n";
   else
      cout << num << " is in set\n";
   num = 29;
   if (s.find(num)==s.end())
      cout << num << " is not in set\n";
   else
      cout << num << " is in set\n";
   
   cout << "---------\n";
   for (i=s.begin(); i!=s.end(); i++)
      cout << *i << endl;

   set<int> s2;
   for (int i=1; i<10; i++)
      s2.insert(i);

   cout << "---------\n";
   set<int> s3;

// ins is an insert iterator
   insert_iterator<set<int> > ins(s3, s3.begin());
   ostream_iterator<int> out(cout,"\n");
   set_union(s.begin(),s.end(),s2.begin(),s2.end(),ins); 
   copy(s3.begin(),s3.end(),out);
   cout << "---------\n";
   s3.clear();
// without using the declared ins insert iterator
   set_intersection(s.begin(),s.end(),s2.begin(),s2.end(),
                    inserter(s3,s3.begin())); 
   copy(s3.begin(),s3.end(),out);

   return 0;
}
