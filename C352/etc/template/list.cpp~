#include <iostream>
using namespace std;
namespace ListNameSpace
{

// constructor
template <class T>
List<T>::List(int s)
{
   thelist = new T[s];
   count=0;
   size = s;
}

// destructor
template <class T>
List<T>::~List()
{
   delete [] thelist;
   thelist = NULL;
}

// copy constructor
template <class T>
List<T>::List(const List<T>& list)
{
   thelist = new T[list.size];
   count = list.count;
   size = list.size;
   for (int i=0; i<count; i++)
      thelist[i] = list.thelist[i];
}

// operator=
template <class T>
const List<T>& List<T>::operator= (const List<T>& list)
{
   if (&list == this)
   {
      return *this;
   }
   delete [] thelist;
   thelist = new T[list.size];
   count = list.count;
   size = list.size;
   for (int i=0; i<count; i++)
      thelist[i] = list.thelist[i];
   return *this;
}
   

template <class T>
void List<T>::add(T num)
{
   thelist[count] = num;
   count++;
}

template <class T>
T List<T>::remove()
{
   count--;
   T temp=thelist[count];
   return temp;
}

}
