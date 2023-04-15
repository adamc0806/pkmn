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
        names = random.choices(testFile, k = 6)
        print(names)
        


    # Main game
    def play(pokemonStats, pokemonMoves):
        pass



Game = game()
