// File:     circle.cpp
// Author:   Dan Brekke
// Date: 

// Description
// This file contains the implementation for a circle class

#include "circle.h"
#include <iostream>
using namespace std;

ostream& operator << (ostream& out, const Circle& c)
{
//   out << "Area: " << c.area() << endl;
   out << c.radius();  // better
   return out; 
}

istream& operator >> (istream& in, Circle& c)
{
   double r;
   in >> r;
   c.setRadius(r);
   return in; 
}


bool Circle::operator==(const Circle& other) const
{
//   return rad == other.rad;
   return radius() == other.radius(); // better
}

Circle::Circle(double r)
{
   setRadius(r);
}

Circle::Circle()
{
   setRadius(0);
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
   return radius()*2;
}

double Circle::area() const
{
   return PI*radius()*radius();
}

double Circle::circumference() const
{
   return 2*PI*radius();
}
