#include <iostream>
#include <vector>
#include <algorithm>
#include <iterator>
using namespace std;

int main()
{
   vector<int> numbers(10);
   for (int i=0; i<10; i++)
      numbers[i] = i+1;
   for (int i=0; i<10; i++)
      cout << numbers[i] << ' ' <<  numbers.at(i) << endl;
   cout << "---------\n";

   cout << "first: " << numbers.front() << endl;
   cout << "last: " << numbers.back() << endl;
   cout << "---------\n";
   
   vector<int>::iterator it;

   it = numbers.begin();
   cout << *it << endl;
   it = it+3;
   cout << *it << endl;
   it = numbers.end();
   it--;
   cout << *it << endl;
   cout << "---------\n";

   it = numbers.begin();
   while (it != numbers.end())
      cout << *it++ << ' ';
   cout << endl;
   cout << "---------\n";

   numbers.resize(20);

   it = numbers.begin();
   for (int i=0; i<numbers.size(); i++)
      cout << *it++ << ' ';
   cout << endl;

   cout << "---------\n";
   cout << "capacity: " << numbers.capacity() << endl
        << "size: " << numbers.size() << endl
        << "max_size: " << numbers.max_size() << endl;
   cout << "---------\n";

   int array[] = {5,7,9,8,2};
   copy (array,array+5,numbers.begin()); // requires #include <algorithm>
   it = numbers.begin();
   for (int i=0; i<numbers.size(); i++)
      cout << *it++ << ' ';
   cout << endl;
   cout << "---------\n";

   vector<int> numbers2(5);
   it = numbers.begin();
   it++; it++; it++;
   copy (numbers.begin(),it,numbers2.begin());  // copy first 3
   it = numbers2.begin();
   for (int i=0; i<numbers2.size(); i++)
      cout << *it++ << ' ';
   cout << endl;
   cout << "---------\n";

   it = numbers2.begin();
   it = numbers2.insert(it,12); // returns iterator to inserted item
   it = numbers2.insert(it,11);
   it++; it++;
   it = numbers2.insert(it,13);
   it = numbers2.end();
   it = numbers2.insert(it,99);
   it = numbers2.begin();
   for (int i=0; i<numbers2.size(); i++)
      cout << *it++ << ' ';
   cout << endl;
   cout << "---------\n";

   it = numbers2.begin();
   it = numbers2.erase(it);
   it = numbers2.erase(it);
   it++; it++;
   it = numbers2.erase(it);
   it = numbers2.begin();
   for (int i=0; i<numbers2.size(); i++)
      cout << *it++ << ' ';
   cout << endl;
   cout << "---------\n";

   numbers2.pop_back();
   it = numbers2.begin();
   for (int i=0; i<numbers2.size(); i++)
      cout << *it++ << ' ';
   cout << endl;
   cout << "---------\n";

   ostream_iterator<int> screen(cout, " ");
   copy (array,array+5,screen);
   cout << endl;
   cout << "---------\n";
   copy (numbers.begin(),numbers.end(),screen);
   cout << endl;
   cout << "---------\n";

   vector<int> v;
   cout << "capacity: " << v.capacity() << endl
        << "size: " << v.size() << endl
        << "max_size: " << v.max_size() << endl;
   cout << "---------\n";
   v.push_back(43);
   v.push_back(28);
   v.push_back(17);
   v.push_back(57);
//   v.push_back(36);
   for (int i=0; i<v.size(); i++)
      cout << v[i] << ' ';
   cout << endl;
   cout << "---------\n";
   cout << "capacity: " << v.capacity() << endl
        << "size: " << v.size() << endl
        << "max_size: " << v.max_size() << endl;
   return 0;
}
