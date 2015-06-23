#include <iostream>

using namespace std;

#include "rectangle.h"

Rectangle::Rectangle(double lengthValue, double widthValue,
                     int xValue, int yValue)
   : Shape( xValue, yValue )
{
   length=lengthValue;
   width=widthValue;
}

double Rectangle::Area() const
{
   return length * width;

}

void Rectangle::Display() const
{
   cout << "Center = ";
   Shape::Display();
   cout << "; Length = " << length;
   cout << "; Width = " << width << endl;
}

