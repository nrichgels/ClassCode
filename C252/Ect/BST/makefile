# File:     makefile
# Author:   Dan Brekke

# Description
# This makefile will compile the program

CC=g++
OBJECTS=main.o 
prog:		$(OBJECTS)
		$(CC) -o prog $(OBJECTS)
main.o: 	main.cpp binarySearchTree.h binaryTree.h bst.h
		$(CC) -c main.cpp
clean:
		rm -rf *.o core.* prog

