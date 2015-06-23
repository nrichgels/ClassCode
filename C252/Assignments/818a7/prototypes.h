#include "structs.h"

#ifndef _PROTOTYPES_H_
#define _PROTOTYPES_H_

void read(Employee Employees[], int& count);
SummaryData Summary(Employee Employees[], int count);
void outputData(Employee employees[], int count, SummaryData Totals);
void sort(Employee numbers[], int n);
#endif
