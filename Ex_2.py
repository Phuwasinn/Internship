import functools

def retry(n):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            for attempt in range(1, n + 1):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    print(f"Attempt {attempt} failed: {e}")

            print("I'm tired")
        return wrapper
    return decorator

@retry(n=3)
def unstable_connection():
    raise ConnectionError("Connection failed")

unstable_connection()