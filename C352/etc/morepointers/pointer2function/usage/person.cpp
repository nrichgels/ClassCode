// File:    person.cpp
// Author:  Dan Brekke

#include "person.h"

Person::Person(const string& namestr,int type)
{
	setName(namestr);
	switch (type)
	{
	   case 1: UtilityFunction=function1; break;
	   case 2: UtilityFunction=function2; break;
	   case 3: UtilityFunction=function3; break;
	   case 4: UtilityFunction=function4; break;
	}
}

string Person::getName() const
{
	return name;
}

void Person::setName(const string& namestr)
{
	name = namestr;
}

