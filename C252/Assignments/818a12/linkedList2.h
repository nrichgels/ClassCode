#ifndef _LINKEDLIST2_H_
#define _LINKEDLIST2_H_
#include <iostream>
#include "linkedList.h"
using namespace std;

template <class T>
class linkedListType2 : public linkedListType<T>
{
   public:
      void insertAt(int position, const T& newItem);
      void retrieveAt(int position, T& item) const;
};

template <class T>
void linkedListType2<T>::retrieveAt(int position,T& item) const
{
   if (position >= linkedListType<T>::length() || position < 0)
      cout << "error: position not in list\n";
   else
   {
      nodeType<T>* p = linkedListType<T>::first;
      for (int i=0; i<position; i++)
         p = p->link;
      item = p->info;
   }
}

template <class T>
void linkedListType2<T>::insertAt(int position, const T& newItem)
{
   if (position > linkedListType<T>::count || position < 0)
      cout << "error: invalid list position in insertAt\n";
   else
   {
      linkedListType<T>::count++;
      nodeType<T>* newNode = new nodeType<T>;
      newNode->info = newItem;
      newNode->link = NULL;
      if (linkedListType<T>::isEmptyList())
      {
         linkedListType<T>::first = newNode;
         linkedListType<T>::last = newNode;
      }
      else
      {
         nodeType<T>* current = linkedListType<T>::first;
         nodeType<T>* previous = NULL;
         for (int i = 0; i<position; i++)
         {
            previous = current;
            current = current->link;
         }
         newNode->link = current;
         if (previous == NULL)
            linkedListType<T>::first = newNode;
         else
            previous->link = newNode;
         if (current == NULL)
            linkedListType<T>::last = newNode;
      }
   }
}

#endif
