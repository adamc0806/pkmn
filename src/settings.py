# Auth: Adam Carrington.
# Date of Creation: 26/03/2023.
# All code written and documented by above mentioned author.

# Built in modules
import os
import time # delay between text outputs
import json # Needed for json compatibility

# Author written modules


class settings:


    # __init__ used to open settings
    # Find settings file, if none exists, create one
    # NOTE: ONLY default config will be packaged with program.
    def __init__(self):

        if os.path.isfile("settings.json"):
            self.settingsConfig = open("settings.json", "a")
        else: # If file not found
            try:
                with open('defaults.json','r') as defaults, open('settings.json','a') as settings: 
                    # read content from default config
                    for line in defaults:
                            # append content to new config
                            settings.write(line)
            except FileNotFoundError: # Alert user that no config is available, and create one.
                print("You have no defaults file, creating a default configuration...")
                defaults = open("defaults.json", "w")
                defaults.write("""{"SleepTime": 0,\n}""")

                # Create configurable settings file, write data and close.
                setSettings = open("settings.json", "w")
                setSettings.write(defaults)
                defaults.close()
        



    def configSettings(self): # Self explanatory.
         print("""
         ===================
         |CONFIGURATION    |
         |1. TEXT SPEED    |
         |2. --            |
         |3. --            |
         |4. RETURN TO MENU|
         ===================""")


configure = settings() # Create object