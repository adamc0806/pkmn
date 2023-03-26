# Auth: Adam Carrington.
# Date of Creation: 26/03/2023.
# All code written and documented by above mentioned author.

class game:


    def __init__(self):
        # open stats and moves jsons as attributes
        self.pokemonStats = open("Stats.json", "r")
        self.pokemonMoves = open("Moves.json", "r")


    def game(self):
        self.pstats = self.pokemonStats.read()
        print(self.pstats())