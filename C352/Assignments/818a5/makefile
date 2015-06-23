# File:     makefile
# Author:   Nathan Richgels

# Description
# This makefile will make the example program of an Array class.

CC=g++
OBJECTS=main.cpp
EXE=prog5

$(EXE):		main.cpp sortedlist.h
		$(CC) -o $(EXE) $(OBJECTS)
clean:
		rm -rf *.o core.* $(EXE)

