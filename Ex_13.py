import functools

def Exception_Wrapper(default = 0):
    def Decorator(func):
        @functools.wraps(func)
        def wrapper (*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except Exception as e:
                print(f"Error: {e}")
                return default
        return wrapper
    return Decorator

@Exception_Wrapper(default=None)
def divide(a, b):
    return a / b

print(divide(10, 0))