import functools
import time

def timer(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"Time: {end - start:.2f}s")
        return result
    return wrapper

def logger(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Log: Args: {args}, Kwargs: {kwargs}")
        return func(*args, **kwargs)
    return wrapper

@timer
@logger
def chained(x,y):
    time.sleep(0.5)
    return x + y
print("Result:", chained(3, 4))