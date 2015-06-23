// Author: Nathan Richgels
// File: array.h
// Date: 2/26/2013
// Class: CSIS352
// Assignment 3

#ifndef __array_H__
#define __array_H__
#include <stdexcept>
using namespace std;

namespace ArrayNameSpace
{
/************************CLASS DECLERATION****************************
 * *******************************************************************/
template <class T>
class Array
{
   public:
      // Constructor
      // Creates an Array object without any available indeces
      // Paramaters: none
      explicit Array();
      
      // Constructor
      // Creates an Array object with a constant amount of indeces
      // Paramaters: int: Initial amount of indeces
      explicit Array(int);
      
      // Constructor
      // Creates an Array object with an alternate idealogy behind the indeces
      // Paramaters: int: Starting index of the Array
      //            int: Ending index of the array
      explicit Array(int, int);
      
      // Destructor
      // Recycles dynamic memory once the program using this class
      // is finished
      // Paramaters: None
      ~Array();
      
      // Copy Constructor
      // Copies dynamic memory when an array object is passed to a 
      // (pass by value) function
      // Paramaters: Array: What the new array is copying from
      Array(const Array&);
      
      // Bracket ([]) overload
      // Preconditions: Object is initialized, and a valid index is set within
      // Postconditions: Returns the value at the given index of the array.
      T& operator[](const int& index) throw (out_of_range);
      
      // Bracket([]) overload
      // Preconditions: Object is initialized, and a valid index is set within
      // Postconditions: Returns the value at the given index of the array.
      //                 Throws an exception if invalid index is entered
      //   *Used when an array is pass by reference
      const T& operator[](const int& index) const throw (out_of_range);
      
      // Method compares Array to another Array
      // Precondition: Both arrays are initialized
      // Postcondition: Returns true if arrays are equal sized and have the
      //                same value in each index- false otherwise
      bool operator==(const Array& other) const;
      
      // Method compares Array to another Array
      // Precondition: Both arrays are initialized
      // Postcondition: Returns true if Arrays are of unequal size or have
      // unmatching values within the length of the Array- false otherwise
      bool operator!=(const Array& other) const;
      
      // Method compares Array to another Array
      // Precondition: Both arrays are initialized
      // Postcondition: Returns true if there is a value less than
      // a value in the other array at the same index, or if the array is 
      // shorter than the other array- false otherwise
      bool operator<(const Array& other) const;
      
      // Method compares Array to another Array
      // Precondition: Both arrays are initialized
      // Postcondition: Returns true if the Array is longer than the other
      // the other Array, or has a value greater than the other array at
      // a matching index- false otherwise
      bool operator>(const Array& other) const;
      
      // Method compares Array to another Array
      // Precondition: Both arays are initialized
      // Postcondition: Returns true if the Array is greater than the other
      // Array, has more indeces, or matches every index.
      bool operator>=(const Array& other) const;
      
      // Method compares Array to another Array
      // Precondition: Both arrays are initialized
      // Postcondition: Returns true if hte Array is less than the other Array,
      // has less indeces, or matches every index.
      bool operator<=(const Array& other) const;
      
      // Method sets all values equal to the other array
      // Precondition: Both arrays are initialized
      // Postcondition: All values in Array are matching the
      // other array's
      const Array& operator=(const Array& other);
      
      // Method changes the amount of available indeces in the Array
      // Precondition: Array is initialized
      // Postcondition: The amount of indeces is changed to given integer
      void Resize(const int&);
      
