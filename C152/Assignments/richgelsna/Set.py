#!/usr/bin/python26
# Written by: Nathan Richgels
# The intention of this script is to define a class named Set that keeps track
# of distinct objects.
# ~~~~~~~~~~~~~~~~~~~~~~~~Data Dictionary~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Comma- (str)
# Set- (class) Creates a Set object
# 
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Create narration for Pydocs.
"""
File: Set.py
Author: Nathan Richgels
Asmt: Set Class

  This file contains the implementation of the Set class.
  The file also contains a body of code to test the correctness of the methods.
"""

# Create a constant string for organizing that can be used throughout different
#functions.

Comma=', '

# Initiate Class

class Set:
    #~~~~~~~~~~~~~~~~~~~~~Data Dictionary~~~~~~~~~~~~~~~~~~~~~~~~~~~
    # __init__- (func) Initializes the Set object being created
    # __str__- (func) Prepares a string representation for the print operation
    # add- (func) Places 'item' in the Set.
    # discard- (func) Removes 'item' from the Set.
    # __contains__- (func) Returns true if an item is within a set.
    # __and__- (func) '&' Operator forms the set intersection Set 'Other' with
    #this Set.
    # __len__- (func) Determines the cardinality of the object for len()
    #function.
    # __or__- (func) '|' Operator forms the set union of the 'other' with
    #this Set.
    # __repr__- (func) String for Display when referenced alone in
    #interactive shell.
    # __sub__- (func) '-' Operator forms the Set difference of the Set 'other'
    #and this Set.
    # __xor__- (func) '^' Operator forms the symmetric differences of the Set
    #'other' and this Set.
    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    
    #Explain what this particular Class does.
    """
    Creates a Set object
 
    A Set defines membership of elements from the "universe" of items
        under consideration.  As such, an item is uniquely represented as
        a member (i.e. will not appear in the Set more than once).  Methods
        are provided to add items to the set, remove items, and perform the
        operations of set intersection, union, and difference.  Printing
        a set results in the items being listed in '{' and '}'
    """
    ####The Constructor##################################################
    #####################################################################
    def __init__(self):
        #~~~~~~~~~~~~~~~~~~~~~~~Data Dictionary~~~~~~~~~~~~~~~~~~~~~~~~~~
        # self._contents- (list) A list that is limited to act as though
        #it's a set.
        #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        """
        Initializes the Set object being created
 
        process:  Initializes object
        precondition(s): none
        postcondition(s): the Set object is initialized to the empty state
        """
        
        self._contents=list()
        
    ####__str__#########################################################
    ####################################################################
    def __str__(self):
        
        """
        Prepares a string representation for the print operation

        process: Returns a string representation for the Set
        precondition(s): none
        postcondition(s): Returns a string representation to 'print'.
                          The Set remains unchanged."""
        # Join removes the brackets of the list, and replaces the comma and
        #space.  All that's left is adding the Elephent Ear brackets: { }.
        return '{'+ Comma.join(self._contents)+'}'

    ####add###########################################################
    ##################################################################
    def add(self, item):
        #~~~~~~Data Dictionary~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        # item- (obj) Programmer's input to their Set. Makes sure it's
        #not already in the set before adding itself to the set.
        #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        """
        Places 'item' in the Set

        process: Adds 'item' to set if it not already in set
        precondition(s): 'item' is to be added to list
        postcondition(s): if 'item' is not in list, it is added...
                                  otherwise the Set remains as is"""
        # After assuring that what's being added to the list isn't already
        #in there, we append the programmer's input to the list.  With that
        #restriction, it won't be possible to have two objects in a list.
        if item not in self._contents:
            self._contents.append(item)
            
    ####discard#######################################################
    ##################################################################
    def discard(self, item):
        #~~~~~Data Dictionary~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        # item- (obj) Programmer's input to remove something from their Set.
        #Makes sure that it's actually in the list before it removes itself.
        #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        
        """
        Removes 'item' from the Set

        process: Removes 'item' from set if it is in the set
        precondition(s): 'item' is hte lement of the Set to discard
        postcondition(s): if present, the item is removed from the Set.
                          Otherwise the Set is unchanged"""

        # After assuring that item is in the list, it gets taken out.
        # If the programmer tries to take something out that's not there,
        #the if statement is ignored, imitating the Set effect of "nothing
        #happening".
        if item in self._contents:
            self._contents.remove(item)
            
    ####__contains__#################################################
    #################################################################
    def __contains__(self, item):
        #~~~~~Data Dictionary~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        # item- (obj) The programmer's query of whether or not the
        #object is in their set.
        #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        
        """
        'in' Operation determines if 'item is in the Set or not

        process:  Boolean- Determines of 'item' is in the Set or not
        precondition(s): 'item' is the element to check for
        postcondition(s): returns true if 'item' is in Set, false otherwise
                          The Set remains unchanged.
        item  (any)     Left hand operand ... use 'in' operator"""

        # If an object is in the list, then the statement is True.  If there
        #is any other result at all, (a.k.a if the object isn't in the list)
        #then the statement is False.
        
        if item in self._contents:
            return True
        else:
            return False

    def __and__(self, other):
        #~~~~~~~Data Dictionary~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        # _common_contents- (Set) filled with common objects that are within
        #two sets of a programmer.
        # item- (obj) Each object in the list of a programmer's second Set.
        #It is compared individually to the objects of the first list, and
        #added to a third Set if it is in the first two sets.
        # other._contents- (Set) A Set interacting with the primary Set
        #(made with the same class functions) via an operater.
        #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        
        """
        '&' Operator forms the set intersection Set 'other' with this Set

        process:  Forms a new Set containing elements common to both operands
        precondition(s): 'other' is a Set to be 'intersected' with this Set
        postcondition(s): returns a Set which is the intersection of the
                          operands (i.e. contains elements that appear in
                          both operands).
                          Does not alter either operand.
        other  (Set)      Right hand operand ... use '&' operator"""

        # Check every object in a user's secondary list, sequentially check if
        #the object is in the user's primary list. If it is, add the object
        #into a Set, and return the Set of common objects to the programmer.
        _common_contents=Set()
        for item in other._contents:
            if item in self._contents:
                _common_contents.add(item)
        return _common_contents

    ####__len__##################################################
    #############################################################
    def __len__(self):

        #~~~~~Data Dictionary~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        # every- (obj) Takes place of every object in the Set once, but
        #essentially doesn't have any other use.
        #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        
        """
        Determines the cardinality of the object for len() function

        process:  Returns the number of elements in the Set
        precondition(s): none
        postcondition(s): Returns an integer count of the elements in the Set.
                           The Set remains unchanged."""

        # Set default length of the list to 0, then loop the list once for
        #every object within it, adding one to the length of each repetition.
        length=0
        for every in self._contents:
            length+=1
        return length

    ####__or__##################################################
    ############################################################
    def __or__(self, other):

        #~~~~~Data Dictionary~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        # Union- (Set) The set that is the combination of any two sets put
        #together.
        # every1- (obj) Represents every object in the programmer's primary
        #set.
        # every2- (obj) Represents every object in the programmer's secondary
        #set.
        # other._contents- (Set) A Set interacting with the primary Set
        #(made with the same class functions) via an operater.
        #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        """
        '|' Operator forms the set union of the 'other' with this Set

        prcoess:  Forms new Set containing elemets in either of the operants
        precondition(s): 'other' is a Set to be 'unioned' to this Set
        postcondition(s): returns a Set which is the union of the operands
                           (i.e. contains elements that appear in at least
                            one operand).
                           Does not alter either operand."""

        # Create a set that adds every object into it from any two Sets the
        #Programmer makes.  Gives the user back the new set.
        Union=Set()
        for every1 in self._contents:
            Union.add(every1)
        for every2 in other._contents:
            Union.add(every2)
        return Union
    
    ####__repr__#######################################################
    ###################################################################
    def __repr__(self):

        """
        String for display when referenced alone in an interactive shell

        process:  Returns a string representation for the Set
        precondition(s): none
        postcondition(s): Set is unaltered."""
        # The pre defined __repr__ meaning does all the work.  All I have to do
        #is provide a correct string, then the functions results will be
        #printed out in the shell without the print command.
        return '{'+ Comma.join(self._contents)+'}'

    ####__sub__#######################################################
    ##################################################################
    def __sub__(self, other):

        #~~~~~Data Dictionary~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        # Subtracted- (Set)  Every object in the primary set is added to it,
        #and every object from the seocondary set is attempted to take away
        #from it. Then it's reported to the user.
        # every1- (obj) Takes the place of every object of the primary set, and
        #adds it to the third set.
        # every2- (obj) Takes the place of every object of the secondary set,
        #and takes it away from the third set.
        # other._contents- (Set) Secondary Set.
        #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        """
        '-' Operator forms the set difference of the Set 'other' and this Set

        process:  Forms Set that contains elements in this Set that are not in
                  Set 'other'
        precondition(s): other is a Set whose elements are removed from this Set
        postcondition(s): returns a Set which contains all the elements in
                           the Left Hand Set which are NOT in the Right Hand
                           Set.
                           Does not alter either operand
        other  (Set)     Right hand operand ... use '-' operator"""

        # Add every object to a new Set, then for every object in the secondary
        #set, remove it from the new set, and return the new set to the
        #programmer.
        Subtracted=Set()
        for every1 in self._contents:
            Subtracted.add(every1)
        for every2 in other._contents:
            Subtracted.discard(every2)
        return Subtracted

    ####__xor__#####################################################
    ################################################################
    def __xor__(self, other):

        """
        '^' Operator forms the symmetric differences of the Set 'other' and this Set

        process:  Forms a Set containing elements from the operands that are in
                  exactly one of the oeprand Sets
        precondition(s):  other is a Set which is the right operand in the operation
        postcondition(s): returns a Set which contains all the elements in
                           the Left Hand Set which are NOT in the Right Hand
                           Set.
                           Does not alter either operand.
        other  (Set)       The right hand operand ... use '^' operator."""
        
        xor=Set()
        for every1 in self._contents:
            xor.add(every1)
        for every2 in self._contents:
            xor.discard(every2)
        return xor

if __name__=='__main__':
    print "Class Works: Jerry is a Set!"
    Jerry= Set()
    print "[Jerry= Set()]-->" + str(Jerry)
    
    print ""
    print "Jerry can grow larger, but only if we add things to Jerry we"
    print "haven't before!"
    Jerry.add("cheese")
    Jerry.add("water")
    Jerry.add("Peanut Butter")
    print "Jerry.add('cheese')"
    print "Jerry.add('water')"
    print "Jerry.add('Peanut Butter')"
    print "[print Jerry] " + str(Jerry)
    print ""
    print "Jerry gets smaller when you take away from Jerry too. But only"
    print "if we take away what he obviously has."
    Jerry.discard("water")
    Jerry.discard("pocket lint")
    print "Jerry.discard('water')"
    print "Jerry.discard('pocket lint')"
    print "[print Jerry] " + str(Jerry)
    print ""
    print "Let's try and guess what Jerry has."
    print "[Cherry in Jerry]--> " + str("Cherry" in Jerry)
    print "[cheese in Jerry]--> " + str("cheese" in Jerry)
    print ""
    Jerry.add("water")
    Tom=Set()
    Tom.add("milk")
    Tom.add("CatNip")
    Tom.add("Peanut Butter")
    print "Jerry. add('water')"
    print "Tom=Set()"
    print "Tom.add('milk')"
    print "Tom.add('CatNip')"
    print "Tom.add('Peanut Butter')"
    print "What does Tom and Jerry both have?"
    print "[Tom & Jerry]--> " + str(Tom&Jerry)

    print ""
    print "How many objects does Tom have?"
    print "[len(Tom)]--> " + str(len(Tom))
    print ""
    print "Let's see how many possessions Tom and Jerry have between the two"
    print "of them."
    print "[Tom|Jerry]--> " + str(Tom|Jerry)

    print ""
    print "Owner confiscated everything Tom had.  Also, whatever Tom had"
    print "confiscated, Jerry had confiscated too! Jerry only has a couple"
    print "items left."
    print "[Jerry-Tom]--> " + str(Jerry-Tom)
