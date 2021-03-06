// Author: Nathan Richgels
// File: money.cpp
// Date: 1/31/2012
// Class: CSIS352
// Assignment 1
#include <iomanip>
#include <iostream>
#include <sstream>
#include "money.h"
using namespace std;

int Money::fieldSize = 10;
bool Money::blCommas = false;
bool Money::blTruncate = false;
bool Money::blRound = false;
bool Money::blGeneral = true;
bool Money::blCurrency = false;
bool Money::blAccounting = false;
bool Money::blDollarSign = false;

/*string intToString(int n, Money obj)
{
   //ss is for converting an integer into a string.
   stringstream ss;
   //length is the amount of space that the number will take up
   int length;
   //needed commas is how many commas are needed for the integer.
   int neededCommas = 0;
   //count is the amount of space that both the commas and the number will take up.
   int count;
   //tracker tracks at what place in the unfinished string that the
   // array is being copied is at.
   int tracker = 0;

   //If the given integer is negative, subtract it from 0.
   //This gurantees an absolute value of the integer.
   if(n<0)
   {
     n = 0 - n;
   }//End if statement
   
   
   //cout << "n: " << n << endl; //Debugging
   
   //load the integer into the string stream
   ss << n;
   //take the resulting string back out and assign it to unfinishedNumber.
   string unfinishedNumber = ss.str();
   length = unfinishedNumber.length();
   //cout << "unfinishedNumber: " << unfinishedNumber << endl;
   
   //If there are more than 4 digits in the unfinishedNumber, calculate how
   // many commas are needed to insert into the Number.
   if(length >= 4)
   {
      neededCommas = 1 + ((length - 4)/3);
   }
   else
      neededCommas = 0;

   //The total amount of character space needed for our final number is
   // the number of digits of the original number added with the number
   // of commas that are needed.
   count = length + neededCommas;
   char finishedString[count];
   //cout << count << endl;  //debugging
   
   //This for loop assembles the number.
   for(int i = 0; i<count; i++)
   {
    //If the remainder of dividing the i repetition by 4 is 0,
    // and i is not equal to 0, then a comma will be placed in
    // that place.
    if((i)%4 == 0 && i!= 0)
    {
     finishedString[i] = ',';
    }
    //otherwise, the place at the i position is a copy of an actual digit from the
    //number we are trying to produce.
    else
    {
     //cout << "finishedString[i] (before): " << finishedString[i] << "unfinishedNumber[tracker] (before): " 
     //<< unfinishedNumber[tracker] << endl; //Debugging
     finishedString[i] = unfinishedNumber[tracker];
     //cout << "finishedString[i] (after): " << finishedString[i] << " unfinishedNumber[tracker] (after): " 
     //<< unfinishedNumber[tracker] << endl;  //Debugging
     tracker++;
    }//End else
    
   }//End for loop

  //cout << "finishedString: " << finishedString << endl; //Debugging
  return finishedString;
}//End intToString*/

Money::Money(double amt)
{
   setValues(amt);
}//End Constructor for Money

void Money::setFieldSize(const int& size)
{
   fieldSize = size;
}

void Money::setFormat(const formatType& type)
{
   switch(type)
   {case General :
                  blGeneral = true;
		  blAccounting = false;
		  blCurrency = false;
		  blCommas = false;
		  blDollarSign = false;
		  blRound = false;
                  blTruncate = false;
		  break;

    case Currency :
		  blGeneral = false;
		  blAccounting = false;
		  blCurrency = true;
		  blCommas = true;
		  blDollarSign = true;
		  blRound = false;
		  blTruncate = true;
		  break;

    case Accounting :
		    blGeneral = false;
		    blAccounting = true;
		    blCurrency = false;
		    blCommas = true;
		    blDollarSign = true;
		    blRound = false;
		    blTruncate = false;
		    break;

   /* case Cents :
	       blRound = false;
	       blTruncate = false;
	       break;

    case Round :
	       blRound = true;
	       blTruncate = false;
	       break;

    case Truncate :
		  blRound = false;
		  blTruncate = true;
		  break;

    case DollarSign :
		    blDollarSign = true;
		    break;

    case NoDollarSign :
		      blDollarSign = false;
		      break;
    case Commas :
		blCommas = true;
		break;

    case NoCommas :
		  blCommas = false;
		  break;            //Use for this code is expired */
   }
}

