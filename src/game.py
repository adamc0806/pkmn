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
        self.turnCount = 0
        
    # Generate random team
    def generateTeam():
        
        pokemonNames = open("pokemonNames.txt", "r").read().splitlines()
        pokemon = []
        pokemon.append(random.choice(pokemonNames).strip())
        
        for i in range(0, 4):
            pokemon.append(random.randint(15, 100))

        oppPokemon = []
        oppPokemon.append(random.choice(pokemonNames).strip())

        for i in range(0, 4):
            oppPokemon.append(random.randint(15, 100))
        
        # When teams generated
        game.startPlay(pokemon, oppPokemon)
        
        # 1 = attack
        # 2 = defense
        # 3 = speed
        # 4 = Health
        # Array position is for me to easily remember which is which
        
        
    def startPlay(pokemon, oppPokemon):
        
        print("=== PLAYING GAME ===")
        if pokemon[3] > oppPokemon[3]:
           game. playerTurn(pokemon, oppPokemon)
        elif pokemon[3] < oppPokemon[3]:
            game.oppTurn(pokemon, oppPokemon)
        else: # If both speeds are equal, this is very unlikely but could potentially happen
            self.playerTurn(pokemon, oppPokemon)

    def playerTurn(pokemon, oppPokemon):
        turnCount = 0
        print("=== Your turn ===")
        print("""\t================
                 \t|Choose a move:|
                 \t| 1. Attack    |
                 \t| 2. Defend    |
                 \t| 3. Heal      |
                 \t================""")
        move = input("==>> ").lower()
        if move == "defend" or move == 1:
            attack = (pokemon[1] * pokemon[1]) / pokemon[2]
            oppPokemon[4] -= attack
            print("=== You did ", attack, " damage! ===")
            print("=== Your stats: ", pokemon, "Opponent's stats: ", oppPokemon, " ===")
        elif move == "defend" or move == 2:
            if turnCount == 0:
                turnCount += 1
                print("=== You can't defend on the first turn! ===")
                game.oppTurn(pokemon, oppPokemon)
            else:
                pass
        elif move == "heal" or move == 3:
            health = (oppPokemon[1] - (pokemon[2]) / pokemon[2]) # Heal by opponent's attack minus half your health
            pokemon[4] += health
            print("=== You healed for ", health, " health! ===")
        if pokemon[4] == 0:
            print("=== Your pokemon fainted... ===")
            game.generateTeam()
        game.oppTurn(pokemon, oppPokemon)


    def oppTurn(pokemon, oppPokemon):
        turnCount = 0
        print("=== Opponent's turn! ===")
        move = random.randint(0, 3)
        if move == 1:
            attack = (pokemon[1] * pokemon[1]) / pokemon[2]
            pokemon[4] -= attack
            print("=== The computer did ", attack, " damage! ===")
            print("\n=== Your stats: ", pokemon, "Opponent's stats: ", oppPokemon, " ===")
        elif move == 2:
            if turnCount == 0:
                turnCount += 1
                game.playerTurn(pokemon, oppPokemon)
            else:
                pass
        elif move == 3:
            health = (pokemon[1] - oppPokemon[2]) / oppPokemon[2] # Heal by opponent's attack minus half your health
            oppPokemon[4] += health
            print("\n=== The opponent healed for ", health, " health! ===")
            game.playerTurn(pokemon, oppPokemon)
        if oppPokemon[4] == 0:
            print("\n=== The opponent's pokemon fainted... ===")
            if oppPokemonDeathCount == 6:
                print("\n=== The computer loses! ===")
                game.generateTeam()
            elif playerDeathCount == 6:
                print("\n=== You lose! ===")
            else:
                game.playerTurn(pokemon, oppPokemon)
Game = game()
