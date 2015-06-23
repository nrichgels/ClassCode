// This program contains an example of using the STL map.
// A map is similar to a vector except that it allows indexing
// by any ordered data type.
#include <iostream>
#include <map>
#include <iterator>
#include <string>
using namespace std;

int main()
{
   map<string,int> m;
   m["hello"]=43;
   m["there"]=92;
   m["how"]=24;
   m["are"]=71;
   m["you"]=59;

   map<string,int>::iterator i;
   i = m.find("how");
   cout << i->second << endl;

   cout << "-------------------\n";
   cout << m["you"] << endl;

   cout << "-------------------\n";
   for (i=m.begin(); i!=m.end(); i++)
      cout << i->first << ' ' << i->second << endl;


   cout << "-------------------\n";

   map<string,string> phonebook;
   phonebook["Jim Nasium"] = "235-9384";
   phonebook["Marty Graw"] = "282-8473";
   phonebook["Justin Case"] = "281-3627";
   phonebook["Quinn Tuplets"] = "235-6452";
   phonebook["Sandy Shore"] = "236-3726";
   phonebook["Phil Harmonic"] = "477-3766";
   
   string s;
   s = "Marty Graw";
   cout << phonebook[s] << endl;
   cout << "-------------------\n";
   return 0;
}
