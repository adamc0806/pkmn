# Auth: Adam Carrington.
# Date of Creation: 26/03/2023.
# All code written and documented by above mentioned author.

# Built in modules
import os
import time
import random

# Author written modules
from settings import *



class game:


    def __init__(self):
        # Open stats and moves jsons as attributes
        self.pokemonStats = open("Stats.json", "r")
        self.pokemonMoves = open("Moves.json", "r")

    # Main game
    def game(self):
        self.pstats = self.pokemonStats.read()
        print(self.pstats())