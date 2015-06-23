CC=g++
CFLAGS=
LFLAGS=
OBJECTS=	main.o peter.o stewie.o
prog:		$(OBJECTS)
		$(CC) $(CFLAGS) -o prog $(OBJECTS) $(LFLAGS)
main.o:		main.cpp peter.h stewie.h
		$(CC) $(CFLAGS) -c main.cpp
peter.o:	peter.cpp peter.h
		$(CC) $(CFLAGS) -c peter.cpp
stewie.o:	stewie.cpp stewie.h
		$(CC) $(CFLAGS) -c stewie.cpp
clean:
		rm -rf core *.o prog
