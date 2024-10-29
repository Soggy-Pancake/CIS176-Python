"""
Create a program with a dictionary that stores the first_name, last_name, and age of a person. 
You will pre-populate the dictionary with the following key/value pairs.

first_name = 'Your first name'

last_name = 'Your last name'

age = 30

Next, create a menu (using print statements) that allows changing one of the three values (first_name, last_name, age). 
Determine, using an IF statement which of the three values the user chose to change, prompt the user for the new value, and update the dictionary.

"""

import os

def printDict(Dict : dict):
    dictKeys = Dict.keys()
    for key in dictKeys:
        print(f"{key}: {Dict[key]}")

def askInt(question : str):
    while True:
        try:
            return int(input(question))
        except ValueError:
            print("Enter a number!")
        except:
            exit()

def assignmentName() -> str:
    return "Chapter 9 (Person Dictionary)"

def main():

    os.system("cls")
    personDict = {
        "firstName" : "Your first name",
        "lastName" : "Your last name",
        "age" : 30
    }

    while True:
        printDict(personDict)
        print("")

        print("1. Change first name")
        print("2. Change last name")
        print("3. Change age")
        print("0. exit")

        choice = askInt(": ")

        if choice == 1:
            personDict["firstName"] = input("New first name: ")
            os.system("cls")
            print("Name changed!")
            print("")
            continue

        if choice == 2:
            personDict["lastName"] = input("New last name: ")
            os.system("cls")
            print("Name changed!")
            print("") 
            continue
        
        if choice == 3:
            personDict["age"] = askInt("New age: ")
            os.system("cls")
            print("Age changed!")
            print("") 
            continue

        if choice == 0 or choice == None:
            break

        print("Invalid option!")



if __name__ == "__main__":
    assignmentName() #just to give a warning when I copy paste this to other assignments
    main()