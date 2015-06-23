// Shape is an abstract base class
// the Circle class inherits from Shape
// the Rectangle class inherits from Shape
// the Square class inherits from Rectangle

#include <iostream>
#include <iomanip>

using namespace std;

#include "circle.h"
#include "rectangle.h"
#include "square.h"

void func(const Shape& s)
{
   s.Display();
   cout << "Area = " << s.Area() << endl << endl;
}

int main()
{
   Circle circle(2.5, 37, 43);
   cout << "Circle: ";
   circle.Display();
   cout << "Circle area: " << circle.Area() << endl << endl;

   Rectangle rec(2,4,8,9);
   cout << "Rectangle: ";
   rec.Display();
   cout << "Rectangle area: " << rec.Area() << endl << endl;

   Square square(4,6,5);
   cout << "Square: ";
   square.Display();
   cout << "Square area: " << square.Area() << endl << endl;

   Shape* p;
   p = &circle;
   cout << "Circle: ";
   p->Display();
   cout << "Circle: ";
   cout << "Area = " << p->Area() << endl;

   p = &rec;
   cout << "\nRectangle: ";
   p->Display();
   cout << "Rectangle: ";
   cout << "Area = " << p->Area() << endl;

   p = &square;
   cout << "\nSquare: ";
   p->Display();
   cout << "Square: ";
   cout << "Area = " << p->Area() << endl << endl;

   func(circle);
   func(rec);
   func(square);

   return 0;

}

