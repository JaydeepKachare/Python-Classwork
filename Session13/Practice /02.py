from decorator import do_twice 

@do_twice
def say_wheee() : 
    print("whee !")


@do_twice
def greet(name) : 
    print(f"Hello , {name}")
# greet = do_twice(greet)


@do_twice
def return_greeting(name) : 
    print("creating greeting")
    return f"Hi, {name}"
# return_greeting = do_twice(return_greeting)




# hi_adam = return_greeting("Adam")
# print(hi_adam)

# # greet("JD")
# # say_wheee() 
print(say_wheee)
print(say_wheee.__name__)
say_wheee() 