import os, sys, importlib

print("Importing assignments!")

assignmentModules = []
try:
    sys.path.insert(0, os.path.join(__file__[:__file__.rfind("\\")], "Assignments") )
except:
    print("Failed to add assignments folder to path! Exiting...")
    sys.exit()

for assignment in os.listdir("Assignments"):
    #print(f"Assignment {assignment}")
    #from Assignments import Ch1Ex1
    try:
        assignmentModules.append(importlib.import_module(assignment))
    except Exception as e:
        print(f"Import FAIL for assignment {assignment} : {e}")

def printMenu() -> None:
    for i in range(len(assignmentModules)):
        print(f"{i + 1}. {assignmentModules[i].fullAssignmentName()}")


#print(assignmentModules)


while True:
    os.system("cls")
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
