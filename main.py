import os, sys, importlib, traceback

print("Importing assignments!")

assignmentModules = []
try:
    sys.path.insert(0, os.path.join(__file__[:__file__.rfind("\\")], "Assignments") )
except:
    print("Failed to add assignments folder to path! Exiting...")
    sys.exit()

for assignment in os.listdir("Assignments"):
    #leftover from testing if making each assignment a class worked (Made things overcomplicated for no reason)
    if not os.path.isdir(os.path.join("Assignments",assignment)) or assignment.startswith("__"):
        continue
    try:
        assignmentModules.append(importlib.import_module(assignment))
    except Exception as e:
        print(f"Import FAIL for assignment {assignment} {type(e)} : {e}")
        traceback.print_exc()

def printMenu() -> None:
    os.system("cls")
    for i in range(len(assignmentModules)):
        print(f"{i + 1}. {assignmentModules[i].assignmentName()}")


#print(assignmentModules)

while True:
    printMenu()
    print("0. Exit")
    try:
        selected = input("Input Assignment: ")

        if selected == "0":
            sys.exit()
        if selected == "":
            raise ValueError
            #Just to warn that im looking for a number
        
        selected = int(selected)

        if selected > len(assignmentModules):
            raise ModuleNotFoundError
        else:
            # Run assignment :3 
            assignmentModules[selected - 1].main()

    except Exception as e:
        print(e, type(e))
        if type(e) == ModuleNotFoundError:
            print("Assignment not found!")
        elif type(e) == ValueError:
            print('Please input number before the assignment name! (Ex with "1. Assignment" input the number 1)')
