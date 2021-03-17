import functools


def debug (func) : 
    """This is function which print signature and return value """
    @functools.wraps(func) 
    def wrapper_debug(*args, **kwargs) : 
        print(f"calling '{func.__name__}'")
        value = func(*args , **kwargs) 
        print(f"value returned from '{func.__name__}' is '{value}'")

        return value 
    return wrapper_debug 



@debug
def greeting( name , age=None) : 
    if age is None : 
        return  f"Hello , {name} "
    else : 
        return f"{name} , Wow you are {age} years old !!!!"

# greeting = debug(greeting)


result = greeting("Three eyed raven", 1005)
print(result)