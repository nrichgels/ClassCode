#include <iostream>
#include "heap.h"

#define WAIT while(cin.get() != '\n') \
                cin.get()

using namespace std;

int main()
{
    Heap<int> heap;
    try
    {
	heap.heapInsert(30);
	cout << "inserted 30\n";
	heap.dump();  // demonstrate heap contents
        cout << "hit <ENTER> to continue ";
	WAIT;
        cout << endl;
	heap.heapInsert(70);
	cout << "inserted 70\n";
	heap.dump();  // demonstrate heap contents
	WAIT;
	heap.heapInsert(60);
	cout << "inserted 60\n";
	heap.dump();  // demonstrate heap contents
	WAIT;
	heap.heapInsert(10);
	cout << "inserted 10\n";
	heap.dump();  // demonstrate heap contents
	WAIT;
	heap.heapInsert(80);
	cout << "inserted 80\n";
	heap.dump();  // demonstrate heap contents
	WAIT;
	heap.heapInsert(40);
	cout << "inserted 40\n";
	heap.dump();  // demonstrate heap contents
	WAIT;
	heap.heapInsert(90);
	cout << "inserted 90\n";
	heap.dump();  // demonstrate heap contents
	WAIT;
	heap.heapInsert(20);
	cout << "inserted 20\n";
	heap.dump();  // demonstrate heap contents
	WAIT;
	heap.heapInsert(50);
	cout << "inserted 50\n";
	heap.dump();  // demonstrate heap contents
	WAIT;
    }
    catch (HeapException error)
    {
	cout << error.what() << endl;
    }
    int num;
    while (!heap.heapIsEmpty())
    {
	heap.heapDelete(num);
	cout << "deleted " << num << endl;
	heap.dump();  // demonstrate heap contents
	WAIT;
    }
    return 0;
}

