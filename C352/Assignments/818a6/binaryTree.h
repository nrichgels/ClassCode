//Header File Binary Search Tree
#ifndef H_binaryTree
#define H_binaryTree
#include <iostream>
#include <stack>

using namespace std;

	//Definition of the Node
template <class elemType>
struct nodeType
{
	elemType			info;
	nodeType<elemType>  *llink;
	nodeType<elemType>  *rlink;
};
	
	//Definition of the class
template <class elemType>
class binaryTreeType
{
public:
    const binaryTreeType<elemType>& operator=
                 (const binaryTreeType<elemType>&); 
      //Overload the assignment operator.
    bool isEmpty() const;
      //Function to determine whether the binary tree
	  //is empty.
	  //Postcondition: Returns true if the binary tree is empty;
      //               otherwise, returns false.
    void inorderTraversal() const;
      //Function to do an inorder traversal of the binary tree.
	  //Postcondition: Nodes are printed in inorder sequence.
    void preorderTraversal() const;
      //Function to do a preorder traversal of the binary tree.
	  //Postcondition: Nodes are printed in preorder sequence.
    void postorderTraversal() const;
      //Function to do a postorder traversal of the binary tree.
	  //Postcondition: Nodes are printed in postorder sequence.

	void inorderTraversal(void (*visit) (elemType&)) const;
	  //Function to do an inorder traversal of the binary tree.
	  //The parameter visit, which is a function, specifies
	  //the action to be taken at each node.
	  //Postcondition: The action specified by the function visit
	  //               is applied to each node of the binary tree.

        
         void preorderTraversal(void (*visit) (elemType&)) const;
            //Function to do an inorder traversal of the binary tree.
            //The parameter visit, which is a function, specifies
            //the action to be taken at each node.
            //Postcondition: The action specified by the function visit
            //               is applied to each node of the binary tree.    
            
       int treeHeight() const;
      //Funtion to determine the height of a binary tree.
	  //Postcondition: Returns the height of the binary tree.
    int treeNodeCount() const;
      //Funtion to determine the number of nodes in a 
	  //binary tree.
      //Postcondition: Returns the number of nodes in the 
	  //               binary tree.
    int treeLeavesCount() const;
      //Funtion to determine the number of leaves in a 
	  //binary tree.
      //Postcondition: Returns the number of leaves in the 
	  //               binary tree.
    void destroyTree();
      //Function to destroy the binary tree.
	  //Postcondition: Memory space occupied by each node 
	  //               is deallocatd.
      //               root = NULL;

    binaryTreeType(const binaryTreeType<elemType>& otherTree); 
      //copy constructor

    binaryTreeType();   
      //default constructor

    ~binaryTreeType();   
      //destructor

protected:
    nodeType<elemType>  *root;

private:
    void copyTree(nodeType<elemType>* &copiedTreeRoot,
                  nodeType<elemType>* otherTreeRoot);
      //Makes a copy of the binary tree to which 
      //otherTreeRoot points. 
	  //Postcondition: The pointer copiedTreeRoot points to
      //               the root of the copied binary tree.
    void destroy(nodeType<elemType>* &p);
      //Function to destroy the binary tree to which p points. 
      //Postcondition: Memory space occupied by each node, in the
	  //               binary tree to which p points, is deallocatd.
      //               p = NULL;

    void inorder(nodeType<elemType> *p) const;
      //Function to do an inorder traversal of the binary
      //tree to which p points.  
	  //Postcondition: Nodes of the binary tree, to which p
	  //               points, are printed in inorder sequence.
    void preorder(nodeType<elemType> *p) const;
      //Function to do a preorder traversal of the binary
      //tree to which p points.  
	  //Postcondition: Nodes of the binary tree, to which p
	  //               points, are printed in preorder sequence.
    void postorder(nodeType<elemType> *p) const;
      //Function to do a postorder traversal of the binary
      //tree to which p points.  
	  //Postcondition: Nodes of the binary tree, to which p
	  //               points, are printed in postorder sequence.

	void inorder(nodeType<elemType> *p, void (*visit) (elemType&)) const;
	  //Function to do an inorder traversal of the binary
	  //tree starting at the node specified by the parameter p. 
	  //The parameter visit, which is a function, specifies the
	  //action to be taken at each node.
	  //Postcondition: The action specified by the function visit
	  //               is applied to each node of the binary tree
	  //               to which p points.


