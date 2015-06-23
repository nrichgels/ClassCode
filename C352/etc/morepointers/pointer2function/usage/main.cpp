// File:    main.cpp
// Author:  Dan Brekke

#include <iostream>
#include <string>
#include "person.h"
using namespace std;


int main()
{
    string name = "John Doe";
    int persontype = 3;
    Person p1(name,persontype);
    p1.UtilityFunction();

    Person p2("Jane Doe",2);
    p2.UtilityFunction();

    return 0; 
} // end main

