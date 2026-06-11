class Animal:
    def speak(self):
        print("...")

class Dog(Animal):
    def speak(self):          
        print("Woof")

class Cat(Animal):
    def speak(self):           
        print("Meow")

dog = Dog()
cat = Cat()
dog.speak()  
cat.speak()  