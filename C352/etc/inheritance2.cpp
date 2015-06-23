#include <iostream>
#include <list>
using namespace std;

template <class T>
class myList : public list<T>
{
   public:
      void traverse ( void (*) (T&) );
      void print() const;
      void insert(const T&);
};

template <class T>
void myList<T>::traverse( void (*visit) (T&))
{
   typename list<T>::iterator p;
   for (p=this->begin(); p!=list<T>::end(); p++)
      visit(*p);
}

template <class T>
void myList<T>::print() const
{
   typename list<T>::const_iterator p;  // could use class instead of typename
   for (p=this->begin(); p!=list<T>::end(); p++)
      cout << *p << ' ';
   cout << endl;
}

template <class T>
void myList<T>::insert(const T& item)
{
   list<T>::insert(list<T>::end(),item);
}

void increment(int& num)
{
   num++;
}
void output(int& num)
{
   cout << "value: " << num << endl;
}
int main()
{
   myList<int> x;
   x.insert(4);
   x.insert(12);
   x.insert(7);
   x.insert(9);
   x.print();
   x.traverse(increment);
   x.traverse(output);
   return 0;
}

