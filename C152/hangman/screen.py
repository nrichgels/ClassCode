# file: screen.py
# author:  Rick Walker
# This file contains functions to control screen features for a VT102 compatible
# terminal ... including an xterm.


## cursorAt function #########################################################
def cursorAt(row = 0, column = 0):
    """ Function:  Places the cursor at the specified position on the terminal

	Preconditions: row and column, when specified, indicate the position on the
	               screen where the cursor should be located
	Postconditions:  Cursor is located as specified	

	row (int)        input ... specifies the line for the cursor
	column (int)     input ... specifies the space in the line for the cursor
	"""

    print chr(27) + '[' + str(row) + ';' + str(column) + 'H',
## End cursorAt ##############################################################

## clrScreen function ########################################################
def clrScreen():
    """ Function:  Clears the screen of a VT102 compatible terminal
    
	Preconditions:  none
	Postconditions:  The screen is cleared and the cursor is located in the
	                 upper left hand corner of the screen
	"""

    print chr(27) + '[2J',
    print chr(27) + '[H',
## End clrScreen #############################################################

## saveCursor function #######################################################
def saveCursor():
    """ Function:  Remembers the current cursor attributes 
    
        Preconditions:  none
	Postconditions:  The current cursor attributes are saved ... cursor is
			 unchanged.
	"""
    
    print chr(27) + '7',
## End saveCursor ############################################################

## restoreCursor function ####################################################
def restoreCursor():
    """ Function:  Resets cursor attributes to what they were when saveCursor
    		   was invoked
        
	Preconditions:  Cursor attributes must be saved with saveCursor prior to
			invoking this function, otherwise, results are unpredictable
	Postconditions:  Cursor attributes are restored to their values when 
			 saveCursor was last invoked.  However, see preconditions.
	"""
    print chr(27) + '8',
## END restoreCursor #########################################################

## clearToEnd function #######################################################
def clearToEnd(): 
    """ Function:  Clears the screen from the cursor position to the bottom
    		   of the screen.
        
	Preconditions:  none
	Postconditions:  The screen from the current cursor position to the end
			  of the screen is cleared.  Cursor remains in current
			  position.
	"""

    print chr(27) + '[J',
## End clearToEnd ############################################################
