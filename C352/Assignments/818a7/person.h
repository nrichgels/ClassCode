#ifndef __PERSON_H__
#define __PERSON_H__

#include <iostream>
#include <string>
#include "date.h"
using namespace std;

class Person
{
public:
   
   // Constructor
   // Creates a Person with the given Name, BirthDate, and Social Security
   //  Number.
   explicit Person(const string&, const Date&,const string&);
   
   // Constructor
   // Creates a Person with no pre-inserted information.
   explicit Person();
   
   // Sets the person's name.
   // Preconditions: Person has been initialized,
   //                first paramater is a legal string.
   // Postconditions: The name of the Person is set to given string.
   void setName(const string&);
   
   // Sets the person's Birth Date.
   // Preconditions: Person has been initialized,
   //                first paramater is a legal Date
   // Postconditions: The Person's BirthDate is set to the given Date.
   void setBirthDate(const Date&);
   
   // Sets the person's Social Security Number.
   // Preconditions: Person has been initialized,
   //                first paramater is a legal string.
   // Postconditions: The Person's Social Security is equl to the given string
   void setSS(const string&);
   
   // Returns the name of the Person.
   // Preconditions: Person has been initialized,
   //                Name has been set.
   // Postconditions: Name was returned.
   string getName() const;
   
   // Returns the Person's BirthDate
   // Preconditions: Person has been initialized,
   //                Birth Date has been set
   // Postconditions: Date was returned
   Date getBirthDate() const;
   
   // Returns the Person's Social Security Number
   // Preconditions: Person has been initialized,
   //                Social Security Number has been set.
   // Postconditions: Social Security number has been returned.
   string getSS() const;
private:
   string name;
   Date birthDate;
   string SS; //Social Security

}; //End class Person

#endif