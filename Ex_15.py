import functools
import time

def Timer(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"Time: {end - start:.2f}s")
        return result
    return wrapper

def Logger(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Log: Args: {args}, Kwargs: {kwargs}")
        return func(*args, **kwargs)
    return wrapper

@Timer
@Logger
def Chained(x,y):
    time.sleep(0.5)
    return x + y
print("Result:", Chained(3, 4))