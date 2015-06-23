#include <iostream>

using namespace std;

#include "shape.h"

Shape::Shape( int xValue, int yValue )
{
   x=xValue;
   y=yValue;
}

void Shape::Display() const
{
   cout << '[' << x << ',' << y << ']';
}

