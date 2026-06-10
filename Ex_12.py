import functools

def double(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        if isinstance(result, (int, float)):
            return result * 2
        return result
    return wrapper

@double
def val():
    return 5

print(val())