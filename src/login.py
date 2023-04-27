# Login menu
# Author: Adam Carrington
# Date of creation: 27/04/2023

# Built in modules
import os
import time


# Author created modules
from menu import loggedIn # For obvious reasons.


class login:

    def __init__(self):

        # Create 2 blank strings for username and password.
        self.username = ""
        self.password = ""


    def main():
        print("""|===========|
                 | login menu|
                 |1. create  |
                 |  account  |
                 |2. login   |
                 |===========|
              """)
        opt = input("Enter choice ==>> ").lower() # Ensures lowercase argument.
        if opt == 1 or opt == "create account":
            account.create(account.username, account.password)
        elif opt == 2 or opt == "login":
            account.login(account.username, account.password)
        else:
            print("Invalid value entered. Try again.")
            account.main(account.username, account.password)

    def login():
        print("Login to account")
        account.username = input("Enter username ==>> ")
        account.password = input("Enter password ==>> ")
        with open("HashedDetails.json", "r+") as f:
            details = json.load(f)
            if hashUsername(account.username) == details["username"]:
                if hashPassword(account.password) == details["password"]:
                    print("=== Login Successful! ===")



    # Hashing algorithms are one way and cannot be reverse-engineered. 
    # Prevents data theft.
    def hash():
        account.username
        account.password



account = login() # Create the object
