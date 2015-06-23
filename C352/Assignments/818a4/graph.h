//Using kolourpaint
#ifndef __GRAPH_H__
#define __GRAPH_H__
#include <stdexcept>
#include <iostream>
#include <iomanip>
#include <sstream>
using namespace std;

namespace GraphNameSpace
{
/************************ENUM TYPES***********************************
 *********************************************************************/
enum directedType {DIRECTED, UNDIRECTED}; //End enum directedType
enum weightedType {WEIGHTED, UNWEIGHTED}; //End enum weightType

/************************STRUCT DECLERATION***************************
 *********************************************************************/
template <class Type>
struct nodeType1
{
   Type value;
   nodeType1<Type> *link;
   int vertexID;
};//End nodeType1

template <class Type>
struct nodeType2
{
   nodeType1<Type> *fromAddress;
   nodeType1<Type> *toAddress;
   nodeType2<Type> *link;
   int weight;
};//End nodeType2

/************************CLASS DECLERATION****************************
 *********************************************************************/
template <class T>
class Graph
{
   public:
      // Constructor
      // Creates a Graph object with UNDIRECTED and UNWEIGHTED as default.
      // Paramaters: none
      explicit Graph();
      
      // Constructor
      // Creates a Graph object with choice of DIRECTED or UNDIRECTED and
      // UNWEIGHTED as default.
      // Paramaters: directedType{DIRECTED, UNDIRECTED}
      explicit Graph(directedType);
      
      // Constructor
      // Creates a Graph object with choice of WEIGHTED or UNWEIGHTED and
      // UNDIRECTED as default.
      // Paramaters: weightedType{WEIGHTED, UNWEIGHTED}
      explicit Graph(weightedType);
      
      // Constructor
      // Creates a Graph object with choice of WEIGHTED or UNWEIGHTED and
      // choice of DIRECTED or UNDIRECTED.
      // Paramaters: directedType{DIRECTED, UNDIRECTED}, 
      //             weightedType{WEIGHTED, UNWEIGHTED}
      explicit Graph(directedType, weightedType);
      
      // Constructor
      // Creates a Graph object with choice of WEIGHTED or UNWEIGHTED and
      // choice of DIRECTED or UNDIRECTED.
      // Paramaters: weightedType{WEIGHTED, UNWEIGHTED}
      //             directedType{DIRECTED, UNDIRECTED}, 
      explicit Graph(weightedType, directedType);
      
      // Destructor
      // Recycles dynamic memory once hte program using htis class is finished.
      // Paramaters: none
      ~Graph();
      
      // Copy Constructor
      // Copies dynamic memory when a Graph object is passed to a function.
      // Paramaters: Graph: What the new Graph is copying from
      Graph(const Graph&);
      
      // Operator=
      // Copies dynamic memory when a Graph object is set equal to another 
      // Graph object.
      // Paramaters: Graph: What the new Graph is copying from.
      const Graph& operator=(const Graph&);
      
      // Method resets the Graph as though it were new.
      // Preconditions: Graph is initialized
      // Postconditions: No vertices of edges are contained within
      void destroy();
      
      // Method returns whether or not there are any vertices within the Graph.
      // Preconditions: Graph is initialized.
      // Postconditions: Returns 0 if no vertices, 1 there are vertices
      bool isEmpty() const;
      
      // Method returns whether or not the graph is full.
      // Preconditions: Graph is initialized.
      // Postconditions: 0 is returned, Graph is never full.
      bool isFull() const;
      
      // Method returns how many edges are within the Graph.
      // Preconditions: Graph is initialized.
      // Postconditions: An integer representing how many edges in the graph
      //                 is returned.
      int edgeCount() const;
      
      // Method returns how many vertices are within the graph.
      // Preconditions: Graph is initialized.
      // Postconditions: An integer representing how many vertices in the graph
      //                 is returned.
      int vertexCount() const;
      
      // Method inserts a vertex into the Graph.
      // Preconditions: A paramater matching the template type is given.
      // Postcondition: Graph stores the value.
      void insertVertex(const T);
      
      // Method inserts an edge into the Graph.
      // Paramaters: Template fromValue, Template toValue, int weight
      // Preconditions: Two paramaters that are the template type, and are
      //                currently vertices are given.  Weight is optional if
      //                the graph is WEIGHTED.
      // Postconditions: Link between two vertices is established, with a
      //                possible given weight.
      void insertEdge(const T, const T, const int paramWeight=1);
      
      // Method removes an edge from the Graph.
      // Paramaters: Template fromValue, Template toValue
      // Preconditions: Two paramaters that are the template type, and are
      //                currently vertices are given.
      // Postconditions: The edge is removed from the Graph.
      void deleteEdge(const T, const T);
      
