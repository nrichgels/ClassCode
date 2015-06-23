EXE = prog7
CC = g++
OBJECTS = main.o date.o person.o hourlyemployee.o employees.o employee.o salaryemployee.o functions.o

$(EXE): $(OBJECTS)
	$(CC) -o $(EXE) $(OBJECTS)

main.o: prototypes.h date.h employee.h employees.h hourlyemployee.h person.h salaryemployee.h main.cpp
	$(CC) -c main.cpp

date.o: date.h date.cpp
	$(CC) -c date.cpp

employee.o: employee.cpp employee.h person.h date.h
	$(CC) -c employee.cpp

employees.o: employees.cpp employees.h person.h date.h person.h salaryemployee.h hourlyemployee.h
	$(CC) -c employees.cpp

hourlyemployee.o: hourlyemployee.cpp person.h employee.h
	$(CC) -c hourlyemployee.cpp

salaryemployee.o: salaryemployee.cpp salaryemployee.h person.h employee.h
	$(CC) -c salaryemployee.cpp

person.o: person.cpp person.h
	$(CC) -c person.cpp

functions.o: functions.cpp hourlyemployee.h salaryemployee.h prototypes.h
	$(CC) -c functions.cpp
clean:
		rm -rf $(EXE) $(OBJECTS) core.*
