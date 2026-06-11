class Multiplier():
    def __init__(self, factor):
        self.factor = factor
        
    def __call__(self, x):
        return x * self.factor

double = Multiplier(2)
triple = Multiplier(3)

print (double(9))
print (triple(9))