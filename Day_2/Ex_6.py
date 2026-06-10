import functools

def authorize(func):
    @functools.wraps(func)
    def wrapper(user, *args, **kwargs):
        if user.get("role") != "admin":
            print("Permision Denied")
            return None
        return func(user, *args, **kwargs)
    return wrapper

@authorize
def delete_database(user):
    print("Database deleted!")

delete_database({"role": "guest"})
delete_database({"role": "admin"})