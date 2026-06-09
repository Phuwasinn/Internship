import functools

def Double(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        if isinstance(result, (int, float)):
            return result * 2
        return result
    return wrapper

@Double
def Val():
    return 5

print(Val())