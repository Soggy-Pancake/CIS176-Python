try:
    from Person import Person
except:
    from .Person import Person

import random

class Customer(Person):

    customerID = 0
    mailing = True

    def __init__(self, name, address, age, phone) -> None:
        Person.__init__(self, name, address, age, phone)
        self.customerID = random.randint(0,10000)
        
    # Setters

    def setCustomerID(self, newID):
        self.customerID = newID

    def putOnMailingList(self, mail):
        self.mailing = mail

    # Getters
    def getCustomerID(self):
        return self.customerID

    def onMailingList(self):
        return self.mailing
    
    def print(self):
        Person.print(self)
        print("Customer ID: ", self.customerID)
        print("On mailing list?: ", self.mailing)