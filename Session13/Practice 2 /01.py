
def do_twice(func) : 
    def wrapper(*args , **kwargs) : 
        func(*args , **kwargs)
        func(*args , **kwargs) 
    return wrapper 


def debug(func) : 
    def wrapper(*args, **kwargs) : 
        print(f"Before function call {func.__name__}")
        value = func(*args, **kwargs) 
        print(f"value return from {func.__name__} is {value} ") 
        return value 
    return wrapper 


@debug
@do_twice
def greet_name(name) : 
    print(f"Hello , {name}")


greet_name("Adam")