CC=g++
OBJECTS=circle.o shape.o main.o rectangle.o square.o

prog:		$(OBJECTS)
		$(CC) -o prog $(OBJECTS)

main.o:		main.cpp circle.o shape.o rectangle.o square.o
		$(CC) -c main.cpp

circle.o:	circle.cpp circle.h shape.h shape.cpp
		$(CC) -c circle.cpp

rectangle.o:	rectangle.cpp rectangle.h shape.h shape.cpp
		$(CC) -c rectangle.cpp

square.o:	square.h square.cpp rectangle.cpp rectangle.h
		$(CC) -c square.cpp

shape.o:	shape.cpp shape.h
		$(CC) -c shape.cpp

clean:
		rm -rf core.* prog $(OBJECTS)
