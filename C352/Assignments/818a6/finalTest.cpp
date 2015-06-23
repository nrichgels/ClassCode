#include <iostream>
#include "binarySearchTree.h"
using namespace std;

void func(double& x )
{
   cout << x << " ";
}//End func

int main()
{
   bSearchTreeType<double> mySearchTree;
   cout << "Inputting floats: 1000, 500, 1500, 750, 625, 200, 300, 400, 100, 150, 50, 50.1, 49.9 1250,\n"
           "1750, 1650, 1600, 1700, 2000, 1800, 2500, 2250, 3000" << endl << endl;
   mySearchTree.insert(1000);
   mySearchTree.insert(500);
   mySearchTree.insert(1500);
   mySearchTree.insert(750);
   mySearchTree.insert(625);
   mySearchTree.insert(200);
   mySearchTree.insert(300);
   mySearchTree.insert(400);
   mySearchTree.insert(100);
   mySearchTree.insert(150);
   mySearchTree.insert(50);
   mySearchTree.insert(50.1);
   mySearchTree.insert(49.9);
   mySearchTree.insert(1250);
   mySearchTree.insert(1750);
   mySearchTree.insert(1650);
   mySearchTree.insert(1600);
   mySearchTree.insert(1700);
   mySearchTree.insert(2000);
   mySearchTree.insert(1800);
   mySearchTree.insert(2500);
   mySearchTree.insert(2250);
   mySearchTree.insert(3000);
   
   cout << "Entering mySearchTree.inOrder(func): " << endl;
   mySearchTree.inorderTraversal(func);
   cout << endl << endl;
   
   cout << "Entering mySearchTree.preOrder(func): " << endl;
   cout << "Right answer: 1000, 500, 200, 100, 50, 49.9, 50.1, 150, 300, 400, 750, 625, 1500, 1250\n";
   cout << "              1750, 1650, 1600, 1700, 2000, 1800, 2500, 2250, 3000\n\n";
   mySearchTree.preorderTraversal(func);
   cout << endl << endl;
   
   cout << "Using nodeCount(): (note: Right answer is 23)" << endl;
   cout << mySearchTree.treeNodeCount() << endl;
   
   cout << "Using leavesCount(): (note: Right answer is 11)" << endl;
   cout << mySearchTree.treeLeavesCount() << endl << endl;
   
   cout << "Finding level of 49.9: (note: Right answer is 5)" << endl;
   cout << mySearchTree.level(49.9) << endl << endl;
   
   cout << "Finding if balanced: (note: Should not be balanced)" << endl;
   
   if(mySearchTree.balanced())
      cout << "     Not detecting if balanced right\n\n";
   else
      cout << "     Unbalanced: Correct.\n\n";
   
   cout << "Searching for 150: (note: Should be found)" << endl;
   if( mySearchTree.search(150) )
      cout << "150 Found." << endl << endl;
   else
      cout << "150 Not found." << endl;
   
   cout << "Searching for 150.1: (note: Should not be found)" << endl;
   if( mySearchTree.search(150.1) )
      cout << "150.1 Found." << endl << endl;
   else
      cout << "150.1 Not found." << endl << endl;
   
   
   
   return 0;
}//End main