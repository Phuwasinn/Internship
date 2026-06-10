def append_docstring(info):
    def decorator(func):
        func.__doc__ = (func.__doc__ or "") + f"\n{info}"
        return func
    return decorator

@append_docstring("Added by decorator: Do not modify manually.")
def my_func():
    """Original docstring."""
    pass

help(my_func)