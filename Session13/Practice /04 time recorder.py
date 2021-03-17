import time 
import functools

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


@timer
def waste_some_time(num_times) : 
    for i in range (num_times) : 
        num = 0

waste_some_time(1000000) 