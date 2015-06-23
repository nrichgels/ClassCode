// Author: Nathan Richgels
// File: converter.cpp
// Date: 4/11/2012
// Class: CSIS252
// Assignment 10
#include <iostream>
using namespace std;
#include "converter.h"
#include "stackType.h"

char IntToChar(int num)
{
   if (num>=0 && num<=9)
      return static_cast<char>(num+48);
   else
      return static_cast<char>(num+55);
}

int CharToInt(char ch)
{
   if (ch>='0' && ch<='9')
      return static_cast<int>(ch) - 48;
   else
      return static_cast<int>(ch) - 55;
}

string Converter::DecimalToAnyBase(int value, int newBase)
{
   string result;
   int num;
   bool neg= false;
   stackType<int> Stack(100);
   Stack.initializeStack();

   if(value<0)
      {value = value * -1;
      result = "-";};

   while(value!=0)
     {Stack.push(value % newBase);
      value=value/newBase;};

   while(!Stack.isEmptyStack())
     {num=Stack.top();
      Stack.pop();
      result= result + IntToChar(num);};

   return result;
}

int Converter::AnyBaseToDecimal(string value, int currentBase)
{
   stackType<char> Stack;
   int result = 0;
   int position = 1;
   int digit;
   bool neg = false;
   Stack.initializeStack();

   if(value[0] == '-')
     {neg = true;
      for(int i=1; i<(value.length()); i++)
         Stack.push(value[i]);}

   else
      {for(int i=0; i<(value.length()); i++)
         Stack.push(value[i]);};

   while(!(Stack.isEmptyStack()))
     {digit = CharToInt(Stack.top());
      Stack.pop();
      result = result + (digit * position);
      position = position * currentBase;};

   if(neg==true)
      result = result *-1;

   return result;
}
