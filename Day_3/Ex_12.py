class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @classmethod
    def from_string(cls, data):
        name, age = data.split("-")
        return cls(name, int(age))
    
    def __str__(self):
        return f"Person(Name = {self.name}, Age = {self.age})"
    
p = Person.from_string("Phuwasin-21")
print(p) 

        
            
            
        