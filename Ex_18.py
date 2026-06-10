import functools

def identity(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)
    return wrapper

@identity
def original_func(x):
    return x * 2

print(original_func(5))