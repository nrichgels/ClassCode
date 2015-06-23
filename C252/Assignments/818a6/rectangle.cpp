// Author: Nathan Richgels
// File: rectangle.cpp
// Date: 2/28/2012
// Class: CSIS252
// Assignment 6
#include <iostream>
#include <iomanip>
using namespace std;
#include "rectangle.h"

// Relational operator overloads:

ostream& operator<<(ostream& out, const Rectangle& rec)
{
  //We assume the programmer wants to see the area when printing.
   out << rec.Area();
}

// For boolean over-riding, we use the Area methods to compare
// the double to determine what is "equal to" "greater than"
// and "less than".
bool Rectangle::operator==(const Rectangle& other) const
{
   return Area() == other.Area();
}

bool Rectangle::operator>=(const Rectangle& other) const
{
   return Area() >= other.Area();
}

bool Rectangle::operator>(const Rectangle& other) const
{
   return Area()>other.Area();
}

bool Rectangle::operator<=(const Rectangle& other) const
{
   return Area()<=other.Area();
}

bool Rectangle::operator<(const Rectangle& other) const
{
   return Area()<other.Area();
}

bool Rectangle::operator!=(const Rectangle& other) const
{
   return Area()!=other.Area();
}


/* Class:  */
Rectangle::Rectangle(double initialLength, double initialWidth)
{
   // Uses the methods later defined to set initial parameters
   setWidth(initialWidth);
   setLength(initialLength);
}


// Calls and reports the private arribute, length.
double Rectangle::Length() const
{
   return length;
}

// Changes the private arribute, length.
void Rectangle::setLength(double changeLength)
{
   length=changeLength;
}

// Calls and returns the private attribute, width.
double Rectangle::Width() const
{
   return width;
}

// Changes the private attribute, width.
void Rectangle::setWidth(double changeWidth)
{
   width=changeWidth;
}

// Multiplies the two private attributes- length and width- then
// returns that value to calculate area for the methods.
double Rectangle::Area() const
{
   double area;
   area= width * length;
   return area;
}

// Doubles the private attributes- length and width- and adds them together
// to simulate the four sides of a rectangle being added together.
double Rectangle::Perimeter() const
{
   double perimeter;
   perimeter = (2*length) + (2 * width);
   return perimeter;
}
