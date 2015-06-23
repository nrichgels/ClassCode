// Author: Nathan Richgels
// File: rectangle.h
// Date: 2/28/2012
// Class: CSIS252
// Assignment 6

#ifndef _RECTANGLE_H_
#define _RECTANGLE_H_

class Rectangle
{
   public:

      // method - constructor
      // description - construct a new Rectangle object
      // precondition - none
      // postcondition - Rectangle object created and initialized to
      //  specified width & length, or 0 by default.
      // method input - length: double, width: double
      // mehtod output - none
      Rectangle(double=0, double=0);

      // method - Length
      // description - returns the length of the Rectangle object.
      // preconditions - Rectangle Object has been initialized.
      // postconditions - Rectangle Object Length has been returned.
      // method input - none
      // method output - Length of Rectangle: double
      double Length() const;

      // method - setLength
      // description - Changes the length of the Rectangle Object
      // preconditions - Rectangle Object has been formed
      // postconditions: New Rectangle Object length is set
      // method input - Length of the Rectangle: double
      // method output - none
      void setLength(double);

      // method - Width
      // desciription - Returns the Width of the Rectangle Object
      // preconditions - Rectangle Object has been initialized
      // postconditions - Rectangle Object length has been returned
      // method input - none
      // method output - Width of the Rectangle: double
      double Width() const;

      // method - setWidth
      // description - Changes the width of the Rectangle Object
      // preconditions - Rectangle Object has been formed
      // postconditions: New Rectangle Object width is set
      // method input - Width of the Rectangle: double
      // method output - none
      void setWidth(double);

      // method - Area
      // description - Returns the area of the Rectangle
      // preconditions - Rectangle Object has been formed
      // postconditions - Area of the Rectangle has been returned
      // method input - None
      // method output - Area of the Rectangle: double
      double Area() const;

      // method - Perimeter
      // description - Returns the perimeter of the Rectangle
      // preconditions - Rectangle Object has been formed
      // postconditions - Perimeter of the Rectangle has been returned
      // method input - None
      // method output - Perimter of the Rectangle: double
      double Perimeter() const;

      bool operator==(const Rectangle&) const;

      bool operator>=(const Rectangle&) const;

      bool operator>(const Rectangle&) const;

      bool operator<=(const Rectangle&) const;

      bool operator<(const Rectangle&) const;

      bool operator!=(const Rectangle&) const;

   private:

      double width;
      double length;
};

ostream& operator<<(ostream& out, const Rectangle&);
#endif