      // Method returns the number of indeces in the Array
      // Preconditions: Array has been initialized
      // Postconditions: Integer representing total indeces is returned
      int Size() const;
      
      
   private:
      int arraySize;
      int startIndiceInt;
      int endIndiceInt;
      bool expandedIntIndexing;
      T* theArray;
};//End class defenition

/************************CLASS IMPLEMENTATION*************************
 ***************************CONSTRUCTORS******************************/

template <class T>
Array<T>::Array()
{
   arraySize = 0;
   theArray = new T[arraySize];
   expandedIntIndexing = false;
}//End constructor

template <class T>
Array<T>::Array(int n)
{
   if(n<0)
      throw invalid_argument("Size of Array cannot be less than 0.");
   arraySize = n;
   theArray= new T[arraySize];
   expandedIntIndexing = false;
}//End constructor

template <class T>
Array<T>::Array(int m, int n)
{
   if(n<m)
      throw domain_error( "The second paramater must be a value larger than " + m);
   arraySize = n-m+1;
   startIndiceInt = m;
   endIndiceInt = n;
   theArray = new T[arraySize];
   expandedIntIndexing = true;
}//End constructor

/************************CLASS IMPLEMENTATION*************************
 ****************************DESTRUCTORS******************************/
template <class T>
Array<T>::~Array()
{
   delete [] theArray;
   theArray = NULL;
}//End destructor


/************************CLASS IMPLEMENTATION*************************
 *************************COPY CONSTRUCTORS***************************/
template <class T>
Array<T>::Array(const Array<T>& anArray)
{
   arraySize = anArray.arraySize;
   theArray = new T[arraySize];
   for(int i = 0; i< arraySize; i++)
   {
      theArray[i] = anArray.theArray[i];
   }//End for loop
   expandedIntIndexing = anArray.expandedIntIndexing;
   startIndiceInt = anArray.startIndiceInt;
   endIndiceInt = anArray.endIndiceInt;
   
}//End copy constructor


/************************CLASS IMPLEMENTATION*************************
 *************************OPERATOR OVERLOADS**************************/
template <class T>
T& Array<T>::operator[](const int& index) throw (out_of_range)
{
   // throw an exception if outside the array boundaries
   if(!expandedIntIndexing)
   {
      if (index >= arraySize || index < 0)
      {
      throw out_of_range( index + " is an index that does not exist within the Array's boundaries.");
      }//End index if statement
      else
         return theArray[index];
   }//End if expandedIntIndexing statement
   else
   {
      if((index - startIndiceInt) >= arraySize || (index - startIndiceInt) < 0)
      {
         throw out_of_range( index + " is an index that does not exist within the Array's boundaries.");
      }//End if statement
      else
         return theArray[index - startIndiceInt];
   }//end else statement
}//End operator overload []

// the following method allows a const pass by reference argument
// For example: void func(const Array& array)
template <class T>
const T& Array<T>::operator[]( const int& index) const throw (out_of_range)
{
//    throw an exception if outside the array boundaries
      if(!expandedIntIndexing)
   {
      if (index >= arraySize || index < 0)
      {
      throw out_of_range( index + " is an index that does not exist within the Array's boundaries.");
      }//End index if statement
      else
         return theArray[index];
   }//End if expandedIntIndexing statement
   else
   {
      if((index - startIndiceInt) >= arraySize || (index - startIndiceInt) < 0)
      {
         throw out_of_range( index + " is an index that does not exist within the Array's boundaries.");
      }//End if statement
      else
         return theArray[index - startIndiceInt];
   }//end else statement
}//End operator overload [] const Pass by reference

template <class T>
const Array<T>& Array<T>::operator=(const Array<T>& other)
{
   if( &other == this)
      return *this;
   
   delete [] theArray;
   arraySize = other.arraySize;
   theArray = new T[arraySize];
   for(int i = 0; i < arraySize; i++)
   {
      theArray[i] = other.theArray[i];
   }//End for loop
   expandedIntIndexing = other.expandedIntIndexing;
   startIndiceInt = other.startIndiceInt;
   endIndiceInt=other.endIndiceInt;
   return *this;
}//End operator overload =


/************************CLASS IMPLEMENTATION*************************
 ********************RELATIONAL OPERATOR OVERLOADS********************/
template <class T>
bool Array<T>::operator==(const Array& other) const
{
   if(Size()!=other.Size())
      return false;
   else
   {
      for(int i = 0; i<Size(); i++)
      {
         if(theArray[i] != other.theArray[i])
            return false;
      }//End for statement
      return true;
   }//End else statement
}//End operator== overload

template <class T>
bool Array<T>::operator!=(const Array& other) const
{
   if( *this == other)
      return false;
   else
      return true;
}//End operator!= overload

template <class T>
bool Array<T>::operator<(const Array& other) const
{
   if(Size()<other.Size() )
   {
      for(int i = 0; i< Size(); i++)
      {
         if( theArray[i] != other.theArray[i])
            return(theArray[i]<other.theArray[i]);
      }//End for loop
      return true;
   }//End if statement
   else if(Size()>other.Size()|| Size() == other.Size())
   {
      for(int i = 0; i< other.Size(); i++)
      {
         if( theArray[i] != other.theArray[i])
            return(theArray[i]<other.theArray[i]);
      }//End for loop
      return false;
   }//End elif statement
      
}//End operator< overload

template <class T>
bool Array<T>::operator>(const Array& other) const
{
   if(Size()<other.Size() || Size() == other.Size())
   {
      for(int i = 0; i< Size(); i++)
      {
         if( theArray[i] != other.theArray[i])
            return(theArray[i]>other.theArray[i]);
      }//End for loop
      return false;
   }//End if statement  
   
   else if(Size()>other.Size())
   {
      for(int i = 0; i< other.Size(); i++)
      {
         if( theArray[i] != other.theArray[i])
            return(theArray[i]>other.theArray[i]);
      }//End for loop
      return true;
   }//End elif statement
}//End operator> overload

template <class T>
bool Array<T>::operator<=(const Array& other) const
{
   return !(*this > other);
}//End operator <= overload

template <class T>
bool Array<T>::operator>=(const Array& other) const
{
   return!(*this < other);
}//End operator >= overload

/************************CLASS IMPLEMENTATION*************************
 **************************PUBLIC METHODS*****************************/
template <class T>
void Array<T>::Resize(const int& newSize)
{
   if(newSize<0)
      throw invalid_argument("Size of Array cannot be less than 0.");
   if(newSize==arraySize)
      return;
   if(newSize>arraySize)
   {
      T* temp = new T[newSize];
      endIndiceInt = startIndiceInt + newSize;
      for( int i = 0; i < arraySize; i++)
      {
         temp[i] = theArray[i];
      }//End for loop
      arraySize = newSize;
      delete [] theArray;
      theArray = temp;
      temp = NULL;
   }//End if statement
   if(newSize<arraySize)
   {
      T* temp = new T[newSize];
      endIndiceInt = startIndiceInt + newSize;
      for( int i = 0; i < newSize; i++)
      {
         temp[i] = theArray[i];
      }//End for loop
      arraySize = newSize;
   }//End if statement
}//End method Resize

   
template <class T>
int Array<T>::Size() const
{
   return arraySize;
}//End method Size
}//End ArrayNameSpace
#endif