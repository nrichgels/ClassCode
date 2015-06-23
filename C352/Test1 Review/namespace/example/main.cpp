// file: main.cpp
#include <iostream>
using namespace std;
#include "peter.h"
#include "stewie.h"
int main()
{
   {
      using namespace peter;
      read();
      write();
   }
   {
      using namespace stewie;
      read();
      write();
   }
//   peter::read();  // try uncommenting this line!
//   read();         // next try uncommenting this line!
   return 0;
}
