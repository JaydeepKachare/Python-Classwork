import functools
import time

def debug (func) : 
    """This is function which print signature and return value """
    @functools.wraps(func) 
    def wrapper_debug(*args, **kwargs) : 
        print(f"calling '{func.__name__}'")
        value = func(*args , **kwargs) 
        print(f"value returned from '{func.__name__}' is '{value}'")

        return value 
    return wrapper_debug 



def timer (func) : 
    """ Print runtime of edcorated functiojn """ 
    @functools.wraps(func) 
    def wrapper_timer(*args, **kwargs) : 
        start_time = time.perf_counter() 
        value = func(*args, **kwargs) 
        end_time = time.perf_counter() 
        run_time = end_time - start_time 
        print(f"Finished {func.__name__} in {run_time} seconds")
        return value 
    return wrapper_timer

