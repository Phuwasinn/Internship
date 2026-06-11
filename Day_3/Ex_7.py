class Vehicle:
    def __init__(self, brand):
        self.brand = brand
        print(f"Vehicle created: brand = {self.brand}")

class Car(Vehicle):
    def __init__(self, brand, model):
        super().__init__(brand)  
        self.model = model      
        print(f"Car created: model = {self.model}")

car = Car("Toyota", "Camry")
print(car.brand)  
print(car.model)  