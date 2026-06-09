import functools

def Argument_Logger(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Log: Args: {args}, Kwargs: {kwargs}")
        return func(*args, **kwargs)
    return wrapper

@Argument_Logger
def Func(a, b, c=None):
    return a + b

Func(1, 2, a=3)