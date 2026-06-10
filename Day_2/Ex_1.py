import time, functools

def timer(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()

        print(f"Time: {end - start:.2f} s ")
        return result
    return wrapper

@timer
def slow_function():
    time.sleep(1)

slow_function()