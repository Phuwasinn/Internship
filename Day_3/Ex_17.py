class Engine():
    def start(self):
        print("Engine start")
        
    def stop(self):
        print("Engine stop")
        
class Car():
    def __init__(self, brand):
        self.brand = brand
        self.engine = Engine()

car = Car("BMW") 
car.engine.start()
car.engine.stop()   