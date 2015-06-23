EXE = prog10
CC = g++
OBJECTS = converter.o main.o

$(EXE): $(OBJECTS)
	$(CC) -o $(EXE) $(OBJECTS)

converter.o: converter.cpp converter.h
	$(CC) -c  converter.cpp

main.o: main.cpp converter.cpp converter.h
	$(CC) -c main.cpp

clean:
		rm -rf $(EXE) $(OBJECTS) core.*