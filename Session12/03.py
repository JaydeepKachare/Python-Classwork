
class Base : 

    def __init__(self): 
        self.a = 10 
    
    def fun(self) : 
        print("Inside Base.fun")


class Derived (Base) : 
    def __init__(self):
        Base.__init__(self) 
        self.a = 20 

    def gun(self) : 
        print("Inside Derived.gun")
        print(self.a)
        
    def fun(self) : 
        print("Inside Derived.fun")
        super().fun()

def main() :
    dobj = Derived() 
    dobj.gun() 
    dobj.fun() 


if __name__ == "__main__" : 
    main() 
