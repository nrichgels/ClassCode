#ifndef _DERIVED_H
#define _DERIVED_H
#include "base.h"

class Derived : public Base
{
   public:
      Derived(double val1, double val2);
      void setY(double);
      double getY() const;
      void print() const;
   private:
      double Y;
};
#endif
