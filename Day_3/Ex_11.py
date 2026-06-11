class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @staticmethod
    def is_adult(age):
        return age >=20

print(Person.is_adult(20)) 
print(Person.is_adult(15)) 