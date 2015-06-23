// Author: Nathan Richgels
// File: main.cpp
// Date: 2/26/2013
// Class: CSIS352
// Assignment 3

#include <iostream>
#include <stdexcept>
#include <sstream>
#include "array.h"
using namespace std;
using namespace ArrayNameSpace;

void func1( Array<string> someArray, int count )
{
   stringstream outFunc;
   for(int i = 0; i<count; i++)
   {
      outFunc << someArray[i];
   }
   cout << outFunc.str();
   someArray[11] = "If this is ever seen in output, there's major trouble! \n";
   
}//End func1

void func2( Array<string>& someArray)
{
   someArray[0] = "func2 ";
   someArray[10] = "reference ";
}//End func2
int main()
{
   cout << "Test 1: " << endl;
   int arraySlots = 5;
   Array<int> testSubject(arraySlots);
   
   for(int i = 0; i<arraySlots; i++)
   {
      testSubject[i] = i;
      cout << "testSubject[" << i << "]: " << testSubject[i] << endl;
   }//End for loop
   
   cout << endl << "Test 2:" << endl;
   int count = 12;
   stringstream outMain;
   
   Array<string> stringArray(count);
   stringArray[0] = "func1 ";
   stringArray[1] = "has ";
   stringArray[3] = "executed ";
   stringArray[4] = "successfully ";
   stringArray[5] = "and ";
   stringArray[6] = "uses ";
   stringArray[7] = "a ";
   stringArray[8] = "pass ";
   stringArray[9] = "by ";
   stringArray[10] = "value ";
   stringArray[11] = "paramater. \n";
   
   func1(stringArray, count);
   func2(stringArray);
   
   for(int i = 0; i<count; i++)
      outMain << stringArray[i];
   cout << outMain.str();
   
   cout << "\nTest 3: " << endl;
   Array<string> crazyArray(-1, 1);
   cout << "Array<string> crazyArray(-1, 1);" << endl;
   cout << "assigning the strings \"One\", \" Crazy\", and \" Array\\n\" to each of it's indexes (-1 through 1)" << endl;
   crazyArray[-1] = "One";
   crazyArray[0] = " Crazy";
   crazyArray[1] = " Array\n";
   cout << "Now outputting crazy strings indeces via cout: " << endl;
   cout << crazyArray[-1] << crazyArray[0] << crazyArray[1];
   
   cout << "\nTest 4: " << endl;
   Array<char> arrayOfChars('f', 'j');
   arrayOfChars['f'] = 'H';
   arrayOfChars['g'] = 'e';
   arrayOfChars['h'] = 'l';
   arrayOfChars['i'] = 'l';
   arrayOfChars['j'] = 'o';
   
   cout << "Array<char> arrayOfChars('f', 'j');" << endl;
   cout << "Assigned H, E, L, L, and O to 'f', 'g', 'h', 'i', and 'j' respectively." << endl << "Now outputting: " << endl;
   cout << arrayOfChars['f'] << arrayOfChars['g'] << arrayOfChars['h'] << arrayOfChars['i'] << arrayOfChars['j'] << endl;
   
   cout << "\nTest 5: " << endl;
   enum daysOfWeek{Sun, Mon, Tues, Weds, Thurs, Fri, Sat};
   Array<string> weekDays(Mon, Fri);
   cout << "enum daysOfWeek{Sun, Mon, Tues, Weds, Thurs, Fri, Sat};" << endl;
   cout << "Array<string> weekDays(Mon, Fri);" << endl;
   weekDays[Mon] = "Mon: Worst day of the week.\n";
   weekDays[Tues] = "Tues: An improvement from yesterday.\n";
   weekDays[Weds] = "Weds: At least it's halfway through the week.\n";
   weekDays[Thurs] = "Thurs: Gahl, still one more full weekday after today D;  End my life now.\n";
   weekDays[Fri] = "Fri: Finally, TGIF.\n";
   
   cout << "Assigned appropriately cynical phrases for each day of the week, here goes nothing: " << endl;
   cout << weekDays[Mon] << weekDays[Tues] << weekDays[Weds] << weekDays[Thurs] << weekDays[Fri];
   
   try
   {
      weekDays[Sat] = "\nIf you see this output to the screen, then this part of the program isn't working correctly.\n";
   }//end try block
   catch(out_of_range)
   {
      cout << "\nI'm making a note here, Test 6:\n Huge Success! (this is a catch block of an exception)" << endl;
   }//End catch block
   
   Array<string> arrayOfTheEvening(200);
   try
   {
      arrayOfTheEvening[200] = "\nIf you're seeing this, I have failed.\n";
      cout << arrayOfTheEvening[200];
   }//End try block
   catch(out_of_range)
   {
      cout << "\nIf you see this, test 7 has brought honor to my family. (this is a catch block of an exception)" << endl;
   }//End catch block
   
   try
   {
      Array<float> thisShouldntExist(Fri, Sun);
   }//End try block
   catch(domain_error)
   {
      cout << "\nThe 8th test succeeds! (this is a catch block of an exception)" << endl;
   }
   
   cout << "\nTest 9: Let the Relational Operator testing begin!" << endl;
   Array<int> Comparitor1(10);
   Array<int> Comparitor2(10);
   for(int i = 0; i<10; i++)
   {
      Comparitor1[i] = i + 1;
   }//End for loop
   Comparitor2 = Comparitor1;
   cout << "Comparitor2 == Comparitor1: " << (Comparitor2 == Comparitor1) << endl;
   Comparitor2[9] = 9;
   cout << "Comparitor2[9] = 9;" << endl << "Comparitor2 == Comparitor1: " << (Comparitor2 == Comparitor1) << " Should be: 0" << endl;
   cout << "Comparitor2 < Comparitor1: " << (Comparitor2 < Comparitor1) << " Should be: 1" << endl;
   cout << "Comparitor2 > Comparitor1: " << (Comparitor2 > Comparitor1) << " Should be: 0" << endl;
   cout << "Comparitor1 < Comparitor2: " << (Comparitor1 < Comparitor2) << " Should be: 0" << endl;
   cout << "Comparitor1 > Comparitor2: " << (Comparitor1 > Comparitor2) << " Should be: 1" << endl;
   
   cout << "\nTest 10: Relational Operator testing part 2!" << endl;
   cout << "Comparitor1.Resize(9);" << endl;
   Comparitor1.Resize(9);
   cout << "Comparitor2 == Comparitor1: " << (Comparitor2 == Comparitor1) << " Should be: 0" << endl;
   cout << "Comparitor2 < Comparitor1: " << (Comparitor2 < Comparitor1) << " Should be: 0" << endl;
   cout << "Comparitor2 > Comparitor1: " << (Comparitor2 > Comparitor1) << " Should be: 1" << endl;
   cout << "Comparitor1 < Comparitor2: " << (Comparitor1 < Comparitor2) << " Should be: 1" << endl;
   cout << "Comparitor1 > Comparitor2: " << (Comparitor1 > Comparitor2) << " Should be: 0" << endl;
   cout << "Comparitor1 >= Comparitor2: " << (Comparitor1 >= Comparitor2) << " Should be: 0" << endl;
   cout << "Comparitor1 <= Comparitor2: " << (Comparitor1 <= Comparitor2) << " Should be: 1" << endl;
   cout << "comparitor1 != Comparitor2: " << (Comparitor1 != Comparitor2) << " Should be: 1" << endl;
   cout << "Comparitor1.Size(): " << Comparitor1.Size() << endl;
   cout << "Comparitor2.Size(): " << Comparitor2.Size() << endl;
   
   try
   {
      cout << "\nTest 11" << endl;
      Array<int> someArray(-1);
      cout << "Array Initialized." << endl;
   }//End try
   catch(invalid_argument e)
   {
      cout << e.what() << endl;;
   }//End catch
   
   try
   {
      Array<int> someArray(12);
      someArray.Resize(-4);
   }//End try
   catch(invalid_argument e)
   {
      cout << e.what() << endl;; 
   }//End catch
   return 0;
}//End main
