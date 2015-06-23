#!/usr/bin/python26
# Written by: Nathan Richgels
# The functions "indexAfter" and "insert" were provided by Michael H. Goldwasser
#and David Letscher.
#
# The purpose of this script is to create a SortedSet class, inherited from a
#previously written class, Set.  The SortedSet class will maintain all
#intentions from Set, while also keeping the Set ordered, alphabetically without
#any invocation from the application programmer.
"""
File: SortedSet.py
Author: Nathan Richgels
Asmt: Final Project/ SortedSet Class

  This file inherits everything from the Set class, and orders every item in
  the file, so as to make everything in the set presented in numerical/alphabetical
  order.
  This file also contains a body of code to test the correctness of the methods.
"""


# Import Set, and set the initial existence the same as Set.
from Set import *
class SortedSet(Set):
    """
    Maintains an ordered set of objects (without duplicates).
    """
    #~~~~~~~~~~~~~~~~~~~~~Data Dictionary~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    # __init__- (func) Copies the initial conecpt of Set.
    # indexAfter- (func) Determines where in a set an object should go, if
    #inserted.
    # insert- (func, OverRide(OR)) Adds the object to a set, using the
    #recommended location of indexAfter.
    # add- (func, OR) See insert.
    # __and__- (func, OR) '&' Operator forms the set intersection Set 'Other'
    #with this Set.
    # __or__- (func, OR) '|' Operator forms the set union of the 'other' with
    #this Set.
    # __xor__- (func, OR) '^' Operator forms the symmetric differences of the Set
    #'other' and this Set.
    # append- (func) See insert.
    # remove- (func) Takes an object out of a given sorted set.
    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    # *Additional function definitions are available from the Set class,
    #these defenitions are just overridden, or specific to this  class. 
    
    def __init__(self):
        Set.__init__(self)
    
    # Bring to existance Michael and David's indexAfter function, which
    #essentially calculates what index an object should be if it were inserted
    #into a set or list.
    ####indexAfter############################################################
    ##########################################################################
    def indexAfter(self, value):
	"""
        Find first index of an element strictly larger than given value.

        If no element is greater than given value, this returns the
        length of the set.
        """
        walk = 0
        while walk < len(self) and value >= self[walk]:
          walk += 1
        return walk

    # Bring to existance M&D's insert function, which inserts an object somewhere
    #in the Set if it's not in the Set, and places it at the claimed index
    #according to the indexAfter function.
    # *list.insert has to be replaced with Set.insert
    ####insert###############################################################
    #########################################################################
    def insert(self, value):
	"""
    	Adds given element to the sorted set.

    	If the value is already in the set, this has no effect.
    	Otherwise, it is added in the proper location.

    	value   element to be added to the set.
    	"""
        if value not in self:                  # avoid duplicates
          place = self.indexAfter(value)
          Set.insert(self, place, value)      # the parent's method

    # Now we continue overriding all of Set's previous definitions, so we know
    #the app programmer doesn't use a function that wouldn't exist if SortedSet
    #was written from scratch.
    # __str__, discard, __contains__, __len__, __repr__, __sub__ and __getitem__
    #don't need to be overridden.
    
    ####add##################################################################
    #########################################################################
    def add(self, item):
        """
        Adds given element to the sorted set.

        If the value is already in the set, this has no effect.
        Otherwise, it is added in the proper location.

        value   element to be added to the set.
        """

        # Add is the same thing as insert, except for less letters.
        self.insert(item)
        
    ####__and__##############################################################
    #########################################################################
    def __and__(self, other):
        """
        '&' Operator forms the set intersection Set 'other' with this Set

        process:  Forms a new SortedSet containing elements common to both operands
        precondition(s): 'other' is a Set to be 'intersected' with this SortedSet
        postcondition(s): returns a SortedSet which is the intersection of the
                          operands (i.e. contains elements that appear in
                          both operands).
                          Does not alter either operand.
        other  (Set)      Right hand operand ... use '&' operator"""
        #Keep the code the same, except make sure that instead of returning a
        #Set, you return a Sorted Set.
        _common_contents=SortedSet()
        for item in other._contents:
            if item in self._contents:
                _common_contents.add(item)
        return _common_contents
    
    ####__or__###############################################################
    #########################################################################
    def __or__(self, other):
        """
        '|' Operator forms the set union of the 'other' with this SortedSet

        prcoess:  Forms new SortedSet containing elemets in either of the operants
        precondition(s): 'other' is a Set to be 'unioned' to this SortedSet
        postcondition(s): returns a SortedSet which is the union of the operands
                           (i.e. contains elements that appear in at least
                            one operand).
                           Does not alter either operand."""
        #Again, code is identical, except make sure we return a Sorted set
        #instead of a Set.
        Union=SortedSet()
        for every1 in self._contents:
            Union.add(every1)
        for every2 in other._contents:
            Union.add(every2)
        return Union

    ####__xor__##############################################################
    #########################################################################
    def __xor__(self, other):
        """
        '^' Operator forms the symmetric differences of the Set 'other' and this SortedSet

        process:  Forms a SortedSet containing elements from the operands that are in
                  exactly one of the operand Sets
        precondition(s):  other is a Set which is the right operand in the operation
        postcondition(s): returns a SortedSet which contains all the elements in
                           the Left Hand SortedSet which are NOT in the Right Hand
                           Set.
                           Does not alter either operand.
        other  (Set)       The right hand operand ... use '^' operator."""
        #Once Again, same code, except xor returns a SortedSet.
        xor=SortedSet()
        for every1 in self._contents:
            xor.add(every1)
        for every2 in other._contents:
            xor.add(every2)
        for every3 in self._contents:
            if every3 in other._contents:
                xor.discard(every3)
        return xor

    # Since this is a case where the class is tailored for a pre-written program,
    #we must augment some functions that we know are going to appear in it.
    # These functions are synonyms of other functions.
    def append(self, item):
        """
    Adds given element to the sorted set.

    If the value is already in the set, this has no effect.
    Otherwise, it is added in the proper location.

    value   element to be added to the set.
    """
        self.insert(item)

    def remove(self, item):
        """
        Removes 'item' from the SortedSet

        process: Removes 'item' from SortedSet if it is in the SortedSet
        precondition(s): 'item' is thee lement of the SortedSet to discard
        postcondition(s): if present, the item is removed from the SortedSet.
                          Otherwise the SortedSet is unchanged"""
        self.discard(item)
    
