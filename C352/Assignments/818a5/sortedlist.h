// Author: Nathan Richgels
// File: sortedlist.h
// Date: 3/26/2013
// Class: CSIS352
// Assignment 5
// This file contains the specification and implementation of the
// SortedList class.  This class is-a list, except it automatically
// orders it's contents, and provides additional (and optional)
// methods of traversing it.

#include <list>
#include <iterator>
using namespace std;

/************************CLASS DECLERATION****************************
 * *******************************************************************/
template <class T>
class SortedList : public list<T>
{
public:
   // Method inserts a value into the list
   // Preconditions: List exists and paramater is of type T
   // Postconditions: Inserted into list in order
   // Paramaters: T: an object of type T
   void insert(const T&);
   
   // Method uses a function that takes a paramater of type T, and applies the
   //   function to each item in the list.
   // Preconditions: Passed a function that takes an argument of type T
   // Postconditions: The function is applied to every value in the list.
   void traverse(void (*p) (T&));
   
   // Method prepares the object for an "internal" traversal.
   // Preconditions: SortedList has been initialized
   // Postconditions: endOfList and getNextItem methods are correctly executed.
   // Paramaters: none
   void reset();
   
   // Method reports if the "internal" traversal is at the end location of
   //   the list.
   // Preconditions: List is initialized and reset has been used since
   //                inserting a value.
   // Postconditions: Returns true if the "internal" iterator is alotted 
   //                 at the "end" position.
   // Paramaters: none
   bool endOfList() const;
   
   // Method returns the value of the next item to be "internally" iterated.
   // Preconditions: The list is initialized and has been reset since 
   //                inserting an item.
   // Postconditions: Returns an object of type T that was appended to the list
   // Paramaters: none
   T getNextItem();
   
   // Method reports if the given object is in the list.
   // Preconditions: List has been initialized.
   // Postconditions: Returns true if the given object is in the list, false
   //                 otherwise.
   // Paramaters: T: object to be searched for.
   bool inList(const T&);
   
   // Method returns the amount of a certain object in the list.
   // Preconditions: List has been initialized.
   // Postconditions: Number of specific object is tallied and returned.
   // Paramaters: T: Item to be tallied.
   int count(const T&);
   
   // Method returns the first index of the given object.
   // Preconditions: List has been initialized.
   // Postconditions: Returns first index of given object if object exists 
   //                 within the list, returns -1 otherwise.
   // Paramaters: T: The object being searched for.
   int index(const T&);
   
   // Method returns the first index after given index of a given object.
   // Preconditions: List has been initialized
   // Postconditions: Returns the given object after the given index.
   // Paramaters: int: Starting index to search from.
   //             T: The object being searched for.
   int index(const int&, const T&);
   
   // Method removes the first instance of a given object.
   // Preconditions: List has been initialized.
   // Postconditions: The first instance of the given object has been deleted
   //                 from the list.
   // Paramaters: T: Object to be erased.
   void erase(const T&);
   
   // Method removes all instances of a given object.
   // Preconditions: List has been initialized.
   // Postconditions: All instances of a given object are removed from the list
   // Paramaters: T: Object to be removed.
   void remove(const T&);
   
   // Method overloads the bracket opearator ([])
   // Preconditons: List has been initialized
   // Postconditions: Object at given index is returned
   T& operator[](const int& index);
   
   // Method overloads the bracket operator ([]) for pass by reference
   //   functions.
   // Preconditions: List has been initialized and sent over a pass by
   //                reference function.
   // Postconditions: Object at given index is returned
   const T& operator[](const int& index) const;
   
private:
   typename list<T>::iterator traversingIt;
};//End class SortedList

/************************CLASS IMPLEMENTATION*************************
 **************************PUBLIC METHODS*****************************/
template <class T>
void SortedList<T>::insert(const T& item)
{
   typename list<T>::iterator i;
   i = list<T>::begin();
   
   if( list<T>::empty() )
      list<T>::push_front( item );
   else
   {
      while( (*i < item) && (i != list<T>::end()) )
      {
         i++;
      }//End while loop
      
      list<T>::insert(i, item);
   }//End else statement
}//End insert

template <class T>
void SortedList<T>::traverse( void (*somefunc)(T&) )
{
   typename list<T>::iterator it;
   for (it=list<T>::begin(); it!=list<T>::end(); it++)
      somefunc(*it);
}//End traverse

template <class T>
T& SortedList<T>::operator[](const int& index)
{
   typename list<T>::iterator it;
   it = list<T>::begin();
   for(int i = 0; i<index; i++)
   {
      it++;
   }//End for loop
   
   return (*it);
}//End operator[] overload

template <class T>
const T& SortedList<T>::operator[](const int& index) const
{
   typename list<T>::const_iterator it;
   it = this->begin();
   for(int i = 0; i<index; i++)
   {
      it++;
   }//End for loop
   
   return (*it);
}//End operator[] overload pass by reference

template <class T>
bool SortedList<T>::inList(const T& object)
{
   typename list<T>::const_iterator it;
   it = list<T>::begin();
   
   while( it != list<T>::end() )
   {
      if( (*it) == object )
         return true;
      it++;
   }//End while loop
   
   return false;
}//End inList

template <class T>
int SortedList<T>::count(const T& object)
{
   typename list<T>::iterator it;
   it = list<T>::begin();
   int i = 0;
   
   while( it!=list<T>::end() )
   {
      if( *it == object)
         i++;
      it++;
   }//End while loop
   
   return i;
}//End count

template <class T>
void SortedList<T>::erase(const T& object)
{
   typename list<T>::iterator it;
   it = list<T>::begin();
   
//   cout << "In SortedList." << endl;
   while( *it != object && it != list<T>::end() )
   {
      it++;
   }//end while loop
   
   if( *it == object )
   {
      list<T>::erase(it);
   }//end if statement
   
//  cout << "At end of SortedList." << endl;
}//End erase

template <class T>
void SortedList<T>::remove(const T& object)
{

   typename list<T>::iterator it;
   it = list<T>::begin();
   
   while( it != list<T>::end() )
   {
      while( *it == object )
      {
         it = list<T>::erase(it);
      }//End while loop
      it++;
   }//End while loop
}//End remove

template <class T>
void SortedList<T>::reset()
{
   traversingIt = list<T>::begin();
}//End reset

template <class T>
bool SortedList<T>::endOfList() const
{
   return( traversingIt == list<T>::end() );
}//End endOfList()

template <class T>
T SortedList<T>::getNextItem()
{
   T returnValue;
   returnValue = (*traversingIt);
   traversingIt++;
   return(returnValue);
}//End getNextItem

template <class T>
int SortedList<T>::index(const T& value)
{
   int i = 0;
   typename list<T>::iterator it;
   it = list<T>::begin();
   
   while( *it!=value && it!=list<T>::end() )
   {
      i++;
      it++;
   }//End while loop
   
   if( it == list<T>::end() )
      return(-1);
   return i;
}//End index

template <class T>
int SortedList<T>::index(const int& givenPos, const T& value)
{
   int i = givenPos;
   typename list<T>::iterator it;
   it = list<T>::begin();
   for(int y = 0; y<i; y++)
      it++;
   while( (*it)!=value && it!=list<T>::end() )
   {
      i++;
      it++;
   }//End while loop
   if( it == list<T>::end() )
      return(-1);
   return i;
}//End index