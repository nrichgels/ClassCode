# Enter your answer code in the labeled sections, below.  The unit test code 
# included is for the IDPerson and  is commented out so it won't interfere
# with unit test code you may want to include to test your Person class.
# Feel free to insert whatever test code you want.  The test code I have 
# supplied can be used to help answer parts d) - f).  It can be uncommented
# once you actually HAVE an IDPerson class to test.
  
# a) ############### Create your Person class definition, here ###################
class Person:
    def __init__(self, first='', last=''):
        self._fname=first
        self._lname=last

    def setName(self, first, last):
        self._fname=first
        self._lname=last

    def getFName(self):
        return self._fname

    def getLName(self):
        return self._lname

    
    # b) ####### Add the method that will produce the desired output format ######
    def __str__(self):
        return self._lname +", " + self._fname
# c) ########### Derive the IDPerson class from the Person class, here ###########        
class IDPerson(Person):
    def __init__(self, first='', last='', ID= 0):
        self._fname=first
        self._lname=last
        self._ID=ID

    def setID(self, ID):
        self._ID=ID

    def getID(self):
        return self._ID

    def __str__(self):
        return self._lname +", " + self._fname + ";  " + "ID:" + str(self._ID)

    def __lt__(self, other):
        if self._ID<other._ID:
            return True
        else:
            return False
    def __gt__(self, other):
        if self._ID>other._ID:
            return True
        else:
            return False

    def __eq__(self, other):
        if self._ID==other._ID:
            return True
        else:
            return False
        
        
        
        
    

################ Unit test code, here ############################################        
if __name__ == "__main__":

    
    fred = IDPerson('fred', 'flintstone', 6666)
    barney = IDPerson()
    barney.setName('barney', 'rubble')
    barney.setID(8473)
    print fred.getFName() + ' ... ' + fred.getLName()
    print fred
    print barney
    wilma = IDPerson('wilma', 'flintstone', 1234)
    betty = IDPerson()
    betty.setID(2345)
    betty.setName("betty", "rubble")
    print wilma
    print betty
    
    
    # d) ### Create a list consisting of the above IDPersons, here ###############
    IDPersons=list(fred, barney, wilma, betty)
    
    # e) ### Sort the list and print it out, here ################################
    IDPersons.sort()
    print IDPersons
    # f) ### Open the file 'mypeople' for writing and write your list, here ... ##
    ######## One person per line #################################################
    
