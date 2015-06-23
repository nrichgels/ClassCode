#include <iostream>
using namespace std;
#include <fstream>

char lower(char LetteR)
{
   if(65<=LetteR && LetteR<=90)
      return(static_cast<char>(LetteR + 32));
   else
      return LetteR;
};

int main(int argc, char* argv[])
{
   char n='R';
   cout << n << "Food4Thought" << endl;
   cin.get(n);
   cout << n << "Food4Thought" << endl;
   if(n=='\n')
      cout << "True" << endl;
   else
      cout << "False" << endl;

   return 0;
}
