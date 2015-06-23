#include "person.h"
#include <string>
#include <iostream>
using namespace std;

Person::Person(const string& Name,const Date& BirthDay,const string& SocialSecurity)
{
   name =  Name;
   birthDate = BirthDay;
   SS = SocialSecurity;
}//End Constructor

Person::Person()
{
   
}

void Person::setName(const string& Name)
{
   name = Name;
}//End setName

void Person::setBirthDate(const Date& BirthDay)
{
   birthDate = BirthDay;
}//End setBirthDate

void Person::setSS(const string& SocialSecurity )
{
   SS = SocialSecurity;
}//End setSS

string Person::getName() const
{
   return name;
}//End getName

Date Person::getBirthDate() const
{
   return birthDate;
}//End getBirthDate

string Person::getSS() const
{
   return SS;
}//End getSS;