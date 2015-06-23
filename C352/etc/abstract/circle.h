#ifndef CIRCLE_H
#define CIRCLE_H

#include "shape.h"

class Circle : public Shape
{
   public:
      Circle(double=0.0, int = 0, int = 0);
      double Area() const;
      void Display() const;
      double Radius() const;
   private:
      double radius;
};

#endif

