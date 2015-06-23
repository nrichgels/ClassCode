EXE = prog13
CC = g++
OBJECTS = functions.o main.o date.o person.o student.o

$(EXE): $(OBJECTS)
	$(CC) -o $(EXE) $(OBJECTS)

main.o: binarySearchTree.h binaryTree.h bst.h student.h prototypes.h main.cpp
	$(CC) -c main.cpp

functions.o: functions.cpp binarySearchTree.h binaryTree.h bst.h student.h
	$(CC) -c functions.cpp

date.o: date.h date.cpp
	$(CC) -c date.cpp

person.o: person.cpp person.h date.h
	$(CC) -c person.cpp

student.o: student.cpp person.h student.h
	$(CC) -c student.cpp

clean:
		rm -rf $(EXE) $(OBJECTS) core.*