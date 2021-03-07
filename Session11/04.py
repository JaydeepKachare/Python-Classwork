# Inheritance in Python

class Base :
    def __init__(self):
        self.i = 10 
        self.j = 20 
        print("Inside Base Constructor")
    
    def fun(self) : 
        print("Inside Base fun")
    
    def gun(self) : 
        print("Inside Base gun")
    
    
class Derived (Base) : 
    def __init__(self):
        # super().__init__()
        Base.__init__(self)
        print("Inside Derived Constructor")
        self.x = 30 
        self.y = 40 
    
    def sun(self) : 
        print("Inside Derived sun")

    def gun(self) : 
        print("Inside Derived gun")
    
    

class Derived2 (Derived) : 
    def __init__(self):
        Derived.__init__(self) 
        self.a = 50 
        self.b = 60 
        print("Inside Derived2 Constructor")


def main() :
    
    d2obj = Derived2()
    print(d2obj.i)
    print(d2obj.j)
    print(d2obj.x)
    print(d2obj.y)
    print(d2obj.a)
    print(d2obj.b)


if __name__ == "__main__" : 
    main() 
