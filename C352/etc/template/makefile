# name
# class
# etc.

CC = g++
CFLAGS = 
LFLAGS = 

OBJECTS = main.o

prog:		$(OBJECTS)
		$(CC) -o prog $(OBJECTS) $(LFLAGS)

main.o:		main.cpp list.h list.cpp
		$(CC) $(CFLAGS) -c main.cpp


clean:		
		rm -rf prog core.* $(OBJECTS)
