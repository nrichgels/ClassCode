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
#include "prototypes.h"

int main(int argc, char* argv[])
{
   ifstream in;
   ofstream out;
   BST<Student> Tree;
   in.open(argv[1]);
   out.open(argv[2]);

   Tree=ReadInput(in);
   WriteOutput(out, Tree);

   in.close();
   out.close();

   return 0;
}
