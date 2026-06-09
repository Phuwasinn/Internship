import functools, os

def Debug(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        if os.environ.get("DEBUG") == "True":
            print(f" DEBUG Calling '{func.__name__}'| Args: {args}| Kwargs: {kwargs}")
        result = func(*args, **kwargs)

        if os.environ.get("DEBUG") == "True":
            print(f"[DEBUG] Result: {result}")
        return result
    return wrapper

@Debug
def compute(x, y):
    return x + y

os.environ["DEBUG"] = "False"
compute(3, 4)

os.environ["DEBUG"] = "True"
compute(3, 4)