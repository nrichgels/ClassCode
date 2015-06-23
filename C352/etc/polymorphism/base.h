#ifndef _BASE_H
#define _BASE_H
#include <iostream>
using namespace std;

class Base
{
   public:
      Base(double);
      void setX(double);
      double getX() const;
      virtual void print() const;
   private:
      double X;
};

#endif
