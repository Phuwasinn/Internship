class Student:
    def __init__(self, name, score):
        self.name = name
        self.score = score
    
    def is_passed(self):
        return self.score >=5

s1 = Student("Fluke", 9)
s2 = Student("An", 4.5)
print(s1.is_passed())
print(s2.is_passed())