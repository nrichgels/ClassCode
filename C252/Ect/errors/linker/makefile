# File:     makefile
# Author:   Dan Brekke

# Description
# This makefile will make the example program of a circle class

CC=g++
OBJECTS=main.o func.o
prog:		$(OBJECTS)
		$(CC) -o prog $(OBJECTS)
main.o: 	main.cpp circle.h
		$(CC) -c main.cpp
func.o: 	func.cpp circle.h
		$(CC) -c func.cpp
clean:
		rm -rf *.o core.* prog

