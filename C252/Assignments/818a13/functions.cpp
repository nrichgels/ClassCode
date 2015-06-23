#include <iostream>
#include <iomanip>
#include <fstream>
using namespace std;
#include "binarySearchTree.h"
#include "binaryTree.h"
#include "bst.h"
#include "date.h"
#include "person.h"
#include "student.h"

BST<Student> ReadInput(ifstream& in)
{
   BST<Student> Tree;
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
         Tree.insert(pupil);};}
   return Tree;
}

void WriteOutput(ofstream& out, BST<Student> Tree)
{
   int c=0;
   Student pupil;
   out << left << setw(30) << "Name" << "Dragon ID" << endl;
   out << left << setw(30) << "____" << "_________" << endl;
   Tree.reset();
   while(Tree.inorderGetNextItem(pupil))
      out << left << setw(30) << pupil.Name() << pupil.ID() << endl;
}
