#include <iostream>

using namespace std;

#include "circle.h"

Circle::Circle(double radiusValue, int xValue, int yValue)
   : Shape( xValue, yValue )
{
   radius=radiusValue;
}

double Circle::Area() const
{
   return 3.14159 * radius * radius;
}

void Circle::Display() const
{
   cout << "Center = ";
   Shape::Display();
   cout << "; Radius = " << radius << endl;
}

double Circle::Radius() const
{
   return radius;
}

