# Auth: Adam Carrington.
# Date of Creation: 24/03/2023.
# All code written and documented by above mentioned author.

# Test Comment

# Standard packaged modules.
import os
import time
import random

# Author written modules.
from game import *
from settings import *
from login import *


# menu class, other code will be accessed through here.
# This class has access to everything in the codebase, to save 

class menu:

    # Declare attributes.
    def __init__(self):
        self.loggedIn = True # Set to true while programming to negate awkward issues. 
        # TODO: Change it later when testing properly
        
        

    # main menu
    def main(self):
        print("""
        ==============
        |MAIN    MENU|
        =============|
        |1. play     |
        |2. login    |
        |3. settings |
        |4. quit     |
        ==============""")
        option = int(input("Enter option (number) ==>")) # Take input

        # go to correct class
        if option == 1:
            if self.loggedIn == True: # Check if user logged in
                game.__init__(self)
                game.generateTeam()
                # game.play(pokemonStats, pokemonMoves)
            else:
                print("You need to log into an account first, loading login screen")
                account.__init__(self)
                account.main()

        elif option == 2:
            account.__init__(self)
            account.main()# login

        elif option == 3: 
            settings.__init__(self) # Check for settings file(s)
            settings.configSettings(self) # View or change settings.

        elif option == 4:
            quit() # Terminate the program

outputMenu = menu()
print(outputMenu.main())
