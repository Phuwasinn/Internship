import functools

def make_adder(fixed):
    def adder(x):
        return fixed + x  
    return adder

add_five = make_adder(5)
print(add_five(10))