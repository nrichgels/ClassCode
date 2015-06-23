// This program contains an example of using the STL list.  An iterator
// is needed for many of the list operations.  An iterator is similar to
// a pointer to a location in the list.
#include <iostream>
#include <list>
using namespace std;

int main()
{
   list<int> mylist;
   list<int>::iterator i;
   cout << "the biggest the list can be is "
        << mylist.max_size() << " ints\n";
   i=mylist.begin();
   if (mylist.empty())
       cout << "list is empty\n";
   else
       cout << "there are " << mylist.size() << " items in the list\n";

// each of the following inserts is at the beginning of the list
   i=mylist.insert(i,5);
   i=mylist.insert(i,7);
   i=mylist.insert(i,2);
   for (i=mylist.begin(); i!=mylist.end(); i++)
       cout << *i << endl;
   cout << "-------------\n";
// insert each of the following at the end of the list
   i=mylist.end();
   i=mylist.insert(i,9);
   i=mylist.end();
   i=mylist.insert(i,4);
   i++;  // move i to the end
   i=mylist.insert(i,3);
   for (i=mylist.begin(); i!=mylist.end(); i++)
       cout << *i << endl;
   cout << "-------------\n";
// erase the 1st and last item in the list
   i=mylist.begin();
   mylist.erase(i);
   i=mylist.end(); // i points to one item past the end of the list
   i--;  // i points to the last item in the list
   i=mylist.erase(i);
   for (i=mylist.begin(); i!=mylist.end(); i++)
       cout << *i << endl;
   cout << "-------------\n";
// remove 9 from the list
   mylist.remove(9);
// sort the list
   mylist.sort();
   for (i=mylist.begin(); i!=mylist.end(); i++)
       cout << *i << endl;
   cout << "-------------\n";
   if (mylist.empty())
       cout << "list is empty\n";
   else
       cout << "there are " << mylist.size() << " items in the list\n";
   cout << "-------------\n";
   i = mylist.begin();
   for (int x = 0; x < mylist.size(); x++)
      cout << *i++ << endl;
   return 0;
}
