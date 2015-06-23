#include "derived.h"

Derived::Derived(double val1, double val2) : Base(val1), Y(val2)
{ }

void Derived::setY(double val)
{
   Y = val;
}

double Derived::getY() const
{
   return Y;
}

void Derived::print() const
{
   Base::print();
   cout << "Y = " << getY() << endl;
}

