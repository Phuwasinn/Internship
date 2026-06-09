import functools

def Deprecated(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Warning: Function '{func.__name__}' is deprecated")
        return func(*args, **kwargs)
    return wrapper

@Deprecated
def Old():
    print("Doing old stuff...")

Old()