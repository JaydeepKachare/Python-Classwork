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
    
   


def main() :
    
    # bobj = Base()
    # print(bobj.i)
    # print(bobj.j)
    # bobj.fun() 
    # bobj.gun() 
    
    dobj = Derived()
    print(dobj.i)
    print(dobj.j)
    print(dobj.x)
    print(dobj.y)
    dobj.sun() 
    dobj.gun() 
    del dobj 


if __name__ == "__main__" : 
    main() 
