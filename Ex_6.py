import functools

def Authorize(func):
    @functools.wraps(func)
    def wrapper(user, *args, **kwargs):
        if user.get("role") != "admin":
            print("Permision Denied")
            return None
        return func(user, *args, **kwargs)
    return wrapper

@Authorize
def Delete_Database(user):
    print("Database deleted!")

Delete_Database({"role": "guest"})
Delete_Database({"role": "admin"})