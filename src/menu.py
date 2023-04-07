# Auth: Adam Carrington.
# Date of Creation: 24/03/2023.
# All code written and documented by above mentioned author.


# Standard packaged modules.
import os
import time
import random

# Author written modules.
from game import game
from view import view
from settings import settings


# menu class, other code will be accessed through here.
# This class acts as the main file, where the entire codebase will be executed from.

class menu:

    # Declare attributes.
    def __init__(self):
        self.loggedIn = True
        self.p = open("Stats.json", "r") # Why tf this no open, it's literally in the same directory???
        
        

    # main menu
    def main(self):
        print("""
        ==============
        |MAIN    MENU|
        =============|
        |1. play     |
        |2. view pkmn|
        |3. settings |
        |4. quit     |
        ==============""")
        option = int(input("Enter option (number) ==>")) # Take input

        # go to correct class
        if option == 1:
            if self.loggedIn == True: # Check if user logged in
                game.game(self)
            else:
                print("You need to log into an account first, loading login screen")
                pass # Go to login menu inside settings class
        elif option == 2:
            pass # View pokemon
        elif option == 3:
            settings.__init__(self)
        elif option == 4:
            quit() # Terminate the program

outputMenu = menu()
print(outputMenu.main())