#include "employees.h"

// Reads information from an ifstream and stores it in employees
// preconditions: ifstream in is in a proper format (check README),
//                ifstream is the first paramater,
//                Employees is the second paramater
// postconditions: given contents of ifstream object is stored in given
//                 Employees object
void read(ifstream& in, Employees& employees);

// Tries to open file provided in argv[1].  Returns true if successful, false
//  otherwise.
// preconditions: int is first paramater,
//                char* array is second paramater.
//                ifstream is third paramater.
// postconditions: returns true if ifstream object was able to hold and object
//                 from argv[1] and if argc is equl to 2.
//                 returns false otherwise.
bool openFiles(int argc, char *argv[], ifstream &input);

