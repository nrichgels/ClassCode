#include <iostream>
using namespace std;

void func1(void)
{
   cout << "hello\n";
}

void func2(int& num)
{
   num = 99;
   cout << "in func2 " << num << endl;
}

int func3(int x)
{
   x = x+1;
   return x;
}

int main()
{
   func1();
   int x = 44;
   func2(x);
   cout << "in main " << x << endl;
   cout << func3(x) << endl;
   return 0;
}
