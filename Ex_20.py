List = []

def register(func):
    List.append(func)
    return func

@register
def func_a():
    pass

@register
def func_b():
    pass

@register
def func_c():
    pass

print("Functions:")
for f in List:
    print(f"  - {f.__name__}")