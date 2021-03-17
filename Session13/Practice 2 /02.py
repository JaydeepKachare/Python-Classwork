import functools




def repeat(num_times) :
    def decorator_repeat(func) : 
        def wrapper(*args, **kwargs) : 
            for i in range(0,num_times) : 
                value = func(*args,**kwargs)
            return value 
        return wrapper 
    return decorator_repeat 


@repeat(num_times = 4 )
def greet(name) : 
    print(f"Hello , {name}")



greet("Adam")