#include <iostream>
#include "binarySearchTree.h"

using namespace std;

void print(int& x);									
void update(int& x);								

int main()											
{
	bSearchTreeType<int> treeRoot;					//Line 1
		
	int num;										//Line 2

	cout << "Line 3: Enter numbers ending with -999."	
		 << endl;									//Line 3
	cin >> num;										//Line 4

	while (num != -999)								//Line 5
	{
		treeRoot.insert(num);						//Line 6
		cin >> num;									//Line 7
	}

	cout << endl 
		<< "Line 8: Tree nodes in inorder: ";	    //Line 8
	treeRoot.inorderTraversal(print);				//Line 9
	cout << endl << "Line 10: Tree Height: "
		 << treeRoot.treeHeight()
		 << endl << endl;							//Line 10

	cout << "Line 11: ******* Update Nodes *******"
		 << endl;									//Line 11
	treeRoot.inorderTraversal(update);				//Line 12

	cout << "Line 13: Tree nodes in inorder after "
		 << "the update: " << endl << "         ";	//Line 13
	treeRoot.inorderTraversal(print);				//Line 14
	cout << endl << "Line 15: Tree Height: "
		 << treeRoot.treeHeight()
		 << endl;									//Line 15

	return 0;										//Line 16
}

void print(int& x)									//Line 17
{
	cout << x << " ";								//Line 18
}	

void update(int& x)									//Line 19
{
	x = 2 * x;										//Line 20
}

