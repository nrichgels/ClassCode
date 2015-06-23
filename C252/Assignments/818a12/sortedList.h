#ifndef __SORTED_LIST_H__
#define __SORTED_LIST_H__
#include <iostream>
using namespace std;
#include "linkedList.h"
#include "linkedList2.h"

template <class T>
class sortedListType : public linkedListType2<T>
{
   public:
      void insert(const T& item);
};

template <class T>
void sortedListType<T>::insert(const T& item)
{
   T Spare;
   int c=0;
   if(linkedListType<T>::isEmptyList())
     {insertFirst(item);}

   else
      if(item>=linkedListType<T>::back())
         {linkedListType<T>::insertLast(item);}

      else
        {linkedListType2<T>::retrieveAt(c, Spare);
         while(item>=Spare && c<=linkedListType2<T>::length())
           {c++;
            retrieveAt(c, Spare);}
            linkedListType2<T>::insertAt(c, item);}
}
#endif
