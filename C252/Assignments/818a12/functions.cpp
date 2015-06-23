#include <fstream>
#include <iostream>
#include <iomanip>
using namespace std;
#include "linkedList.h"
#include "linkedList2.h"
#include "sortedList.h"
#include "student.h"

void WriteOutput(ofstream& out, sortedListType<Student> List)
{
   int c=0;
   Student pupil;
   out << left << setw(30) << "Name" << "Dragon ID" << endl;
   out << left << setw(30) << "____" << "_________" << endl;
   while(List.length() > c)
     {List.retrieveAt(c, pupil);
      out << left << setw(30) << pupil.Name() << pupil.ID() << endl;
      c++;}
}

sortedListType<Student> ReadInput(ifstream& in)
{
   sortedListType<Student> List;
   Student pupil;
   string Name;
   char character;
   int DragID;
   int i=1;

   while(!in.eof())
     {Name="";
      in.get(character);
      if(character=='\n')
         in.get(character);
      if(in.eof())
         character=',';
      while(character!=',')
        {Name=Name+character;
         in.get(character);}
      if(!in.eof())
        {pupil.setName(Name);
         in >> DragID;
         pupil.setID(DragID);
         List.insert(pupil);};}
   return List;
}
