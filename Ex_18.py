import functools

def Identity(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)
    return wrapper

@Identity
def Original_Func(x):
    return x * 2

print(Original_Func(5))