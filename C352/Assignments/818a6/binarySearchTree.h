//Header File Binary Search Tree

#ifndef H_binarySearchTree
#define H_binarySearchTree
#include <iostream>
#include <cassert>
#include "binaryTree.h"
#include <stack>
#include <stdexcept>

using namespace std;

template<class elemType>
class bSearchTreeType: public binaryTreeType<elemType>
{
public:
    bool search(const elemType& searchItem) const;
      //Function to determine if searchItem is in the binary 
      //search tree.
      //Postcondition: Returns true if searchItem is found in the 
      //               binary search tree; otherwise, returns false.

    void insert(const elemType& insertItem);
      //Function to insert insertItem in the binary search tree.
      //Postcondition: If there is no node in the binary search
      //               tree that has the same info as insertItem,
      //               a node with the info insertItem is created
      //               and inserted in the binary search tree.


    void deleteNode(const elemType& deleteItem);
      //Function to delete deleteItem from the binary search tree 
      //Postcondition: If a node with the same info as deleteItem 
      //               is found, it is deleted from the binary 
      //               search tree.
      //               If the binary tree is empty or deleteItem
      //               is not in the binary tree, an appropriate
      //               message is ptinted.

   int level(const elemType& item) const;
      //Function to return the level of the tree where item is.
      //     The level is the number of branches from the root to the node. 
      //     The root is at level 0.
      //Input: item to find the level where it's at
      //Output: level where item is
      //Precondition:  item must be in the tree
      //Postcondition: Returns the level where item is 
   
   bool balanced() const;
      //Function to return whether the tree is balanced (by definition) or not
      //Input: none
      //Output: whether tree is balanced or not (bool)
      //Precondition:  none
      //Postcondition: Returns true if tree is balanced, false otherwise

private:
    void deleteFromTree(nodeType<elemType>* &p);
      //Function to delete the node to which p points is deleted
      //from the binary search tree.
      //Postcondition: The node to which p points is deleted
      //               from the binary search tree.
    
    bool privateSearch(nodeType<elemType> *p, const elemType& searchItem) const;
    //Function to determine if searchItem is in the binary 
    //search tree.
    //Postcondition: Returns true if searchItem is found in the 
    //               binary search tree; otherwise, returns false.
      
    void privateInsert(nodeType<elemType> *p, const elemType& insertItem, stack<nodeType<elemType>* >& previousContainer);
    //Function to insert insertItem in the binary search tree.
    //Postcondition: If there is no node in the binary search
    //               tree that has the same info as insertItem,
    //               a node with the info insertItem is created
    //               and inserted in the binary search tree.
    
    int privateLevel(nodeType<elemType> *p, const elemType& item) const;
          //Function to return the level of the tree where item is.
      //     The level is the number of branches from the p to the node. 
      //     The root is at level 0.
      //Input: item to find the level where it's at
      //       node
      //Output: level where item is
      //Precondition:  item must be in the tree
      //                node must be in tree
      //Postcondition: Returns the level where item is from subtree p
    
    int deepestLevel(nodeType<elemType> *p) const;
    // Fuction to return the the level of the longest path in the tree
    //       (or subtree) that starts at node p.
    //Input: A Node within the tree
    // Output: level of the longest branch
    //Precondition: Tree has a value in it.
    //Postcondition: Returns level of longest branch.
    
    bool privateBalanced( nodeType<elemType> *p ) const;
      //Function to return whether the tree is balanced (by definition) or not
      //Input: node
      //Output: whether tree is balanced or not (bool)
      //Precondition:  node is within tree
      //Postcondition: Returns true if tree is balanced, false otherwise

};

 template<class elemType>
 bool bSearchTreeType<elemType>::privateSearch( nodeType<elemType>* p, const elemType& searchItem) const
 {
    if( (*p).info == searchItem )
       return true;
    
    if( (*p).info < searchItem )
    {
       if( (*p).rlink != NULL )
         return privateSearch( (*p).rlink, searchItem );
    }//End if statement
    
    if( (*p).info > searchItem )
    {
       if( (*p).llink != NULL )
          return privateSearch( (*p).llink, searchItem );
    }//End if statement
    
    return false;
 }//End privateSearch

