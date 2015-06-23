# Nathan Richgels
# CSIS 252 - Asmt #5

EXE = prog7
CC = g++
OBJECTS = main.o read.o Summary.o output.o employee.o sort.o

$(EXE): $(OBJECTS)
	$(CC) -o $(EXE) $(OBJECTS)

main.o: main.cpp structs.h constants.h prototypes.h employee.h
	$(CC) -c main.cpp
employee.o: employee.cpp constants.h employee.h
	$(CC) -c employee.cpp
read.o: read.cpp structs.h constants.h employee.h
	$(CC) -c read.cpp
Summary.o: Summary.cpp employee.h structs.h
	$(CC) -c Summary.cpp
output.o: output.cpp employee.h structs.h
	$(CC) -c output.cpp
sort.o: sort.cpp employee.h
	$(CC) -c sort.cpp