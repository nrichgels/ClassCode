#include <iostream>
#include "base.h"

Base::Base(double val) : X(val)
{}

void Base::setX(double val)
{
   X = val;
}

double Base::getX() const
{
   return X;
}

void Base::print() const
{
   cout << "X = " << getX() << endl;
}


