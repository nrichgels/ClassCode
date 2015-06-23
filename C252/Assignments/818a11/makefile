EXE = prog11
CC = g++
OBJECTS = functions.o main.o

$(EXE): $(OBJECTS)
	$(CC) -o $(EXE) $(OBJECTS)

functions.o: queueType.h stackType.h constants.h functions.cpp
	$(CC) -c functions.cpp
main.o: prototypes.h constants.h main.cpp
	$(CC) -c main.cpp
clean:
		rm -rf $(EXE) $(OBJECTS) core.*