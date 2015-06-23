#ifndef _LIST_H_
#define _LIST_H_

namespace ListNameSpace
{

template <class T>
class List
{
   public:
      explicit List(int size=99);
      ~List(); // destructor
      List (const List&); // copy constructor
      const List& operator = (const List&); // operator =

      void add(T num); // add to end of the list
      T remove();      // remove and return the last int in the list
   private:
      int size;          // size of dynamically allocated array
      int count;         // current number of ints in the array
      T *thelist;      // dynamically allocated array
};
 
}
#include "list.cpp"
#endif
