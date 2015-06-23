#include <iostream>

using namespace std;

int main()
{
   char s[]="hello there";
   char *p;
   p=s;
   while (*p != '\0')
      cout << *p++;
   cout << endl;
   p=s;
   int i=0;
   while (p[i] != '\0')
      cout << p[i++];
   cout << endl;
   i=0;
   while (s[i] != '\0')
      cout << s[i++];
   cout << endl;
   return 0;
}
