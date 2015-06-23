// Shape is an abstract base class.  It is abstract because it contains
// a pure virtual method (abstract method).

#ifndef SHAPE_H
#define SHAPE_H

class Shape
{
   public:
      Shape( int = 0, int = 0 );
      virtual void Display() const;
      virtual double Area() const=0; // abstract method
   private:
      int x;
      int y;
};

#endif

