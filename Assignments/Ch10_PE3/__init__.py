
try:
    from Person import Person
except:
    from .Person import Person

def assignmentName() -> str:
    return "Chapter 10 (Personal Information Class)"

def main():

    myself = Person("Hello", "123 NotReal Street", 18, 1234587387)
    person1 = Person("Friend1", "47 Brain street", 19, 100000000)
    you = Person("", "", 0, 0)

    # it said with propmts so ig im filling in the info from console
    you.name = input("Your name: ")
    you.address = input("Your address: ")
    you.age = input("Your age: ")
    you.phone = input("Your phone number: ")  # this will put in a string instead but nothing will happen if the type is changed so im leaving it

    print("")
    myself.print()
    print("")
    person1.print()
    print("")
    you.print()
    print("")
    print("Done!")


if __name__ == "__main__":
    assignmentName() #just to give a warning when I copy paste this to other assignments
    main()