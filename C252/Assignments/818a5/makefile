# Nathan Richgels
# CSIS 252 - Asmt #5

EXE = prog5
CC = g++
OBJECTS = main.o read.o Summary.o output.o

$(EXE): $(OBJECTS)
	$(CC) -o $(EXE) $(OBJECTS)

main.o:  main.cpp structs.h constants.h prototypes.h
	$(CC) -c main.cpp
read.o:  read.cpp structs.h constants.h
	$(CC) -c read.cpp
output.o: output.cpp structs.h
	$(CC) -c output.cpp
Summary.o: Summary.cpp structs.h
	$(CC) -c Summary.cpp
clean:
	rm -rf *.o core.* $(EXE)
