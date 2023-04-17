# Auth: Adam Carrington.
# Date of Creation: 26/03/2023.
# All code written and documented by above mentioned author.

# Built in modules
import os
import time
import random
import json

# Author written modules
# from login import *
from settings import *



class game:


    # Open stats and moves jsons as attributes
    def __init__(self):

        self.pokemonStats = open("Stats.json", "r")
        self.pokemonMoves = open("Moves.json", "r")
        self.pstats = self.pokemonStats.read()
        
    # Generate random team
    def generateTeam():
        testFile = open("pokemonNames.txt", "r").read().splitlines()
        names = [[],
                 [],
                 [],
                 [],
                 [],
                 []]
        for i in range(0,6):
            placeholder = random.choice(testFile)
            names[i].append(placeholder)
            for j in range(0,5):
                stat = int(random.randint(0,100))
                names[i][j].append(stats) # Refuses to append because it's not a string... really python? 
        print(names)
        # TODO: Generate stats 
        # 1 = attack
        # 2 = defense
        # 3 = sp.attack
        # 4 = sp.defense
        # 5 = speed
        
        


    # Main game
    def play(pokemonStats, pokemonMoves):
        print("GAME STARTING......")
        print("YOUR POKEMON\n", names[0:])
        moveChoice = int(input("What move would you like to use?"))
        if moveChoice == 1:
            print("You used: ", moveChoice[])



Game = game()
