
import functools

def decorator(func) : 
    @functools.wraps(func) 
    def wrapper_decorator() : 
        # do something before 
        value = func(*args, **kwargs) 
        # do something after 
        return value
    return wrapper_decorator

# Boilerplate template for creating decorator 
