def assignmentName() -> str:
    return "Chapter 5 (Stadium Seating)"

def getInput(inputStr):
    while True:
        try:
            return int(input(inputStr))
        except KeyboardInterrupt:
            exit()
        except:
            print("Input a whole number!")

def calcRevenue(a,b,c):

    a *= 20
    b *= 15
    c *= 10

    print(f"Class A Revenue: {a}")
    print(f"Class B Revenue: {b}")
    print(f"Class C Revenue: {c}")
    print(f"Total Revenue: {a + b + c}")

def main():
    aSeats = getInput("Number of class A seats: ")
    bSeats = getInput("Number of class B seats: ")
    cSeats = getInput("Number of class C seats: ")

    calcRevenue(aSeats, bSeats, cSeats)


if __name__ == "__main__":
    assignmentName() #just to give a warning when I copy paste this to other assignments
    main()