      // Method that removes a vertex from the graph.
      // Preconditions: Vertex is is a template type and is currently within
      //                the graph.
      // Postconditions: The vertex and any edges associated with it are
      //                 removed.
      void deleteVertex(const T);
      
      // Method that reports all vertices and their connections.
      // Preconditions: Graph is initialized
      // Postconditions: Every piece of information regarding the Graph is
      //                 printed.
      void dump();
   private:
      bool isDirectedType;
      bool isWeightedType;
      int edges;
      int vertices;
      int nextVertexID;
      
      nodeType1<T> *first1;
      nodeType1<T> *last1;
      nodeType2<T> *first2;
      nodeType2<T> *last2;
      
      void copyGraph(const Graph& someGraph);
   
};//End class Graph

/************************CLASS IMPLEMENTATION*************************
 ***************************CONSTRUCTORS******************************/
template <class T>
Graph<T>::Graph()
{
   isDirectedType = false;
   isWeightedType = false;
   first1 = NULL;
   last1 = NULL;
   first2 = NULL;
   last2 = NULL;
   edges = 0;
   vertices = 0;
   nextVertexID = 0;
}//End Constructor

template <class T>
Graph<T>::Graph(directedType directedOption)
{
   isDirectedType = (directedOption == DIRECTED);
   isWeightedType = false;
   first1 = NULL;
   last1 = NULL;
   first2 = NULL;
   last2 = NULL;
   edges = 0;
   vertices = 0;
   nextVertexID = 0;
}//End Constructor

template <class T>
Graph<T>::Graph(weightedType weightedOption)
{
   isWeightedType = (weightedOption == WEIGHTED);
   isDirectedType = false;
   first1 = NULL;
   last1 = NULL;
   first2 = NULL;
   last2 = NULL;
   edges = 0;
   vertices = 0;
   nextVertexID = 0;
}//End constructor

template <class T>
Graph<T>::Graph(weightedType weightedOption, directedType directedOption)
{
   isWeightedType = (weightedOption == WEIGHTED);
   isDirectedType = (directedOption == DIRECTED);
   first1 = NULL;
   last1 = NULL;
   first2 = NULL;
   last2 = NULL;
   edges = 0;
   vertices = 0;
   nextVertexID = 0;
}//End constructor

template <class T>
Graph<T>::Graph(directedType directedOption, weightedType weightedOption)
{
   isWeightedType = (weightedOption == WEIGHTED);
   isDirectedType = (directedOption == DIRECTED);
   first1 = NULL;
   last1 = NULL;
   first2 = NULL;
   last2 = NULL;
   edges = 0;
   vertices = 0;
   nextVertexID = 0;
}//End constructor

/************************CLASS IMPLEMENTATION*************************
 ****************************DESTRUCTORS******************************/
template <class T>
Graph<T>::~Graph()
{
   destroy();
}//End Destructor

/************************CLASS IMPLEMENTATION*************************
 *************************COPY CONSTRUCTORS***************************/
template <class T>
Graph<T>::Graph( const Graph<T>& other)
{
   copyGraph( other );
}//End copy contructor
/************************CLASS IMPLEMENTATION*************************
 *************************OPERATOR OVERLOADS**************************/
template <class T>
const Graph<T>& Graph<T>::operator=(const Graph<T>& other )
{
   if( this != &other )
      copyGraph( other );
   
   return *this;
}//end overload =
/************************CLASS IMPLEMENTATION*************************
 **************************PUBLIC METHODS*****************************/
template <class T>
bool Graph<T>::isEmpty() const
{
   return (first1 == NULL);
}//End isEmpty

template <class T>
bool Graph<T>::isFull() const
{
   return false;
}//End isFull

template <class T>
int Graph<T>::edgeCount() const
{
   return edges;
}//End edgeCount

template <class T>
int Graph<T>::vertexCount() const
{
   return vertices;
}//End vertexCount

template <class T>
void Graph<T>::insertVertex(const T givenVertex)
{
   //Before doing anything, make sure teh vertext doesn't already exist
   nodeType1<T> *exploringNode;
   exploringNode = first1;
   while( exploringNode != NULL )
   {
      if( (*exploringNode).value == givenVertex)
         throw invalid_argument( "The given vertex already exists." );
      exploringNode = (*exploringNode).link;
   }//End while loop
   
   nodeType1<T> *newNode;
   newNode = new nodeType1<T>;
   (*newNode).link = NULL;
   (*newNode).vertexID = nextVertexID;
   (*newNode).value = givenVertex;
   
   if(first1 == NULL)
   {
      first1 = newNode;
      last1 = newNode;
   }//End if statement
   else
   {
      (*last1).link = newNode;
      last1 = newNode;
   }//End else statement
   vertices++;
   nextVertexID++;
}//End insertVertex

template <class T>
void Graph<T>::insertEdge(const T fromVertex, const T toVertex, const int paramWeight)
{
   //Before doing anything, test to make sure that the edge doesn't already exist.
   nodeType2<T> *exploringNode;
   exploringNode = first2;
   while( exploringNode != NULL )
   {
      if( ( (*(*exploringNode).fromAddress).value == fromVertex ) && ( (*(*exploringNode).toAddress).value == toVertex ) )
         throw invalid_argument( "Edge already exists within the graph." );
      if( !isDirectedType )
         if( ( (*(*exploringNode).toAddress).value == fromVertex ) && ( (*(*exploringNode).fromAddress).value == toVertex ) )
            throw invalid_argument( "Edge already exists within the graph." );
         
      exploringNode = (*exploringNode).link;
   }//End while loop
   
   
   nodeType2<T> *newNode;
   newNode = new nodeType2<T>;
   
   nodeType1<T> *currentNodeType1;
   nodeType1<T> *currentNodeType2;
   currentNodeType1 = first1;
   currentNodeType2 = first1;
   

   
   while( (currentNodeType1 != NULL) && ((*currentNodeType1).value != fromVertex) )
   {
      currentNodeType1 = (*currentNodeType1).link;
   }//End while loop
   
   while( (currentNodeType2 != NULL) && ((*currentNodeType2).value != toVertex) )
   {
      currentNodeType2 = (*currentNodeType2).link;
   }//End while loop
   
   //Check to make sure that both given vertices exist
   if( currentNodeType1 == NULL || currentNodeType2 == NULL )
      throw invalid_argument( "One or more given vertices do not exist." );
   
   (*newNode).fromAddress = currentNodeType1;
   (*newNode).toAddress = currentNodeType2;
   (*newNode).weight = paramWeight;
   (*newNode).link = NULL;
   
   if( first2 == NULL )
   {
      first2 = newNode;
      last2 = newNode;
   }//End if statement
   else
   {
      (*last2).link = newNode;
      last2 = newNode;
   }//End else statement
    
    edges++;
}//End insertEdge

template <class T>
void Graph<T>::deleteEdge(const T fromVertex, const T toVertex)
{
   nodeType2<T> *currentNodeType;
   nodeType2<T> *previousNodeType;
   
   currentNodeType = first2;
   while( (currentNodeType != NULL) && ( (*(*currentNodeType).fromAddress).value != fromVertex || ((*(*currentNodeType).toAddress).value != toVertex) ) )
   {
      previousNodeType = currentNodeType;
      currentNodeType = (*currentNodeType).link;
   }//End while loop
   
   if (currentNodeType == NULL && !isDirectedType)
   {
      currentNodeType = first2;
      while( (currentNodeType != NULL) && ( (*(*currentNodeType).toAddress).value != fromVertex || ((*(*currentNodeType).fromAddress).value != toVertex) ) )
      {
         previousNodeType = currentNodeType;
         currentNodeType = (*currentNodeType).link;
      }//End while loop
   }//End if statement
   
   if(currentNodeType == NULL)
      throw invalid_argument( "Edge doesn't exist, and therefore was not be deleted." );
   
   if(first2 == last2)
   {
      delete first2;
      first2 = NULL;
      last2 = NULL;
   }//End if statement
   
   else if(first2 == currentNodeType)
   {
      first2 = (*first2).link;
      delete currentNodeType;
      currentNodeType = NULL;
   }//End else if
   
   else if(last2 == currentNodeType)
   {
      last2 = previousNodeType;
      delete currentNodeType;
      currentNodeType = NULL;
   }//end else if
   
   else
   {
      (*previousNodeType).link = (*currentNodeType).link;
      delete currentNodeType;
      currentNodeType = NULL;
   }//End else statement
   edges--;
}//End deleteEdge

template <class T>
void Graph<T>::deleteVertex( const T givenVertex )
{
   nodeType1<T> *current;
   nodeType1<T> *previous;
   nodeType2<T> *forwardExploringNode;
   nodeType2<T> *exploringNode;
   
   //Find the Vertex to be deleted
   current = first1;
   while( current!= NULL && ((*current).value != givenVertex ) )
   {
      previous = current;
      current = (*current).link;
   }//End while loop
   
   if( current ==NULL )
      throw invalid_argument( "Given vertex does not exist, and therefore was not deleted." );
   
   exploringNode = first2;
   
   //Delete and delete all edges related to the vertex
   //Shouldn't matter whether or not the edges are directed.
   while(exploringNode != NULL)
   {
      forwardExploringNode = (*exploringNode).link;
         
      if( (*exploringNode).fromAddress == current)
         deleteEdge( (*current).value, (*(*exploringNode).toAddress).value);
      else if( (*exploringNode).toAddress == current)
         deleteEdge( (*(*exploringNode).fromAddress).value, (*current).value );
      
      exploringNode = forwardExploringNode;
         
   }//End while loop
   
   if( first1 == last1 )
   {
      delete first1;
      first1 = NULL;
      last1 = NULL;
   }//End if
   
   else if( current == first1 )
   {
      first1 = (*first1).link;
      delete current;
   }//End elif statement
   
   else if( current == last1 )
   {
      (*previous).link = NULL;
      last1 = previous;
      delete current;
   }//End elif statement
   
   else
   {
      (*previous).link = (*current).link;
      delete current;
   }//End else statement
   
   vertices--;
}//end deleteVertex

template<class T>
void Graph<T>::destroy()
{
   nodeType1<T> *destroyer;
   nodeType1<T> *scout;
   
   destroyer = first1;
   while(destroyer!=NULL)
   {
      scout = (*destroyer).link;
      deleteVertex( (*destroyer).value );
      destroyer = scout;
   }//End while loop
   
   vertices = 0;
   nextVertexID = 0;
   edges = 0;
   first1 = NULL;
   last1 = NULL;
   first2 = NULL;
   last2 = NULL;
}//End destroy

template <class T>
void Graph<T>::dump()
{
   nodeType1<T> *exploringNode1;
   nodeType2<T> *exploringNode2;
   exploringNode1 = first1;
   
   cout << "dumping graph:   ";
   if( isDirectedType )
      cout << "DIRECTED   ";
   else
      cout << "UNDIRECTED   ";
   if( isWeightedType )
      cout << "WEIGHTED   ";
   else
      cout << "UNWEIGHTED   ";
   cout << "vertices:" << vertices << "   " << "edges:" << edges << "   " << endl;
   cout << "VERTEX              " << "ADJACENT VERTICES" << endl;
   cout << "-----------------   --------------------------------------------" << endl;
   
   while(exploringNode1 != NULL)
   {
      stringstream lineUp;
      exploringNode2 = first2;
      
      lineUp << "[" << (*exploringNode1).vertexID << "]  " << (*exploringNode1).value ;
      cout << left << setw(20) << lineUp.str();
      
      int i = 0;
      while(exploringNode2 != NULL)
      {
         if(exploringNode1 == (*exploringNode2).fromAddress)
         {
            if( i != 0 )
               cout << ", ";
            cout << "[" << (*(*exploringNode2).toAddress).vertexID << "]" << (*(*exploringNode2).toAddress).value;
            if(isWeightedType)
            {
               cout << "(" << (*exploringNode2).weight << ")";
            }//End if statement
            i++;
         }//End if statement
         
         if(!isDirectedType)
         {
            if(exploringNode1 == (*exploringNode2).toAddress)
            {
               if( i != 0 )
                 cout << ", ";
               cout << "[" << (*(*exploringNode2).fromAddress).vertexID << "]" << (*(*exploringNode2).fromAddress).value;
               if(isWeightedType)
               {
                 cout << "(" << (*exploringNode2).weight << ")";
               }//End if statement
               i++;
            }//End if statement
         }//End if statement
         exploringNode2 = (*exploringNode2).link;
      }//End while loop
     
     cout << endl;
     exploringNode1 = (*exploringNode1).link;
   }//End while loop
}//End dump

/************************CLASS IMPLEMENTATION*************************
 *************************PRIVATE METHODS*****************************/
template <class T>
void Graph<T>::copyGraph(const Graph<T>& someGraph)
{
   if(first1 != NULL)
      destroy();
   
   if( someGraph.first1 != NULL )
   {
      nodeType1<T> freshNode1;
      nodeType1<T> current1;
      
      
      nodeType2<T> freshNode2;
      nodeType2<T> current2;
      
      current1 = someGraph.first1;
      current2 = someGraph.first2;
      
      insertVertex( (*current1).value );
      freshNode1 = first1;
      (*freshNode1).vertexID = (*current1).vertexID;
      current1 = (*current1).link;
      
      while( current1 != NULL)
      {
         insertVertex( (*current1).value );
         freshNode1=(*freshNode1).link;
         (*freshNode1).vertexID = (*current1).vertexID;
         current1 = (*current1).link;
      }//End while loop
      
      if(someGraph.first2 != NULL)
      {
         insertEdge( *((*current2).fromAddress).value, *((*current2).toAddress).value );
         freshNode2 = first2;
         (*freshNode2).weight = (*current2).weight;
         current2 = (*current2).link;
         while( current2 != NULL)
         {
            insertEdge( *((*current2).fromAddress).value, *((*current2).toAddress).value );
            freshNode2 = (*freshNode2).link;
            (*freshNode2).weight = (*current2).weight;
            current2 = (*current2).link;
         }//End while loop
      }//End if statement
   }//End if statement
   
}//End copyGraph

}//End namespaceGraph

#endif