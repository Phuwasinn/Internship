import functools, time

def delay(secs):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            print(f"Waiting {secs} s")
            time.sleep(secs)

            return func(*args, **kwargs)
        return wrapper
    return decorator

@delay(secs = 5)
def hello():
    print("Hello!")

hello()