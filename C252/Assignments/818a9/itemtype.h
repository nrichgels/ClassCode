// Author: Nathan Richgels
// File: itemtype.h
// Date: 3/28/2012
// Class: CSIS252
// Assignment 9

#ifndef __PERSON_H__
#define __PERSON_H__


#include <iostream>
#include <iomanip>
using namespace std;
#include "date.h"

class Person
{
   public:
      //Methods:

      // Method - constructor
      // description - Constructs a new Person object.
      // precondition - none
      // postcondition - Person object is created, and is initialized with 
      //                 given name and Birth Date.
      // method input - Name; string, BirthDate; Date
      // method output - none
      Person(string Name, Date BirthDate);

      // Method - constructor
      // description - Constructs a new Person object.
      // precondition - none
      // postcondition - Person object is created with no default
      //                 paramaters.
      // method input - none
      // method output - none

      Person();

      // Method - setBirthdate
      // description - Sets the date of birth for the object.
      // precondition - The Person object has been initiated.
      // postcondition - The Person object has the given birthdate.
      // method input - Month; int, Day; int, Year; int
      // method output - none
      void setBirthdate(int, int , int);

      // Method - Birthdate
      // description - Outputs the birthdate of a Person Object
      // precondition - The person object's birthdate has been set.
      // postcondition - The person object's birthdate is returned
      // method input - none
      // method output - birthdate; date
      Date Birthdate() const;

      // Method - setName
      // description - Sets the name of a Person object
      // precondition - The Person object has been initialized
      // postcondition - The Person object has the given name
      // method input - Name; string
      // method output - none
      void setName(string);

      // Method - Name
      // description - returns the Name of a Person object
      // precondition - The Person object has a name
      // postcondition - The Person object's name is returned
      // method input - none
      // method output - Name; string
      string Name() const;

      // Method - getAge
      // description - calculates and returns the age of a Person
      //               object calculated with current date.
      // precondition - The Person object's birthdate has been
      //                entered.
      // postcondition - The Person object's age has been returned
      // method input - none
      // method output - Age; int
      int getAge();

      // operator overloads:
      bool operator==(const Person& other) const;

   private:
      string name;
      Date bdate;
      Date current;
};

// Stream Overloads:
ostream& operator<<(ostream& out, Person& person);
istream& operator>>(istream& in, Person& person);
typedef Person ITEM;
#endif


