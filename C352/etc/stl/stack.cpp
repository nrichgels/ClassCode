// This program contains an example of using the STL stack.  The stack
// does not have an iterator.
#include <iostream>
#include <stack>
using namespace std;

int main()
{
   stack<int> s;
   cout << "pushing " << 3 << endl;
   s.push(3);
   cout << "pushing " << 8 << endl;
   s.push(8);
   cout << "pushing " << 2 << endl;
   s.push(2);
   cout << "pushing " << 7 << endl;
   s.push(7);
   cout << "pushing " << 5 << endl;
   s.push(5);
   cout << "stack size = " << s.size() << endl;
   cout << "stack contents\n";
   int num;
   while (!s.empty())
   {
      num = s.top();  // there is not s.pop(num);
      s.pop();
      cout << num << endl;
   }
   return 0;
}
