// File:    person.h
// Author:  Dan Brekke

#ifndef _PERSON_
#define _PERSON_
#include <string>
#include "utility.h"
using namespace std;

class Person
{
	public:
	    Person(const string& ="",int=1);
	    string getName() const;
	    void setName(const string&);
	    void (*UtilityFunction) (void);
	private:
	    string name;
};
#endif

