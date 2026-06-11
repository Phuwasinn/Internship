class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @property
    def age(self):
        return self.__age
    
    @age.setter
    def age(self, value):
        if value < 0:
            raise ValueError("Age can't be negative")
        self.__age = value

p = Person("Fluke", 21)
print(p.age) 

try:
    p.age = -5
except ValueError as e:
    print("ValueError:", e)