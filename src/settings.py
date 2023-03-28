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
        if os.path.isfile("Settings.json"):
            self.settingsConfig = open("Settings.json", "a")
        else: # If file not found
            with open('defaults.json','r') as defaults, open('settings.json','a') as settings:
                # read content from default config
                for line in defaults:
                        # append content to new config
                        settings.write(line)
        
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