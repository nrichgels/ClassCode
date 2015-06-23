# File:     makefile
# Author:   Nathan Richgels

# Description
# This makefile will make the example program of a money class

CC=g++
OBJECTS=main.o money.o
EXE=prog1

$(EXE):		$(OBJECTS)
		$(CC) -o $(EXE) $(OBJECTS)
main.o: 	main.cpp money.h
		$(CC) -c main.cpp
money.o:	money.cpp money.h
		$(CC) -c money.cpp
clean:
		rm -rf *.o core.* $(EXE)

