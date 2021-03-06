// Author: Nathan Richgels
// File: money.h
// Date: 1/31/2012
// Class: CSIS352
// Assignment 1

#ifndef __MONEY_H__
#define __MONEY_H__
using namespace std;

enum formatType {General, Currency, Accounting, Cents, Round, Truncate,
             DollarSign, NoDollarSign, Commas, NoCommas};
             
class Money
{
   public:
      // Constructor
      // Creates a money object.
      // Paramaters: double: Initializes current value of Money object.
      //                     Default value is 0.
      Money(double = 0);
      
      // Method determines how much space is alotted for output.
      // Preconditions: none
      // Postconditions:  Amount of character space is alotted in front of the 
      //                 decimal.
      // Paramaters: integer: describes how much space is alotted for output.
      static void setFieldSize(const int& size);
      
      // Method Determines one of three formatting types: General, Accounting,
      // or Currency
      // Preconditions: none
      // Postconditions: Output is reformatted.
      // Paramaters: formatType: Can be of value General, Accounting, or
      //                         Currency.
      static void setFormat(const formatType& type);
      
      // Method returns how many dollars the object is worth.
      // Preconditions: Object is initialized.
      // Postconditions: Integer representing dollars is returned.
      // Paramaters: none
      long getDollars() const;
      
      // Method returns how many parts out of 100 additional to the dollar
      // that this object contains.
      // Preconditions: Object is initialized.
      // Postconditions: Integer representing cents is returned.
      // Paramaters: none
      short getCents() const;
      
      // Method returns total amount of currency that the object contains.
      // Preconditions: object is initialized
      // Postconditions: double representing currency is returned.
      double Value() const;
      
      // Method compares currency value to a different Money object.
      // Preconditions: Two seperate Money objects are initialized.
      // Postconditions: boolean returned
      bool operator==(const Money& amt) const;
      
      // Method compares currency value to a different Money object.
      // Preconditions: Two seperate Money objects are initialized.
      // Postconditions: boolean returned
      bool operator!=(const Money& amt) const;
      
      // Method compares currency value to a different Money object.
      // Preconditions: Two seperate Money objects are initialized.
      // Postconditions: boolean returned
      bool operator>(const Money& amt) const;
      
      // Method compares currency value to a different Money object.
      // Preconditions: Two seperate Money objects are initialized.
      // Postconditions: boolean returned
      bool operator<(const Money& amt) const;
      
      // Method compares currency value to a different Money object.
      // Preconditions: Two seperate Money objects are initialized.
      // Postconditions: boolean returned
      bool operator<=(const Money& amt) const;
      
      // Method compares currency value to a different Money object.
      // Preconditions: Two seperate Money objects are initialized.
      // Postconditions: boolean returned
      bool operator>=(const Money& amt) const;
      
      // Method sets the currency value of the object.
      // Preconditions: Object is initialized.
      // Postconditions: Object's value matches given value.
      void operator=(const double& amt);
      
      // Method compares currency value to a double.
      // Preconditions: Money object is initiialized.
      // Postconditions: boolean returned
      double operator*(const double& amt) const;
      
      // Method compares currency value to a double.
      // Preconditions: Money object is initiialized.
      // Postconditions: boolean returned
      double operator/(const double& amt) const;
      
      // Method compares currency value to a double.
      // Preconditions: Money object is initiialized.
      // Postconditions: boolean returned
      double operator+(const double& amt) const;
      
      // Method compares currency value to a double.
      // Preconditions: Money object is initiialized.
      // Postconditions: boolean returned
      double operator-(const double& amt) const;
      
      // Method compares currency value to a double.
      // Preconditions: Money object is initiialized.
      // Postconditions: boolean returned
      double operator*(const Money& amt) const;
      
      // Method compares currency value to a double.
      // Preconditions: Money object is initiialized.
      // Postconditions: boolean returned
      double operator/(const Money& amt) const;
      
      // Method compares currency value to a double.
      // Preconditions: Money object is initiialized.
      // Postconditions: boolean returned
      double operator+(const Money& amt) const;
      
      // Method compares currency value to a double.
      // Preconditions: Money object is initiialized.
      // Postconditions: boolean returned
      double operator-(const Money& amt) const;
      
      // function rewrites the outstream.
      // Precondition: none
      // Postcondition: outputs value in given formatting type.
      friend ostream& operator<<(ostream& out, const Money obj);
   private:
      long dollarAmt;  //Stores Dollar amount of object.
      
      short centAmt;  //Stores Cent ammount of object.
      
      static int fieldSize;  //Amount of space leading the decimal poiint when
                             //outputting the money object.
                             
      static bool blCommas;  //Represents programmers want for commas in output
      
      static bool blDollarSign;  //Represents programmer's want for Dollar
                                 //Sign in output
                                 
      static bool blTruncate;  //Represent Programmer's want for truncating
                               //Decimal value in output.
                               
      static bool blRound;  //Represents Programmer's want for rounding
                            //decimal value in output.
                            
      static bool blGeneral;  //If true, General formatting for output is
                              //Enabled.
                              
      static bool blAccounting;  //If true, Accounting format for output is
                                 //Enabled.
                                 
      static bool blCurrency;  //If true, Currency format for output is
                               //Enabled.
                               
      void setValues(double amt); //Private function provides arithmetic for
                                  //Various other functions.
      
      double getValue() const;  //Private function provides arithmetic for
                                //Various other functions.
                                
      friend string intToString(int, Money obj);  //Failed attempt at writing
                                                  //commas into ints, after
                                                  //turning the int into a
                                                  //string.
};//End class Money

#endif
