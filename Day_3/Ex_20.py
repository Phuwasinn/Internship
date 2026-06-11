class User:
    count = 0
    
    def __init__(self, name):
        self.name = name
        User.count += 1

u1 = User("Fluke")
u2 = User("Anh Quan")
u3 = User("Anh Quang")

print(User.count)