#include <iostream>
using namespace std;

class number
{
   public:
      number(int=0);
      int Value() const;
      const number operator=(int);
      const number operator++();
      const number operator++(int);
   private:
      int value;
};

const number number::operator++()  //pre increment
{
   value++;
   return *this;
}

const number number::operator++(int dummy) //post increment
{
   int whatever;
   cout << "in post increment, dummy = " << dummy << endl;
   cout << "address of dummy " << &dummy << endl;
   cout << "address of whatever " << &whatever << endl;
   number temp=*this;
   value++;
   return temp;
}

number::number(int num) : value(num)
{}

int number::Value() const
{
   return value;
}

const number number::operator=(int num)
{
   value = num;
   return *this;
}

ostream& operator << (ostream& out, const number& n)
{
   out << n.Value();
   return out;
}

int main()
{
   number x(5);
   number y,z;
   cout << x << endl;
   x = 18;
   ++x;
   z = y = ++x;
   cout << x << endl;
   cout << y << endl;
   cout << z << endl;
   x++;
   z = y = x++;
   cout << x << endl;
   cout << y << endl;
   cout << z << endl;
   
   cout << x++ << endl;
   cout << x << endl;
   
   return 0;
}
