class Vehicle:
    def general(self):
        print("I am the Vehicle")

class Car(Vehicle):
    def __init__(self):
        print("I am the car")
        self.tyre = 4
        self.roofTop = True
    
    def vehicel_type(self):
        print("I am the car with 4 wheels and roof top")

class Bike(Vehicle):
    def __init__(self):
        print("I am the bike")
        self.tyre = 2
        self.roofTop = False
    
    def vehicle_type(self):
        self.general()
        print("I am the bike with 2 tires and no roof")


c = Car()
c.general()
c.vehicel_type()

b = Bike()
b.vehicle_type()


print(isinstance(c, Car))

print(issubclass(Car, Bike))