template<class elemType>
bool bSearchTreeType<elemType>::search(const elemType& searchItem) const
{
   if( binaryTreeType<elemType>::root != NULL )
      return( privateSearch( binaryTreeType<elemType>::root, searchItem ) );
   else
      return false;
    /*
    nodeType<elemType> *current;
    bool found = false;

    if (binaryTreeType<elemType>::root == NULL)
        cout << "Cannot search an empty tree." << endl;
    else
    {
       current = binaryTreeType<elemType>::root;

       while (current != NULL && !found)
       {
             if (current->info == searchItem)
                 found = true;
              else
                  if (current->info > searchItem)
                      current = current->llink;
                  else
                      current = current->rlink;
       }//end while
    }//end else

    return found;
    */

}//end search

template<class elemType>
void bSearchTreeType<elemType>::privateInsert(nodeType<elemType> *p, const elemType& insertItem, stack<nodeType<elemType>* >& previousContainer)
{
   nodeType<elemType> *previousNode;
   nodeType<elemType> *newNode;
   
   if( p == NULL)
   {
      newNode = new nodeType<elemType>;
      (*newNode).llink = NULL;
      (*newNode).rlink = NULL;
      (*newNode).info = insertItem;
      
      if( previousContainer.empty() )
         binaryTreeType<elemType>::root = newNode;
      else
      {
         previousNode = previousContainer.top();
         if( (*previousNode).info > (*newNode).info )
            (*previousNode).llink = newNode;

         if( (*previousNode).info < (*newNode).info )
            (*previousNode).rlink = newNode;
      }//End else statement
    }//End if statement
   
   if ( p != NULL )
   {
      previousContainer.push(p);
      if( (*p).info > insertItem )
         privateInsert( (*p).llink, insertItem, previousContainer );
      
      if( (*p).info < insertItem )
         privateInsert( (*p).rlink, insertItem, previousContainer );
   }//End if statement
}//End privateInsert

template<class elemType>
void bSearchTreeType<elemType>::insert(const elemType& insertItem)
{
   stack<nodeType<elemType>* > previousContainer;
   privateInsert(binaryTreeType<elemType>::root, insertItem, previousContainer);
   

    /*
    nodeType<elemType> *current;  //pointer to traverse the tree
    nodeType<elemType> *trailCurrent; //pointer behind current
    nodeType<elemType> *newNode;  //pointer to create the node

    newNode = new nodeType<elemType>;
    assert(newNode != NULL);
    newNode->info = insertItem;
    newNode->llink = NULL;
    newNode->rlink = NULL;

    if (binaryTreeType<elemType>::root == NULL)
       binaryTreeType<elemType>::root = newNode;
    else
    {
       current = binaryTreeType<elemType>::root;
 
       while (current != NULL)
       {
           trailCurrent = current;

           if (current->info == insertItem)
           {
               cout << "The item to be inserted is already in ";
               cout << "the list -- duplicates are not allowed."
                    << endl;
               return;
           }
           else
               if (current->info > insertItem)
                   current = current->llink;
               else
                   current = current->rlink;
       }//end while

       if (trailCurrent->info > insertItem)
           trailCurrent->llink = newNode;
       else
           trailCurrent->rlink = newNode;
       */
}//end insert

template<class elemType>
void bSearchTreeType<elemType>::deleteNode(const elemType& deleteItem)
{
	nodeType<elemType> *current;  //pointer to traverse the tree
	nodeType<elemType> *trailCurrent; //pointer behind current
	bool found = false;

	if (binaryTreeType<elemType>::root == NULL)
		cout << "Cannot delete from an empty tree." 
		     << endl;
	else
	{
		current = binaryTreeType<elemType>::root;
		trailCurrent = binaryTreeType<elemType>::root;

		while (current != NULL && !found)
		{
			if (current->info == deleteItem)
				found = true;
			else
			{
				trailCurrent = current;

				if (current->info > deleteItem)
					current = current->llink;
				else
					current = current->rlink;
			}
		}//end while

		if (current == NULL)
			cout << "The item to be deleted is not in the tree." 
			     << endl;
		else
			if (found)
			{
				if (current == binaryTreeType<elemType>::root)
					deleteFromTree(binaryTreeType<elemType>::root);
				else
					if (trailCurrent->info > deleteItem)
						deleteFromTree(trailCurrent->llink);
					else
						deleteFromTree(trailCurrent->rlink);
			}//end if
	}
}//end deleteNode

