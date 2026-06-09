import functools

def Types_Validate(*expected_type):
    def Decorator(func):
        @functools.wraps(func)  
        def wrapper(*args, **kwargs):
            for i, (arg, expected) in enumerate(zip(args, expected_type)):
                if not isinstance(arg, expected):
                    raise TypeError(
                        f"Argument {i+1}: expected {expected.__name__}, "
                        f"got {type(arg).__name__}"
                    )
            return func(*args, **kwargs)
        return wrapper
    return Decorator

@Types_Validate(int, int)
def add(a, b):
    return a + b

try:
    add("hello", 2)
except TypeError as e:
    print("TypeError:", e)