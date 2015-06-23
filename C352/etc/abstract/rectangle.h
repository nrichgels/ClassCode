#ifndef RECTANGLE_H
#define RECTANGLE_H

#include "shape.h"

class Rectangle : public Shape
{
   public:
      Rectangle(double=0.0, double=0.0, int = 0, int = 0);
      double Area() const;
      void Display() const;
   private:
      double length;
      double width;
};

#endif

