class User:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def to_dict(self):
        return {
            "name": self.name,
            "age": self.age
        }

user = User("Fluke", "21")
print(user.to_dict())    