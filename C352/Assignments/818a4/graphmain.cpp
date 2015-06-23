#include <iostream>
#include "graph.h"
using namespace GraphNameSpace;
using namespace std;

class V
{
   public:
      V() {}  // constructor with no arguments
      V(const string& s) : value(s) {}  // constructor with argument
      string getValue() const {return value;}
      bool operator==(const V& v) const {return getValue()==v.getValue();}
      bool operator!=(const V& v) const {return getValue()!=v.getValue();}
      bool operator<(const V& v) const {return getValue()<v.getValue();}
      bool operator<=(const V& v) const {return getValue()<=v.getValue();}
      bool operator>(const V& v) const {return getValue()>v.getValue();}
      bool operator>=(const V& v) const {return getValue()>=v.getValue();}
   private:
      string value;
};

ostream& operator<<(ostream&out, const V& v)
{
   out << v.getValue();
   return out;
}


int main()
{
   Graph<int> Graph1;  // UNDIRECTED and UNWEIGHTED
   Graph<int> Graph2(WEIGHTED,DIRECTED);
   Graph<char> Graph3(DIRECTED,WEIGHTED);
   Graph<int> Graph4(DIRECTED);  // DIRECTED and UNWEIGHTED)
   Graph<int> Graph5(WEIGHTED);  // WEIGHTED and UNDIRECTED
   char A = 'A';
   char B = 'B'; 
   char C = 'C';
   Graph3.insertVertex(A);
   Graph3.insertVertex(B);
   Graph3.insertVertex(C);
   Graph3.insertEdge(A,B,5);
   Graph3.insertEdge(A,C,3);
   Graph3.insertEdge(B,C,4);
   if (Graph3.isEmpty())
      cout << "empty\n";
   else
      cout << "not empty\n";
   if (Graph3.isFull())
      cout << "full\n";
   else
      cout << "not full\n";
   cout << "Vertices: " << Graph3.vertexCount() << endl;
   cout << "Edges: " << Graph3.edgeCount() << endl;
   Graph3.dump();
   Graph3.deleteEdge(A,C);
   Graph3.dump();
   Graph3.deleteVertex(B);
   Graph3.dump();

   Graph<V>  g;
   V V1("Vertex1");
   V V2("Vertex2");
   V V3("Vertex3");
   g.insertVertex(V1);
   g.insertVertex(V2);
   g.insertVertex(V3);
   g.insertEdge(V1,V2);
   g.insertEdge(V3,V1);
   g.insertEdge(V3,V2);
   g.dump();   


   return 0;
}

