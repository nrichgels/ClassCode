CC=g++
OBJECTS=person.o main.o utility.o
EXE=prog
CFLAGS=
LFLAGS=

$(EXE):		$(OBJECTS)
		$(CC) -o $(EXE) $(OBJECTS) $(LFLAGS)

main.o:		main.cpp person.o 
		$(CC) -c $(CFLAGS) main.cpp

person.o:	person.cpp person.h
		$(CC) -c $(CFLAGS) person.cpp
		
utility.o:	utility.cpp
		$(CC) -c $(CFLAGS) utility.cpp

clean:
		rm -rf core.* $(EXE) $(OBJECTS)
