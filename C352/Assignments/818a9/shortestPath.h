#ifndef __SHORTEST_PATH_H__
#define __SHORTEST_PATH_H__

#include "graph.h"
#include <stack>
#include <stdexcept>
#include <iostream>
#include <iomanip>
#include <sstream>
using namespace std;

const int MAX=2147483647;

//Found struct holds the location to a node and keeps track whether or not that
// node has been found, it's smallestLocalWeight (meaning the smallest weight
// that has been found for it to hold), and the previous node that gurantees
// it's currrent weight.
template <class T>
struct Found
{
   nodeType1<T> *foundation;
   nodeType1<T> *through;
   Found *connection;
   bool found;
   int smallestLocalWeight;
   
};//End struct Found

template <class T>
class ShortestPath : public Graph<T>
{
public:
   // Constructor
   // Creates a ShortestPath object with UNDIRECTED and UNWEIGHTED as default.
   // Paramaters: none
   explicit ShortestPath();
   
   // Constructor
   // Creates a ShortestPath object with choice of DIRECTED or UNDIRECTED and
   // UNWEIGHTED as default.
   // Paramaters: directedType{DIRECTED, UNDIRECTED}
   explicit ShortestPath(directedType);
   
   // Constructor
   // Creates a ShortestPath object with choice of WEIGHTED or UNWEIGHTED and
   // UNDIRECTED as default.
   // Paramaters: weightedType{WEIGHTED, UNWEIGHTED}
   explicit ShortestPath(weightedType);
   
   // Constructor
   // Creates a ShortestPath object with choice of WEIGHTED or UNWEIGHTED and
   // choice of DIRECTED or UNDIRECTED.
   // Paramaters: directedType{DIRECTED, UNDIRECTED}, 
   //             weightedType{WEIGHTED, UNWEIGHTED}
   explicit ShortestPath(directedType, weightedType);
   
   // Constructor
   // Creates a ShortestPath object with choice of WEIGHTED or UNWEIGHTED and
   // choice of DIRECTED or UNDIRECTED.
   // Paramaters: weightedType{WEIGHTED, UNWEIGHTED}
   //             directedType{DIRECTED, UNDIRECTED}, 
   explicit ShortestPath(weightedType, directedType);
   
   // method outputs to the screen the shortest path (weight wise) within the
   //                                                                   graph.
   // Paramaters: object of Type T, The start of the graph
   //             object of Type T, the end location of the graph
   // Preconditions: Objects are within the initiated graph
   // Postconditions: A path to the location is found and output to the screen.
   void outputShortestPath( const T& obj1, const T& obj2);
};

/************************CLASS IMPLEMENTATION*************************
 ***************************CONSTRUCTORS******************************/
template <class T>
ShortestPath<T>::ShortestPath() : Graph<T>()
{
}//End Constructor

template <class T>
ShortestPath<T>::ShortestPath(directedType directedOption) : Graph<T>(directedOption)
{
}//End Constructor

template <class T>
ShortestPath<T>::ShortestPath(weightedType weightedOption) : Graph<T>(weightedOption)
{
}//End Constructor

template <class T>
ShortestPath<T>::ShortestPath(weightedType weightedOption, directedType directedOption)
                              : Graph<T>(weightedOption, directedOption)
{
}//End Constructor

template <class T>
ShortestPath<T>::ShortestPath(directedType directedOption, weightedType weightedOption)
                              : Graph<T>(directedOption, weightedOption)
{
}//End Constructor

/************************CLASS IMPLEMENTATION*************************
 **************************PUBLIC METHODS*****************************/
template <class T>
void ShortestPath<T>::outputShortestPath( const T& obj1, const T& obj2)
{

   nodeType1<T> *current;
   nodeType2<T> *edgeSeeker;
   int edges = Graph<T>::edgeCount();
   int vertices = Graph<T>::vertexCount();
   int beginIndex = -1;
   int endIndex = -1;
   int foundCount = 0;
   int currentMinWeight;
   int z;
   int currentInt;
   
   Found<T> found[vertices];
   Found<T> dummyFound;
   Found<T> *currentFound;
   
   stack<Found<T> > correctOrdering;
   current = Graph<T>::first1;
//The found struct will hold a node's status relative to the algorithm.
//So, we create an array to hold each node's algorithm status.
   
   //This assigns every index within the found struct array a node
   //relative to the graph.
   while( current != NULL )
   {
      found[foundCount].foundation = current;
      found[foundCount].found = false;
      found[foundCount].smallestLocalWeight = MAX;
      current = (*current).link;
      foundCount++;
   }//End while loop
   
   //This for loop checks whether the objects to find a shortest path between
   //actually exists in the graph.  If they do, it hold their integer index.
   for( int i = 0; i<foundCount; i++)
   {
      if( found[i].foundation->value == obj1 )
         beginIndex = i;
      if( found[i].foundation->value == obj2 )
         endIndex = i;
   }//End for loop
   
   //otherwise we throw an exception
   if( beginIndex == -1 || endIndex == -1 )
      throw invalid_argument( "One or more of the provided arguments does not exist." );
   
   found[beginIndex].found = true;
   found[beginIndex].smallestLocalWeight = 0;
   found[beginIndex].connection = NULL;
   currentInt = beginIndex;
   
   //While the end path is not found.
   while( !found[endIndex].found )
   {
      currentMinWeight = MAX;
      //Assign edgeSeeker the first edge in the linked structure.
      edgeSeeker = Graph<T>::first2;
      
      //While edgeSeeker hasn't hit the end...
      while( edgeSeeker != NULL )
      {  
         //If the address from the sending vertex of the edge is equal to the
         //address of the current vertex...
         if( (*edgeSeeker).fromAddress == found[currentInt].foundation )
         {
            int key = 0;
            int newLocalWeight = found[currentInt].smallestLocalWeight + (*edgeSeeker).weight;
            
            //Find the int value of the corresponding receiving end.
            while( (*edgeSeeker).toAddress != found[key].foundation )
            {
               key++;
            }
            
            //If the toAddress's smallestLocalWeight is greater than the edge's
            //weight + the current node's smallestLocalWeight, replace it, and
            //make the current node node the through node for the vertex
            if( found[key].smallestLocalWeight > newLocalWeight )
            {
               found[key].smallestLocalWeight = newLocalWeight;
               found[key].connection = &found[currentInt];
            }//End if statement (nest 3)
         }//End if statement (nest 2)
         
         edgeSeeker = (*edgeSeeker).link;
      }//End while loop (nest 1)
      
      //This for loop essentially finds the smallest local weight of any 
      //node not currently found.
      for(int i = 0; i<foundCount; i++)
      {
         if( !found[i].found && found[i].smallestLocalWeight < currentMinWeight )
            currentInt = i;
      }//End for loop (nest 1)
      found[currentInt].found = true;
   }//End while loop

   
   
   //Once the end of the path is found, we have to permanently link the products of our algorithm together.
   currentFound = &found[endIndex];
   
   while( currentFound != NULL)
   {
      correctOrdering.push( (*currentFound) );
      currentFound = (*currentFound).connection;
   }//End while loop
   
   dummyFound = correctOrdering.top();
   cout << dummyFound.foundation->value;
   correctOrdering.pop();
   while( !correctOrdering.empty() )
   {
      dummyFound = correctOrdering.top();
      cout << "->" <<  dummyFound.foundation->value << "(" << dummyFound.smallestLocalWeight << ")";
      correctOrdering.pop();
   }//End while loop
   
   cout << endl;
   
}//End outputShortestPath

#endif