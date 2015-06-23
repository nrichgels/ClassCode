#ifndef _HEAP_H_
#define _HEAP_H_

const int MAX_HEAP = 100;
#include <stdexcept>
#include <string>
using namespace std;

class HeapException;

template <class HeapItemType>
class Heap
{
   public:
      Heap(); // default constructor

      virtual bool heapIsEmpty() const;
      // Determines whether a heap is empty.
      // Precondition: None.
      // Postcondition: Returns true if the heap is empty;
      // otherwise returns false.

      virtual void heapInsert(const HeapItemType& newItem)
                              throw(HeapException);
      // Inserts an item into a heap.
      // Precondition: newItem is the item to be inserted.
      // Postcondition: If the heap was not full, newItem is
      // in its proper position; otherwise HeapException is
      // thrown.

      virtual void heapDelete(HeapItemType& rootItem)
                              throw(HeapException);
      // Retrieves and deletes the item in the root of a heap.
      // This item has the largest search key in the heap.
      // Precondition: None.
      // Postcondition: If the heap was not empty, rootItem
      // is the retrieved item, the item is deleted from the
      // heap, and the function returns true. However, if the
      // heap is empty, removal is impossible and the function
      // throws HeapException.

      void dump(); // added for demonstration purposes only

   protected:
      void heapRebuild(int root);
      // Converts the semiheap rooted at index root
      // into a heap.

   private:
      HeapItemType items[MAX_HEAP]; // array of heap items
      int          size;            // number of heap items
}; 


template <class HeapItemType>
Heap<HeapItemType>::Heap() : size(0)
{
} // end default constructor

template <class HeapItemType>
bool Heap<HeapItemType>::heapIsEmpty() const
{
   return bool(size == 0);
} // end heapIsEmpty

template <class HeapItemType>
void Heap<HeapItemType>::heapInsert(const HeapItemType& newItem) 
                         throw(HeapException)
// Method: Inserts the new item after the last item in the
// heap and trickles it up to its proper position. The
// heap is full when it contains MAX_HEAP items.
{
   if (size >= MAX_HEAP)
      throw HeapException("HeapException: Heap full");
   // place the new item at the end of the heap
   else {
   items[size] = newItem;

   // trickle new item up to its proper position
   int place = size;
   int parent = (place - 1)/2;
   while ( (parent >= 0) &&
           (items[place] > items[parent]) )
   {  // swap items[place] and items[parent]
      HeapItemType temp = items[parent];
      items[parent] = items[place];
      items[place] = temp;

      place = parent;
      parent = (place - 1)/2;
   } // end while

   ++size;}
} // end heapInsert

template <class HeapItemType>
void Heap<HeapItemType>::heapDelete(HeapItemType& rootItem) 
                         throw(HeapException)
// Method: Swaps the last item in the heap with the root
// and trickles it down to its proper position.
{
   if (heapIsEmpty())
      throw HeapException("HeapException: Heap empty");
   else
   {  rootItem = items[0];
      items[0] = items[--size];
      heapRebuild(0);
   } // end if
} // end heapDelete

template <class HeapItemType>
void Heap<HeapItemType>::heapRebuild(int root)
{
   // if the root is not a leaf and the root's search key
   // is less than the larger of the search keys in the
   // root's children
   int child = 2 * root + 1; // index of root's left
                             // child, if any

   if ( child < size )
   {  // root is not a leaf, so it has a left child at child
      int rightChild = child + 1; // index of right child,
                                  // if any

      // if root has a right child, find larger child
      if ( (rightChild < size) &&
           (items[rightChild] > items[child]) )
         child = rightChild; // index of larger child

      // if the root's value is smaller than the
      // value in the larger child, swap values
      if ( items[root] < items[child] )
      {  HeapItemType temp = items[root];
         items[root] = items[child];
         items[child] = temp;

         // transform the new subtree into a heap
         heapRebuild(child);
      } // end if
   } // end if

   // if root is a leaf, do nothing
} // end heapRebuild
// End of implementation file.

// The following method was added for
// demonstration purposes only.
#include <iostream>
#include <iomanip>
using namespace std;
template <class HeapItemType>
void Heap<HeapItemType>::dump()
{
    for (int i=0; i<size; i++)
        cout << "array[" << setw(2) << i
        << "] = " << items[i] << endl;
}



class HeapException: public logic_error
{
public:
   HeapException(const string & message = "")
                        : logic_error(message.c_str())
   { }
};  // end HeapException

#endif