    int height(nodeType<elemType> *p) const;
      //Function to determine the height of the binary tree
      //to which p points. 
	  //Postcondition: Height of the binary tree to which 
	  //               p points is returned.
    int max(int x, int y) const;
      //Function to determine the larger of x and y.
	  //Postcondition: Returns the larger of x and y.
    int nodeCount(nodeType<elemType> *p) const;
      //Function to determine the number of nodes in 
      //the binary tree to which p points. 
  	  //Postcondition: The number of nodes in the binary 
	  //               tree to which p points is returned.
    int leavesCount(nodeType<elemType> *p) const;
      //Function to determine the number of leaves in  
      //the binary tree to which p points 
 	  //Postcondition: The number of leaves in the binary 
	  //               tree to which p points is returned.
};

	//Definition of member functions

template<class elemType>
binaryTreeType<elemType>::binaryTreeType()
{
	root = NULL;
}

template<class elemType>
bool binaryTreeType<elemType>::isEmpty() const
{
	return (root == NULL);
}

template<class elemType>
void binaryTreeType<elemType>::inorderTraversal() const
{
	inorder(root);
}

template<class elemType>
void binaryTreeType<elemType>::preorderTraversal() const
{
	preorder(root);
}

template<class elemType>
void binaryTreeType<elemType>::postorderTraversal() const
{
	postorder(root);
}

template<class elemType>
int binaryTreeType<elemType>::treeHeight() const
{
	return height(root);
}

template<class elemType>
int binaryTreeType<elemType>::treeNodeCount() const
{
	return nodeCount(root);
}

template<class elemType>
int binaryTreeType<elemType>::treeLeavesCount() const
{
	return leavesCount(root);
}

template <class elemType>
void  binaryTreeType<elemType>::copyTree
                      (nodeType<elemType>* &copiedTreeRoot,
		               nodeType<elemType>* otherTreeRoot)
{
	if (otherTreeRoot == NULL)
		copiedTreeRoot = NULL;
	else
	{
		copiedTreeRoot = new nodeType<elemType>;
		copiedTreeRoot->info = otherTreeRoot->info;
		copyTree(copiedTreeRoot->llink, otherTreeRoot->llink);
		copyTree(copiedTreeRoot->rlink, otherTreeRoot->rlink);
	}
} //end copyTree

template<class elemType>
void binaryTreeType<elemType>::inorder(nodeType<elemType> *p) const
{
	if (p != NULL)
	{
		inorder(p->llink);
		cout << p->info << " ";
		inorder(p->rlink);
	}
}

template<class elemType>
void binaryTreeType<elemType>::preorder(nodeType<elemType> *p) const
{
	if (p != NULL)
	{
		cout << p->info << " ";
		preorder(p->llink);
		preorder(p->rlink);
	}
}

template<class elemType>
void binaryTreeType<elemType>::postorder(nodeType<elemType> *p) const
{
	if (p != NULL)
	{
		postorder(p->llink);
		postorder(p->rlink);
		cout << p->info << " ";
	}		
}

   //Overload the assignment operator
template<class elemType>
const binaryTreeType<elemType>& binaryTreeType<elemType>::
           operator=(const binaryTreeType<elemType>& otherTree)
{ 
	if (this != &otherTree) //avoid self-copy
	{
		if (root != NULL)  //if the binary tree is not empty, 
			              //destroy the binary tree
			destroy(root);

		if (otherTree.root == NULL) //otherTree is empty
			root = NULL;
		else
			copyTree(root, otherTree.root);
	}//end else

   return *this; 
}

template <class elemType>
void  binaryTreeType<elemType>::destroy(nodeType<elemType>* &p)
{
	if (p != NULL)
	{
		destroy(p->llink);
		destroy(p->rlink);
		delete p;
		p = NULL;
	}
}

template <class elemType>
void  binaryTreeType<elemType>::destroyTree()
{
	destroy(root);
}

	//copy constructor
