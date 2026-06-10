import functools

def exception_wrapper(default = 0):
    def decorator(func):
        @functools.wraps(func)
        def wrapper (*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except Exception as e:
                print(f"Error: {e}")
                return default
        return wrapper
    return decorator

@exception_wrapper(default=None)
def divide(a, b):
    return a / b

print(divide(10, 0))