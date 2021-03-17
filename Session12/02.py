
class Base : 
    def __init__(self): 
        self.a = 10 
    
    def fun(self) : 
        print("Inside Base.fun")


class Derived (Base) : 
    def __init__(self):
        Base.__init__(self) 
        self.b = 20 

    def gun(self) : 
        print("Inside Derived.gun")
        # Base.fun(self)
        # self.fun() 
        # super().fun()
        print(self.a)
        print(self.b)


def main() :
    dobj = Derived() 
    dobj.gun() 


if __name__ == "__main__" : 
    main() 
