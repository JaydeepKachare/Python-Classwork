
def my_decorator(func) : 
    def wrapper() :
        print("Before func call ... ")
        func() 
        print("After func call ... ")
    return wrapper 

@my_decorator       # say_whee = my_decorator(say_whee)
def say_whee() : 
    print("Wheee..............")


say_whee() 