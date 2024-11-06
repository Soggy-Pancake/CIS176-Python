
class Car:

    year = 0
    speed = 0
    model = ''
    make = ''
    

    def __init__(self, make : str, model : str, year : int):

        self.make = make
        self.model = model
        self.year = year
        self.speed = 0 # It defaults to zero anyway but sure ill do it in init too

        print("Car created!")

    def accelerate(self):
        self.speed += 5

    def brake(self):
        self.speed -= 5

    def crash(self): # just because
        self.speed = 0 

    def getSpeed(self):
        return self.speed