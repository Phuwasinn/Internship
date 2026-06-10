import functools

def deprecated(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Warning: Function '{func.__name__}' is deprecated")
        return func(*args, **kwargs)
    return wrapper

@deprecated
def old():
    print("Doing old stuff...")

old()