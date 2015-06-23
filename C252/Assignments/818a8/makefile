# Author: Nathan Richgels
EXE = prog8
CC = g++
OBJECTS = main.o date.o

$(EXE): $(OBJECTS)
	$(CC) -o $(EXE) $(OBJECTS)

main.o: main.cpp date.h
	$(CC) -c main.cpp

date.o: date.cpp date.h
	$(CC) -c date.cpp

clean:
		rm -rf $(EXE) $(OBJECTS) core.*