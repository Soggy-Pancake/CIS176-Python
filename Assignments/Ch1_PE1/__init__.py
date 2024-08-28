#print("Loading Chapter 1 Exersize 1!")

def assignmentName() -> str:
    return "Chapter 1 Exercise 1"

def main():
    print("Hello, Mike!")
    print("Hello", "Mike!")
    print(5)
    print(5.0)
    print(2 + 5)
    print(2.0 + 5.0)
    print("2" + "5")
    print("2 + 5 = ", 2 + 5)
    print(2 * 5)
    print(5 ** 3)
    print(11 / 3)
    print(11 // 3)
    # input used to keep print statements on screen 
    input("Finished Running...")

if __name__ == "__main__":
    assignmentName() #just to give a warning when I copy paste this to other assignments
    main()