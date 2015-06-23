#include <iostream>
using namespace std;
#include "student.h"

Student::Student(string Name, int ID)
{
   Person::setName(Name);
   setID(ID);
}

Student::Student()
{
}

void Student::setID(int ID)
{
   id=ID;
}

int Student::ID() const
{
   return id;
}

bool Student::operator==(const Student& other) const
{
   return(ID()==other.ID());
}

bool Student::operator!=(const Student& other) const
{
   return(ID()!=other.ID());
}

bool Student::operator<(const Student& other) const
{
   return(ID()<other.ID());
}

bool Student::operator<=(const Student& other) const
{
   return(ID()<=other.ID());
}

bool Student::operator>(const Student& other) const
{
   return(ID()>other.ID());
}

bool Student::operator>=(const Student& other) const
{
   return(ID()>=other.ID());
}
