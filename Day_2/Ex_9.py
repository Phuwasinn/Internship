import functools

def singleton(cls):
    instances = {}  
    @functools.wraps(cls)
    def get_instance(*args, **kwargs):
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs) 
        return instances[cls]
    return get_instance

@singleton
class DatabaseConnection:
    pass

db1 = DatabaseConnection()
db2 = DatabaseConnection()
print("id db1:", id(db1))
print("id db2:", id(db2))
print("Same instance?", db1 is db2)