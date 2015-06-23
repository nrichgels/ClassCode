# File:     makefile
# Author:   Nathan Richgels

# Description
# This makefile will make the example program of a Date class

CC=g++
OBJECTS=main.o date.o
EXE=prog2

$(EXE):		$(OBJECTS)
		$(CC) -o $(EXE) $(OBJECTS)
main.o: 	main.cpp
		$(CC) -c main.cpp
date.o:	date.cpp date.h
		$(CC) -c date.cpp
clean:
		rm -rf *.o core.* $(EXE)

