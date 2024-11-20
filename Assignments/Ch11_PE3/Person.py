class Person:

    name = ""
    address = ""
    age = 0
    phone = 1234567890

    def __init__(self, name, address, age, phone) -> None:
        
        self.name = name
        self.address = address
        self.age = age
        self.phone = phone

    # Setters

    def setName(self, name):
        self.name = name

    def setAddress(self, address):
        self.address = address

    def setAge(self, age):
        self.age = age

    def setPhone(self, phone):
        self.phone = phone

    # Getters

    def getName(self):
        return self.name
    
    def getAddress(self):
        return self.address
    
    def getAge(self):
        return self.age
    
    def getPhone(self):
        return self.phone
    
    def print(self):
        print("Name:", self.name)
        print("Address:", self.address)
        print("Age:", self.age)
        print("Phone Number:", self.phone)