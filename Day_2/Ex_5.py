import functools

def argument_logger(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Log: Args: {args}, Kwargs: {kwargs}")
        return func(*args, **kwargs)
    return wrapper

@argument_logger
def Func(a, b, c=None):
    return a + b

Func(1, 2, a=3)