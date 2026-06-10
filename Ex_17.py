import functools

def c_to_f(func):
    @functools.wraps(func)
    def wrapper(C, *args, **kwargs):
        F = C * 9/5 + 32
        print(f"Converted {C}°C to {F}°F ")
        return func(F, *args, **kwargs)
    return wrapper

@c_to_f
def temperature(temp):
    print(f"Processing temperature: {temp}°F")

temperature(30)
