# init and destroy method in Pythob OOP 

class Demo : 
    x=10        # class variable
    y=20        # class variable 
    
    def __init__(self):
        print("Inside __init__ (constructor)")
        self.i = 30         # instance variable
        self.j = 40         # instance variable 
    
    def __del__ (self) : 
        print("Inside destructor ")
    
    def fun(self) : 
        print("Inside fun")


def main() :
    obj1 = Demo() 
    obj2 = Demo() 

    obj1.fun()          # fun(obj1)

    del obj1 
    del obj2 


if __name__ == "__main__" : 
    main() 


