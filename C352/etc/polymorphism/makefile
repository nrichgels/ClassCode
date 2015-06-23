OBJECTS=main.o base.o derived.o
CC=g++
CFLAGS=
LFLAGS=

prog:		$(OBJECTS)
		$(CC) -o prog $(OBJECTS) $(LFLAGS)

main.o:		main.cpp base.o derived.o
		$(CC) $(CFLAGS) -c main.cpp

base.o:		base.cpp base.h
		$(CC) $(CFLAGS) -c base.cpp

derived.o:	derived.cpp derived.h base.o
		$(CC) $(CFLAGS) -c derived.cpp

clean:
		rm -rf core *.o prog
