class Vehicle:
    def drive(self):
        print("Vehicle is moving")

class Car(Vehicle):
    def __init__(self, brand):
        self.brand = brand
 
car = Car("BMW")
car.drive() 