if __name__=='__main__':
    print "Testing the acquisitions of objects in a SortedSet."
    print "CleaningSupplies=SortedSet()"
    CleaningSupplies=SortedSet()
    print "CleaningSupplies.insert('febreeze')"
    CleaningSupplies.insert('febreeze')
    print "CleaningSupplies.add('windex')"
    CleaningSupplies.add('windex')
    print "CleaningSupplies.append('vacuum')"
    CleaningSupplies.append('vacuum')
    print "print CleaningSupplies"
    print CleaningSupplies

    print ''
    print "Testing the remove function."
    print "CleaningSupplies.remove('vacuum')"
    CleaningSupplies.remove('vacuum')
    print "print CleaningSupplies"
    print CleaningSupplies

    print ''
    print "CleanThe is a Sorted Set included for testing."
    CleanThe=SortedSet()
    CleanThe.add('rug')
    CleanThe.add('sheets')
    CleanThe.add('windows')
    CleanThe.add('vacuum')
    CleanThe.add('windex')
    CleaningSupplies.add('vacuum')
    print 'print CleanThe'
    print CleanThe
    print 'print CleaningSupplies'
    print CleaningSupplies

    print ''
    print "Testing OverRidden Operator functions."
    print 'print CleanThe & CleaningSupplies'
    print CleanThe & CleaningSupplies
    print 'print CleanThe|CleaningSupplies'
    print CleanThe|CleaningSupplies
    print 'print CleanThe^CleaningSupplies'
    print CleanThe^CleaningSupplies
    
