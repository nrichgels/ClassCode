#include <iostream>
#include <iterator>
using namespace std;

int main()
{
   istream_iterator<int> in(cin);
   ostream_iterator<int> out(cout,"\n");
   int num;
   num = *in;
   while (num!=-999)
   {
      out++ = num;
      in++;
      num = *in;
   }
   return 0;
}
