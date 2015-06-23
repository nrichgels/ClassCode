#ifndef __student_h__
#define __student_h__
#include "person.h"
#include <iostream>
using namespace std;

class Student: public Person
{
   public:
      Student(string Name, int DragonID);
      Student();
      void setID(int ID);
      int ID() const;
      bool operator== (const Student& other) const;
      bool operator>= (const Student& other) const;
      bool operator<= (const Student& other) const;
      bool operator>  (const Student& other) const;
      bool operator<  (const Student& other) const;
      bool operator!= (const Student& other) const;
   private:
      int id;
};

#endif
