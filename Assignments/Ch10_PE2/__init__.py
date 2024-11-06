"""
Car Class

Write a class named Car that has the following data attributes:

year (the year the car was made)
model (for the model of the car)
make (for the make of the car)
speed (for the car's current speed)


The Car class should have an _ _ init _ _ method that accepts the car's year, model and make data attributes. It should also assign 0 to the speed data attribute.



The class should also have the following methods:

accelerate (The accelerate method should add 5 to the speed data attribute each time it is called.)
brake (The brake method should subtract 5 from the speed data attribute each time it is called.)
get_speed (The get_speed method should return the current speed.)


Next, design a program (in the main) that creates a Car object.

Then, call the accelerate method 5 times, displaying the speed each time you accelerate. Then call the brake method five times and get the current speed of the car and display it.
"""

# Running from menu gave relative import issues and since I cant use relative import when 
# running on its own I gotta use this as failover
try:
    from Car import Car
except:
    from .Car import Car


def assignmentName() -> str:
    return "Chapter 10 (Car class)"

def main():

    car = Car("NotEven", "Used", 1998)

    for i in range(5):
        car.accelerate()
        print("Accelerated! New speed:", car.getSpeed())
        
    for i in range(5):
        car.brake()

    print("Final speed:", car.getSpeed())

if __name__ == "__main__":
    assignmentName() #just to give a warning when I copy paste this to other assignments
    main()