template <class elemType>
binaryTreeType<elemType>::binaryTreeType
              (const binaryTreeType<elemType>& otherTree)
{
	if (otherTree.root == NULL) //otherTree is empty
		root = NULL;
	else
		copyTree(root, otherTree.root);
}

template <class elemType>
binaryTreeType<elemType>::~binaryTreeType()
{
	destroy(root);
}

template<class elemType>
int binaryTreeType<elemType>::height(nodeType<elemType> *p) const
{
	if (p == NULL)
		return 0;
	else
		return 1 + max(height(p->llink), height(p->rlink));
}

template<class elemType>
int binaryTreeType<elemType>::max(int x, int y) const
{
	if (x >= y)
		return x;
	else
		return y;
}

template<class elemType>
int binaryTreeType<elemType>::nodeCount(nodeType<elemType> *p) const
{
	if( p  == NULL)
		return 0;
	if ( (*p).llink == NULL && (*p).rlink == NULL )
		return 1;
	else
		return (nodeCount( (*p).llink ) + nodeCount( (*p).rlink ) + 1);
}

template<class elemType>
int binaryTreeType<elemType>::leavesCount(nodeType<elemType> *p) const
{
	if(p == NULL)
	{
		return 0;
	}
	if( ((*p).llink ==NULL) && ((*p).rlink == NULL) )
		return 1;
	else
		return( leavesCount( (*p).llink ) + leavesCount( (*p).rlink ) );
}

template <class elemType>
void binaryTreeType<elemType>::inorderTraversal
			                  (void (*visit) (elemType& item)) const
{ 
   stack<nodeType<elemType>*> toVisit;
   nodeType<elemType> *current;
   current = root;
   bool stackAdderRightForked = false;
   
   if( (*current).rlink != NULL )
      toVisit.push( (*current).rlink );
   
   while( (*current).llink != NULL )
   {
      toVisit.push(current);
      current = (*current).llink;
      stackAdderRightForked = false;
   }//End whle loop
   
   while( !(toVisit.empty()) )
   {
      if( stackAdderRightForked )
      {
         while( (*current).llink != NULL )
         {
            toVisit.push(current);
            current = (*current).llink;
         }//End while loop
         stackAdderRightForked = false;
      }//End if statement
      
      visit((*current).info);
      if( (*current).rlink != NULL )
      {
         current = (*current).rlink;
            
         while( (*current).llink != NULL )
         {
            stackAdderRightForked = false;
            toVisit.push(current);
            current = (*current).llink;
         }//End while loop
         
         if( (*current).rlink != NULL && (*current).llink == NULL )
         {
            toVisit.push((*current).rlink);
            stackAdderRightForked = true;
         }//End if
         
         visit((*current).info);
      }//End if statement
      
      current = toVisit.top();
      toVisit.pop();
      
   }//End while loop
   
   if(current == root)
      visit( (*current).info );
      


	//inorder(root, *visit);
}

template <class elemType>
void binaryTreeType<elemType>::inorder(nodeType<elemType>* p,
							   void (*visit) (elemType& item)) const
{
	if (p != NULL)
	{
		inorder(p->llink, *visit);
		(*visit)(p->info);
		inorder(p->rlink, *visit);
	}
}


template<class elemType>
void binaryTreeType<elemType>::preorderTraversal(void (*visit) (elemType&)) const
{
   stack<nodeType<elemType>*> returnToValue;
   nodeType<elemType> *current;
   nodeType<elemType> *max;
   max = root;
   current = root;
   
   while( (*max).rlink != NULL )
      max = (*max).rlink;
   
   if( max == root)
   {
      
      returnToValue.push( current );
      visit( (*current).info );
      if( (*current).llink != NULL )
         current = (*current).llink;
   }//End if statement
   
   while(current != max)
   {
      
      while( (*current).llink != NULL )
      {
         if( (*current).rlink != NULL )
            returnToValue.push( (*current).rlink );
         visit( (*current).info );
         current = (*current).llink;
      }//End while loop
      
      if( (*current).rlink != NULL )
         returnToValue.push( (*current).rlink );
      visit( (*current).info );
      
      
      current = returnToValue.top();
      returnToValue.pop();
   }//End while loop
   
   if( max != root )
      visit( (*current).info );

}//End preorderTraversal

#endif

