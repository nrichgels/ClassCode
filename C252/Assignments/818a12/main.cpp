#include <iostream>
#include <fstream>
using namespace std;
#include "linkedList.h"
#include "linkedList2.h"
#include "sortedList.h"
#include "student.h"
#include "prototypes.h"

int main(int argc, char* argv[])
{
   ifstream in;
   ofstream out;
   sortedListType<Student> List;
   in.open(argv[1]);
   out.open(argv[2]);

   List=ReadInput(in);
   WriteOutput(out, List);
   return 0;
}
