import functools, json

def JSON(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return json.dumps(result)  
    return wrapper

@JSON
def get_user():
    return {"name": "Fluke", "age": 21}

print(get_user())