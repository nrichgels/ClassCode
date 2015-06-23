OBJECTS=main.o
CC=g++

prog:		$(OBJECTS)
		$(CC) -o prog $(OBJECTS)

main.o:		main.cpp heap.h
		$(CC) -c main.cpp

clean:
		rm -rf core *.o prog
