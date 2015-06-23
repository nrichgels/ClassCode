#include "graph.h"
#include <iostream>
#include <stdexcept>
using namespace GraphNameSpace;
using namespace std;

int main()
{
   Graph<string> Graph1;
   
   cout << "Graph1 is empty: " << Graph1.isEmpty() << endl;
   cout << "Graph1 is full: " << Graph1.isFull() << endl << endl;
   Graph1.insertVertex("Line one.");
   Graph1.insertVertex("Line two.");
   Graph1.insertVertex("Line three.");
   Graph1.insertVertex("Line four.");
   
   Graph1.insertEdge("Line one.", "Line three.");
   Graph1.insertEdge("Line two.", "Line four.");
   Graph1.insertEdge("Line one.", "Line four.");
   
   cout << "Graph1 is empty: " << Graph1.isEmpty() << endl;
   cout << "Graph1 is full: " << Graph1.isFull() << endl;
   cout << "First Dump: " << endl;
   Graph1.dump();
   cout << 'n';
   
   
   cout << "Removing Edge from Line two. to Line four." << endl;
   Graph1.deleteEdge("Line two.", "Line four.");
   
   cout << "Graph1 is empty: " << Graph1.isEmpty() << endl;
   cout << "Graph1 is full: " << Graph1.isFull() << endl;
   cout << "Second Dump: " << endl;
   Graph1.dump();
   cout << '\n';
   
   cout << "Destroying Graph1." << endl;
   Graph1.destroy();
   
   cout << "Graph1 is empty: " << Graph1.isEmpty() << endl;
   cout << "Graph1 is full: " << Graph1.isFull() << endl;
   cout << "Third Dump: " << endl;
   Graph1.dump();
   
   Graph1.insertVertex("One");
   Graph1.insertVertex("Two");
   try
   {
      Graph1.insertVertex("One");
   }
   catch(invalid_argument e)
   {
      cout << e.what() << endl;
   }
   
   Graph1.insertEdge( "One", "Two" );
   try
   {
      Graph1.insertEdge( "Two", "One", 4);
   }
   catch(invalid_argument e)
   {
      cout << e.what() << endl;
   }
   
   Graph1.dump();
   cout << '\n';
   Graph1.deleteEdge("Two", "One");
   
   Graph1.dump();
   cout << '\n';
   
   return 0;
}