template<class elemType>
void bSearchTreeType<elemType>::deleteFromTree
                                 (nodeType<elemType>* &p)
{
     nodeType<elemType> *current;    //pointer to traverse 
                                     //the tree
     nodeType<elemType> *trailCurrent;   //pointer behind current
     nodeType<elemType> *temp;        //pointer to delete the node

     if (p == NULL)
         cout << "Error: The node to be deleted is NULL."
              << endl;
     else if (p->llink == NULL && p->rlink == NULL)
          {
             temp = p;
             p = NULL;
             delete temp;
          }
     else if (p->llink == NULL)
          {
             temp = p;
             p = temp->rlink;
             delete temp;
          }
     else if (p->rlink == NULL)
          {
             temp = p;
             p = temp->llink;
             delete temp;
          }
     else
     {
        current = p->llink;
        trailCurrent = NULL;

        while (current->rlink != NULL)
        {
            trailCurrent = current;
            current = current->rlink;
        }//end while

        p->info = current->info;

        if (trailCurrent == NULL) //current did not move; 
                                  //current == p->llink; adjust p
            p->llink = current->llink;
        else
            trailCurrent->rlink = current->llink;
 
        delete current;
     }//end else
}//end deleteFromTree

template<class elemType>
int bSearchTreeType<elemType>::level(const elemType& item) const
{
   if( binaryTreeType<elemType>::root == NULL )
      throw invalid_argument("Error: Tree holds no contents.");
   
   return privateLevel(binaryTreeType<elemType>::root, item);
}//End level

template<class elemType>
int bSearchTreeType<elemType>::privateLevel(nodeType<elemType> *p, const elemType& item) const
{
    
    if( (*p).info == item )
       return 0;
    
    if( (*p).info < item )
    {
       if( (*p).rlink != NULL )
         return privateLevel( (*p).rlink, item ) + 1;
    }//End if statement
    
    if( (*p).info > item )
    {
       if( (*p).llink != NULL )
          return privateLevel( (*p).llink, item ) +1;
    }//End if statement
    throw invalid_argument("Error: Given item does not exist within the Binary Tree.");
}//End privateLevel

template<class elemType>
bool bSearchTreeType<elemType>::balanced() const
{
  if( binaryTreeType<elemType>::root == NULL )
     throw invalid_argument( "Error: Cannot determine whether a Binary Tree is balanced if it contains no items." );
  
  return( privateBalanced( binaryTreeType<elemType>::root ) );

}//End balanced

template<class elemType>
int bSearchTreeType<elemType>::deepestLevel( nodeType<elemType> *p ) const
{
   if( (*p).llink != NULL && (*p).rlink != NULL )
   {
      //I realize the below if statement is an aweful Algorithm design, but
      //it was the best way I could think to do it without assigning variables,
      //which would violate the const declaration of the method. :(
      if( deepestLevel( (*p).llink ) > deepestLevel( (*p).rlink ) )
         return deepestLevel( (*p).llink ) + 1;
      else
         return deepestLevel( (*p).rlink ) + 1;
   }//End if
   
   else if( (*p).llink != NULL )
      return deepestLevel( (*p).llink ) + 1;
   
   else if( (*p).rlink != NULL )
      return deepestLevel( (*p).rlink ) + 1;
   else
      return 0;
}//End deepestLevel;

template<class elemType>
bool bSearchTreeType<elemType>::privateBalanced( nodeType<elemType> *p ) const
{
   if( (*p).llink == NULL && (*p).rlink == NULL )
      return true;
   
   if( (*p).llink == NULL )
      return( deepestLevel( (*p).rlink )== 0 );
   
   if( (*p).rlink == NULL )
      return( deepestLevel( (*p).llink ) == 0 );
   
   if( (deepestLevel( (*p).llink ) - deepestLevel( (*p).rlink ) ) > 1 || ( deepestLevel( (*p).llink ) - deepestLevel( (*p).rlink ) ) < -1 )
      return false;
   else
      return privateBalanced( (*p).llink ) && privateBalanced( (*p).rlink );
}
#endif

