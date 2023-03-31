# Auth: Adam Carrington.
# Date of Creation: 26/03/2023.
# All code written and documented by above mentioned author.

# Built in modules
import os
import time # delay between text outputs
import json # Needed for json compatibility

# Author written modules


class settings:

    # Declare attributes
    # Each attribute is a seperate setting
    def __init__(self):
        # Find settings file, if none exists, create one
        # NOTE: ONLY default config will be packaged with program.

        # TODO: For some reason the if is never evaluated as true, fix it. 
        if os.path.isfile("settings.json"):
            self.settingsConfig = open("settings.json", "a")
        else: # If file not found
            try:
                with open('defaults.json','r') as defaults, open('settings.json','a') as settings: # Python can't find defaults.json anymore
                    # read content from default config
                    for line in defaults:
                            # append content to new config
                            settings.write(line)
            except FileNotFoundError:
                defaults = open("settings.json", "w")
                defaults.write("""{"SleepTime": 0,\n}""")
        
        self.parameter = True # Weird testing thing



    def configSettings(self):
         print("""==========
         CONFIGURATION""")


    def testconfig(self):
        if self.parameter == True:
            configure.configSettings()
        else:
            quit()

configure = settings()
configure.testconfig()