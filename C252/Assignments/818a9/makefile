EXE = prog9
CC = g++
OBJECTS = arrayListTypeImp.o date.o main.o person.o

$(EXE): $(OBJECTS)
	$(CC) -o $(EXE) $(OBJECTS)

arrayListTypeImp.o: arrayListTypeImp.cpp  itemtype.h date.h arrayListType.h 
	$(CC) -c arrayListTypeImp.cpp

date.o: date.h date.cpp
	$(CC) -c date.cpp

person.o: person.cpp date.cpp date.h itemtype.h
	$(CC) -c person.cpp

main.o: main.cpp date.h itemtype.h arrayListType.h
	$(CC) -c main.cpp

clean:
		rm -rf $(EXE) $(OBJECTS) core.*
