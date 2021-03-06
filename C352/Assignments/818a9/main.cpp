#include "shortestPath.h"
#include <iostream>
#include <iomanip>
using namespace std;

int main()
{
   string journeyBegin;
   string journeyEnd;
   ShortestPath<string> UScities(DIRECTED, WEIGHTED);
   
   UScities.insertVertex("Seattle");
   UScities.insertVertex("Los Angeles");
   UScities.insertVertex("Phoenix");
   UScities.insertVertex("Denver");
   UScities.insertVertex("Fargo");
   UScities.insertVertex("Minneapolis");
   UScities.insertVertex("Houston");
   UScities.insertVertex("St. Louis");
   UScities.insertVertex("Chicago");
   UScities.insertVertex("Detroit");
   UScities.insertVertex("Miami");
   UScities.insertVertex("New York");
   
   UScities.insertEdge("Seattle","Chicago", 2072);
   UScities.insertEdge("Seattle","Denver", 1332);
   UScities.insertEdge("Los Angeles", "Seattle", 1151);
   UScities.insertEdge("Los Angeles", "Denver", 1023);
   UScities.insertEdge("Los Angeles", "Phoenix", 381);
   UScities.insertEdge("Los Angeles", "New York", 2824);
   UScities.insertEdge("Phoenix", "Los Angeles", 381);
   UScities.insertEdge("Phoenix", "Houston", 1186);
   UScities.insertEdge("Denver", "Los Angeles", 1023);
   UScities.insertEdge("Denver", "Minneapolis", 920);
   
   UScities.insertEdge("Fargo", "Minneapolis", 240);
   UScities.insertEdge("Fargo", "Denver", 909);
   UScities.insertEdge("Minneapolis", "Fargo", 240);
   UScities.insertEdge("Minneapolis", "Chicago", 409);
   UScities.insertEdge("Minneapolis", "Denver", 920);
   UScities.insertEdge("Houston", "Phoenix", 1186);
   UScities.insertEdge("Houston", "St. Louis", 780);
   UScities.insertEdge("Houston", "Miami", 1190);
   UScities.insertEdge("St. Louis", "Denver", 861);
   UScities.insertEdge("St. Louis", "Detroit", 547);
   UScities.insertEdge("Chicago", "Minneapolis", 409);
   UScities.insertEdge("Chicago", "Detroit", 286);
   UScities.insertEdge("Chicago", "New York", 821);
   UScities.insertEdge("Detroit", "Chicago", 286);
   UScities.insertEdge("Detroit", "St. Louis", 547);
   UScities.insertEdge("Detroit", "New York", 640);
   UScities.insertEdge("Miami", "Houston", 1190);
   UScities.insertEdge("Miami", "New York", 1281);
   UScities.insertEdge("New York", "Chicago", 821);
   UScities.insertEdge("New York", "Los Angeles", 2824);
   UScities.insertEdge("New York", "Miami", 1281);
   
   cout << "Please type in where the journey begins: ";
   getline(cin, journeyBegin);
   cout << "Please type in where your journey will end: ";
   getline(cin, journeyEnd);
   
   UScities.outputShortestPath(journeyBegin, journeyEnd);
   //UScities.dump();
   return 0;
}//End main

/*
dumping graph:  DIRECTED   WEIGHTED   vertices:12   edges:31
VERTEX              ADJACENT VERTICES
-----------------   --------------------------------------------
[0]  Seattle        [8]Chicago(2072), [3]Denver(1332)
[1]  Los Angeles    [0]Seattle(1151), [3]Denver(1023), [2]Phoenix(381), [11]New York(2824)
[2]  Phoenix        [1]Los Angeles(381), [6]Houston(1186)
[3]  Denver         [1]Los Angeles(1023), [5]Minneapolis(920)
[4]  Fargo          [5]Minneapolis(240), [3]Denver(909)
[5]  Minneapolis    [4]Fargo(240), [8]Chicago(409), [3]Denver(920)
[6]  Houston        [2]Phoenix(1186), [7]St. Louis(780), [10]Miami(1190)
[7]  St. Louis      [3]Denver(861), [9]Detroit(547)
[8]  Chicago        [5]Minneapolis(409), [9]Detroit(286), [11]New York(821)
[9]  Detroit        [8]Chicago(286), [7]St. Louis(547), [11]New York(640)
[10] Miami          [6]Houston(1190), [11]New York(1281)
[11] New York       [8]Chicago(821), [1]Los Angeles(2824), [10]Miami(1281)
*/