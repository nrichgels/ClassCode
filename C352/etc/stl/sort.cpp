#include <iostream>
#include <vector>
#include <algorithm>
#include <iterator>
using namespace std;

int main()
{
   vector<int> numbers(10);
   numbers[0] = 32;
   numbers[1] = 83;
   numbers[2] = 19;
   numbers[3] = 48;
   numbers[4] = 79;
   numbers[5] = 37;
   numbers[6] = 25;
   numbers[7] = 57;
   numbers[8] = 88;
   numbers[9] = 45;
   sort(numbers.begin(),numbers.end());
   copy(numbers.begin(),numbers.end(),ostream_iterator<int>(cout,"\n"));

   cout << "--------\n";
   int num;
   num = 63;
   if (binary_search(numbers.begin(),numbers.end(),num))
      cout << num << " is in the vector\n";
   else
      cout << num << " is not in the vector\n";
   num = 48;
   if (binary_search(numbers.begin(),numbers.end(),num))
      cout << num << " is in the vector\n";
   else
      cout << num << " is not in the vector\n";

   return 0;
}
