import functools

def C_to_F(func):
    @functools.wraps(func)
    def wrapper(C, *args, **kwargs):
        F = C * 9/5 + 32
        print(f"Converted {C}°C to {F}°F ")
        return func(F, *args, **kwargs)
    return wrapper

@C_to_F
def Temperature(temp):
    print(f"Processing temperature: {temp}°F")

Temperature(30)