bool Money::operator==(const Money& amt) const
{
  return (getValue()==amt.getValue()); 
}

bool Money::operator!=(const Money& amt) const
{
   return !(*this == amt);
}

bool Money::operator>(const Money& amt) const
{
  return (getValue()>amt.getValue());
}

bool Money::operator<(const Money& amt) const
{
   return (getValue()<amt.getValue());
}

bool Money::operator>=(const Money& amt) const
{
   return !(*this<amt);
}

bool Money::operator<=(const Money& amt) const
{
   return !(*this > amt);
}

void Money::operator=(const double& amt)
{
   setValues(amt);
}

double Money::operator*(const double& amt) const
{
   return (getValue() * amt);
}

double Money::operator/(const double& amt) const
{
   return (getValue() / amt);
}

double Money::operator+(const double& amt) const
{
   return (getValue() + amt);
}

double Money::operator-(const double& amt) const
{
   return (getValue() - amt);
}

double Money::operator*(const Money& amt) const
{
   return (getValue() * amt.getValue());
}

double Money::operator/(const Money& amt) const
{
   return (getValue() / amt.getValue());
}

double Money::operator+(const Money& amt) const
{
   return (getValue() + amt.getValue());
}

double Money::operator-(const Money& amt) const
{
   return (getValue() - amt.getValue());
}

double Money::getValue() const
{
   double r;
   r = dollarAmt + (centAmt/100.);
   return r;
}
void Money::setValues(double amt)
{
   int i;
   i= 0;
   if(amt >= 0)
   {
      while(i<amt)
      {
         i++;
      }//End while loop

      if(i >amt)
      {
         i=i-1;
      }//end if statement
      amt = amt - i;
      centAmt=amt*100;
      dollarAmt = i;
   }//end if statement
   else
   {
      while(i>amt)
      {
         i= i -1;
      }//end while loop
      
      if(i<amt)
      {
         i = i+1;
      }//End if statement
      
      amt = amt - i;

      centAmt = amt *100;
      dollarAmt = i;
   }//end else statement
}//End Money method setValues

long Money::getDollars() const
{
   return dollarAmt;
}

short Money::getCents() const
{
   return centAmt;
}

double Money::Value() const
{
   return getValue();
}

ostream& operator<<(ostream& out, const Money obj)
{ 

   if( Money::blGeneral )
   {
      if( obj.Value() >= 0)
      {
        out << setw(Money::fieldSize) << setprecision(2) << obj.getDollars() << "." << obj.getCents();
      }//End if statement
      if( obj.Value() < 0)
      {
         out << setw(Money::fieldSize) << setprecision(2) << obj.getDollars() << "." << -obj.getCents();
      }//End else statement
   }//End if statement
   
   if( Money::blCurrency )
   {
      if( obj.Value() >= 0  )
      {
	out << setw(Money::fieldSize-2) << setprecision(2) << "$" << obj.getDollars() << "." << obj.getCents(); 
      }//End if statement
      if( obj.Value() < 0)
      {
        out << setw(Money::fieldSize-2) << setprecision(2) << "-$" << -obj.getDollars() << "." << -obj.getCents();
      }//End if statement
   }//End if statement

   if( Money::blAccounting )
   {
     if( obj.Value() >= 0 )
     {
       out << "$" << setw(Money::fieldSize-1) << obj.getDollars() << "." << obj.getCents();
     }//End if statement

     if( obj.Value() < 0 )
     {
       out << "$" << setw(Money::fieldSize-3) << "(" << -obj.getDollars() << "." << -obj.getCents() << ")";
     }//End if statement
   }//End if statement
   return out;
}//End ostream overload for class Money
