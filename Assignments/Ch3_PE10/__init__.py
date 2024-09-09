"""
Create a change-counting game that gets the user to enter the number of coins required to
make exactly one dollar. The program should prompt the user to enter the number of
pennies, nickels, dimes, and quarters. If the total value of the coins entered is equal to one
dollar, the program should congratulate the user for winning the game. Otherwise, the
program should display a message indicating whether the amount entered was more than or
less than one dollar.
"""

def assignmentName() -> str:
    return "Chapter 3: Money Counting Game"

def intInput(askString) -> int:
    number = 0
    while True:
        try:
            number = int(input(askString))
            return number
        
        except ValueError:
            print("Enter a whole number!")

        except KeyboardInterrupt:
            # Prevent not closing with ctrl C
            exit()
    

def main():
    print("The goal of this game is to make exactly 1 dollar with coins.")

    total = 0 #total will be in pennies to avoid floating point precision error

    pennies = intInput("Number of pennies: ")
    nickels = intInput("Number of nickels: ") * 5
    dimes = intInput("Number of dimes: ") * 10
    quarters = intInput("Number of quarters: ") * 25

    # Could += to total instead of seperate variables
    total = pennies + nickels + dimes + quarters

    if total == 100:
        print("You win! Your total was exactly 1 dollar")
    if total > 100:
        print(f"Over 1 dollar! You entered ${total/100}")
    if total < 100:
        print(f"Under 1 dollar! You entered ${total/100}")

if __name__ == "__main__":
    assignmentName() #just to give a warning when I copy paste this to other assignments
    main()