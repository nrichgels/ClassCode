Prog4: main.o average.o Read.o arrayPrint.o EvenOddSplit.o sort.o  \
	median.o
	g++ -o prog4 main.o average.o Read.o arrayPrint.o EvenOddSplit.o \
		sort.o median.o

main.o: main.cpp constants.h prototypes.h
	g++ -c main.cpp
average.o: average.cpp
	g++ -c average.cpp
Read.o: Read.cpp 
	g++ -c Read.cpp
arrayPrint.o: arrayPrint.cpp
	g++ -c arrayPrint.cpp
EvenOddSplit.o: EvenOddSplit.cpp
	g++ -c EvenOddSplit.cpp
sort.o: sort.cpp
	g++ -c sort.cpp
median.o: median.cpp
	g++ -c median.cpp
clean:
	rm -rf $(EXE) *.o $(OBJECTS) core.*

