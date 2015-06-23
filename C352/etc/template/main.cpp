#include <iostream>
using namespace std;
#include "list.h"
using namespace ListNameSpace;

void func(List<int> somelist)
{
   cout << "starting func\n";
   cout << "removed " << somelist.remove() << " in func\n";
   cout << "removed " << somelist.remove() << " in func\n";
   cout << "exiting func\n";
}

List<int> func2(List<int> anotherlist)
{
   cout << "starting func2\n";
   cout << "exiting func2\n";
   return anotherlist;
}

int main()
{
   List<int> list(20);
   list.add(45);
   list.add(36);
   list.add(43);
   func(list);
   List<int> list2;
   list2 = func2(list);
   func(list2);
   List<float> list3;  // different type not possible without a template

   return 0;
}
