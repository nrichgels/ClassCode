EXE = prog6
CC = g++
OBJECTS = main.o rectangle.o

$(EXE): $(OBJECTS)
	$(CC) -o $(EXE) $(OBJECTS)

main.o: main.cpp rectangle.h
	$(CC) -c main.cpp
rectangle.o: rectangle.cpp rectangle.h
	$(CC) -c rectangle.cpp