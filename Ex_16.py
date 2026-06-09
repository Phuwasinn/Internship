def append_docstring(info):
    def Decorator(func):
        func.__doc__ = (func.__doc__ or "") + f"\n{info}"
        return func
    return Decorator

@append_docstring("Added by decorator: Do not modify manually.")
def my_func():
    """Original docstring."""
    pass

help(my_func)