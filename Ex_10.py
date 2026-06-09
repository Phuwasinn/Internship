import functools, time

def Delay(secs):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            print(f"Waiting {secs} s")
            time.sleep(secs)

            return func(*args, **kwargs)
        return wrapper
    return decorator

@Delay(secs = 5)
def Hello():
    print("Hello!")

Hello()