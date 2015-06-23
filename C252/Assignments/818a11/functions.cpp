#include <iostream>
#include <iomanip>
using namespace std;
#include <fstream>
#include "queueType.h"
#include "stackType.h"
#include "constants.h"

bool CorrectFileAmount(const int argc)
{
   if(argc==3)
      return true;
   else
      return false;
};

char lower(char LetteR)
{
   if(65<=LetteR && LetteR<=90)
      return(static_cast<char>(LetteR + 32));
   else
      return LetteR;
};

bool palindrome(ifstream& in)
{
   queueType<char> Queue(ARRAY_MAX);
   stackType<char> Stack(ARRAY_MAX);
   char current;

   in.get(current);
   while(current != '.' && !in.eof())
     {if(current != ' ' && current!= '\n' && current != ',' && current != '\'' && current != '!' && current != '?')
        {Stack.push(lower(current));
         Queue.addQueue(lower(current));};
      in.get(current);
      if(in.eof())
         return false;};

   while(!Stack.isEmptyStack())
     {if(Stack.top()==Queue.front())
        {Stack.pop();
         Queue.deleteQueue();}
      else
         return false;};
   in.get(current);
   return true;
};

void outPalindrome(ifstream& in, ofstream& out)
{
   string phrase;
   char current;
   in.get(current);
   while(current!='.' && !in.eof() )
     {phrase=phrase+current;
      in.get(current);}
   out << phrase << endl;
};
