import os, sys, importlib, traceback, time

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
        input("...")

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
        print("")

        if selected == "0":
            sys.exit()
        if selected == "":
            raise ValueError
            #Just to warn that im looking for a number
        
        selected = int(selected)

        if selected > len(assignmentModules):
            raise ModuleNotFoundError
        else:
            try:
                assignmentModules[selected - 1].main() # Run assignment :3 
                input("Enter to return to menu...")
            except Exception as e:
                # allow seeing the traceback and exception in assignment instead of being dumped out to the menu with no error message, or an error message for the menu
                print("Exception in assignment!")
                print(traceback.print_exc())
                input("Enter to return to menu...")

    except Exception as e:
        print(e, type(e))
        if type(e) == ModuleNotFoundError:
            print("Assignment not found!")
        elif type(e) == ValueError:
            print('Please input number before the assignment name! (Ex with "1. Assignment" input the number 1)')
            time.sleep(5)
