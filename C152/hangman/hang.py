#!/usr/bin/python26
# Author: Nathan Richgels
# The purpose of this program is to start a sample game of Hangman, where
#the user can choose to play the game either graphically using the cs1graphics
#package, or play a text based game.
#
#~~~~~~~~~~~~~~~~~Data Dictionary~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#

# Import the UI.
from hang_ui import *

# Get a word from the user.
Hangword=raw_input("Please enter a word to trial a friend in a game of Hangman! ")
Lowerword=Hangword.lower()

# Make the user decide if they want a graphical interface, or a text-based.
Destination=raw_input("\nEnter G if you want a graphical interface.\nEnter anything else if you want a text-based game. ")

# Make a constant that will only be True after the game is over.
constant=False

#Select what version to be used according to the user's input.
if Destination.lower()=='g':
    
    #Tell the interface how many letters to expect.
    Gvisual=GUI(len(Hangword))
    
    # While the game is not over, repeat the input opportunities for the user.
    while constant==False:
        # Tell the interface to guess a new letter. If the letter is in the
        #user's word,then Success is True, other wise they have False success.
        
        Guess=Gvisual.prompt()
        Success=Guess in Lowerword
        
        #Repeat always starts out at 0 when the user makes a new guess.
        Repeat=0
        
        # This loop evaluates whether and when the interface should be updated.
        while Repeat>=0:
            # OneMore is always True at the beginning of evaluation.
            OneMore=True
            
            # Repeat now becomes the index of the first found guess.  If no more
            #guesses are to be found, then Repeat automatically becomes -1,
            #causing the loop to come to an inevitable end.
            Repeat=Lowerword.find(Guess, Repeat)
            # If there are no more guesses correct guesses, OneMore will
            #be false.
            if Repeat<0:
                OneMore=False
                
            #    
            # If OneMore is true, then that means Repeat is greater than 0, and
            #in the correct location of where a guess should be installed,
            #meaning that the UI update is essential.
            #
            # If Success is False, then that means the UI needs to be updated
            #to report a wrong answer.
            #
            # If OneMore is false, Repeat is -1 meaning there are no immediate
            #right spots for the guess.  If Success is also true, that means
            #the guess was correct and that all guesses were already installed
            #and that there is no place for anymore letters, hence meaning
            #an interface update isn't neccessary, and indeed is harmful.
            if OneMore==True or Success==False:
                constant=Gvisual.update_status(Success, Repeat, Guess)
            
            # Adds one more to Repeat, so Repeat can search the rest of the
            #word for anymore correct letters found in the word. Unless there
            #are no more correct letters, meaning that Repeat = -1. Then 1
            #more won't be added so that the conditions of the loop will end.
            if Repeat>=0:
                Repeat+=1
else:
    #Tell the Interface how many letters to expect.
    Tvisual=TUI(len(Hangword))
    
    # While the game is not over, repeat the input opportunities for the user.
    while constant==False:
        
        # Tell the interface to guess a new letter. If the letter is in the
        #user's word,then Success is True, other wise they have False success.
        Guess=Tvisual.prompt()
        Success=Guess in Lowerword
        
        #Repeat always starts out at 0 when the user makes a new guess.
        Repeat=0
        
        # This loop evaluates whether and when the interface should be updated.
        while Repeat>=0:
            
            # OneMore is always True at the beginning of evaluation.
            OneMore=True
            
            # Repeat now becomes the index of the first found guess.  If no more
            #guesses are to be found, then Repeat automatically becomes -1,
            #causing the loop to come to an inevitable end.
            Repeat=Lowerword.find(Guess, Repeat)

            # If there are no more guesses correct guesses, OneMore will
            #be false.
            if Repeat<0:
                OneMore=False

            #    
            # If OneMore is true, then that means Repeat is greater than 0, and
            #in the correct location of where a guess should be installed,
            #meaning that the UI update is essential.
            #
            # If Success is False, then that means the UI needs to be updated
            #to report a wrong answer.
            #
            # If OneMore is false, Repeat is -1 meaning there are no immediate
            #right spots for the guess.  If Success is also true, that means
            #the guess was correct and that all guesses were already installed
            #and that there is no place for anymore letters, hence meaning
            #an interface update isn't neccessary, and indeed is harmful.
            if OneMore==True or Success==False:
                constant=Tvisual.update_status(Success, Repeat, Guess)

            # Adds one more to Repeat, so Repeat can search the rest of the
            #word for anymore correct letters found in the word. Unless there
            #are no more correct letters, meaning that Repeat = -1. Then 1
            #more won't be added so that the conditions of the loop will end.
            if Repeat>=0:
                Repeat=Repeat+1
            

