#include "structs.h"

#ifndef _PROTOTYPES_H_
#define _PROTOTYPES_H_

void read(EmployeeData Employees[], int& count);
SummaryData Summary(const EmployeeData Employees[], int count);
void outputData(const EmployeeData employees[], int count, SummaryData Totals);

#endif
