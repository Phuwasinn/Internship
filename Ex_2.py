import functools

def Retry(n):
    def Decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            for attempt in range(1, n + 1):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    print(f"Attempt {attempt} failed: {e}")

            print("I'm tired")
        return wrapper
    return Decorator

@Retry(n=3)
def Unstable_connection():
    raise ConnectionError("Connection failed")

Unstable_connection()