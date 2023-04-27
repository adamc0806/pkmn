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

        self.playerDeathCount = 0
        self.oppPokemonDeathCount = 0

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
           game.playerTurn(pokemon, oppPokemon, self)
        elif pokemon[3] < oppPokemon[3]:
            game.oppTurn(pokemon, oppPokemon, self)
        else: # If both speeds are equal, this is very unlikely but could potentially happen
            self.playerTurn(pokemon, oppPokemon, self)

    def playerTurn(pokemon, oppPokemon, self):
        turnCount = 0
        print("=== Your turn ===")
        print("""================
                 |Choose a move:|
                 | 1. Attack    |
                 | 2. Defend    |
                 | 3. Heal      |
                 ================""")
        move = input("==>> ").lower()
        if move == "defend" or move == 1:
            attack = pokemon[1] * pokemon[1] / pokemon[2]
            oppPokemon[4] -= attack
            print("=== You did ", attack, " damage! ===")
            print("=== Your stats: ", pokemon, "Opponent's stats: ", oppPokemon, " ===")
        elif move == "defend" or move == 2:
            if turnCount == 0:
                turnCount += 1
                print("=== You can't defend on the first turn! ===")
                game.oppTurn(pokemon, oppPokemon, self)
            else:
                pass
        elif move == "heal" or move == 3:
            health = oppPokemon[1] - (pokemon[2] / pokemon[2]) # Heal by opponent's attack minus half your health
            pokemon[4] += health
            print("=== You healed for ", health, " health! ===")
        if pokemon[4] <= 0:
            print("=== Your pokemon fainted... ===")
            playerDeathCount += 1
            game.generateTeam()
        elif oppPokemon[4] <= 0:
            print("=== The opponent's pokemon fainted! ===")
            oppPokemonDeathCount += 1
        game.oppTurn(pokemon, oppPokemon, self)


    def oppTurn(pokemon, oppPokemon, self):
        turnCount = 0
        print("=== Opponent's turn! ===")
        move = random.randint(0, 3)
        if move == 1:
            attack = pokemon[1] * pokemon[1] / pokemon[2]
            pokemon[4] -= attack
            print("=== The computer did ", attack, " damage! ===")
            print("=== Your stats: ", pokemon, "Opponent's stats: ", oppPokemon, " ===")
        elif move == 2:
            if turnCount == 0:
                turnCount += 1
                game.playerTurn(pokemon, oppPokemon, self)
            else:
                pass
        elif move == 3:
            health = pokemon[1] - (oppPokemon[2] / oppPokemon[2]) # Heal by opponent's attack minus half your health
            oppPokemon[4] += health
            print("=== The opponent healed for ", health, " health! ===")
            game.playerTurn(pokemon, oppPokemon)
        if oppPokemon[4] <= 0:
            print("=== The opponent's pokemon fainted! ===")
            self.oppPokemonDeathCount += 1
            game.generateTeam()
        elif pokemon[4] <= 0:
            print("=== Your pokemon fainted... ===")
            self.playerDeathCount += 1
            game.generateTeam()
            if self.oppPokemonDeathCount == 6:
                print("=== The computer loses! ===")
                return 0
            elif self.playerDeathCount == 6:
                print("=== You lose! ===")
                return 0
            else:
                game.playerTurn(pokemon, oppPokemon)
Game = game()
