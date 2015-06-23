// File:     circle.h
// Author:   Dan Brekke

// Description
// This file contains the specification for a circle class

#ifndef _CIRCLE_H_
#define _CIRCLE_H_

const double PI = 3.141592654;
using namespace std;

class Circle
{
   public:
      Circle(double=0);  // constructor with default radius
      void setRadius(double);
      double radius() const;
      double diameter() const;
      double area() const;
      double circumference() const;
   private:
      double rad;
};


// implementation for a circle class

Circle::Circle(double r)
{
   rad = r;
}

void Circle::setRadius(double r)
{
   rad = r;
}

double Circle::radius() const
{
   return rad;
}

double Circle::diameter() const
{
   return rad*2;
}

double Circle::area() const
{
   return PI*rad*rad;
}

double Circle::circumference() const
{
   return 2*PI*rad;
}


#endif
