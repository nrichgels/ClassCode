# File:     makefile
# Author:   Nathan Richgels

# Description
# This makefile will make the example program of an Array class.

CC=g++
OBJECTS=main.cpp
EXE=prog3

$(EXE):		main.cpp array.h
		$(CC) -o $(EXE) $(OBJECTS)
clean:
		rm -rf *.o core.* $(EXE)

