import functools, time

def Rate_limiter(Max_calls, Window_secs):
    calls = []
    def Decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            now = time.time()
            while calls and now - calls[0] > Window_secs:
                calls.pop(0)

            if len(calls) >= Max_calls:
                print("Too many requests")
                return None
            calls.append(now)
            return func(*args, **kwargs)
        return wrapper
    return Decorator

@Rate_limiter(Max_calls = 2, Window_secs = 1)
def API_call():
    print("API called successfully")

for _ in range(10):
    API_call()