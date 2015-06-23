// Demo program
#include <iostream>
#include "binarySearchTree.h"

using namespace std;

void visitFunction(int& value)
{
   cout << value << ' ';
}

int main()
{
   bSearchTreeType<int> tree;
   int num;

   cout << "Enter numbers ending with 0." << endl;
   cin >> num;
   while (num != 0)
   {
      tree.insert(num);
      cin >> num;
   }
   cout << "inorder traversal: ";
   tree.inorderTraversal(visitFunction);
   cout << endl;
   cout << "preorder traversal: ";
   tree.preorderTraversal(visitFunction);
   cout << endl;
// uncomment if you did the bonus method
/*
   cout << "postorder traversal: ";
   tree.postorderTraversal(visitFunction);
   cout << endl;
*/

   num = 999;
   tree.insert(999);
   if (tree.search(num))
      cout << num << " is in the tree at level " << tree.level(num) << endl;
   else
      cout << num << " is NOT in the tree\n";
   tree.deleteNode(num);
   if (tree.search(num))
      cout << num << " is in the tree\n";
   else
      cout << num << " is NOT in the tree\n";
   if (tree.balanced())
      cout << "the tree is balanced\n";
   else
      cout << "the tree is NOT balanced\n";
   cout << "tree height = " << tree.treeHeight() << endl;
   cout << "node count  = " << tree.treeNodeCount() << endl;
   cout << "leaves count  = " << tree.treeLeavesCount() << endl;
// remove comment if attempting bonus
/*
   if (tree.full())
      cout << "the tree is full\n";
   else
      cout << "the tree is NOT full\n";
*/
// remove comment if attempting bonus
/*
   if (tree.complete())
      cout << "the tree is complete\n";
   else
      cout << "the tree is NOT complete\n";
*/
   return 0;
}