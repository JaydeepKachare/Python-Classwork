# demo for multiple inheritance in python 

class Base1 :
    def __init__(self,a):
        self.a = a 
    
    def printInfo(self) : 
        print("a : ",a)


class Base2 : 
    def __init__(self,b):
        self.b = b 
    
    def printInfo(self) : 
        print("b : ",self.b)


class Derived (Base1,Base2) :
    def __init__(self, a,b,c):
        Base1.__init__(self,a)
        Base2.__init__(self,b)
        self.c = c 

    def printInfo(self):
        print("a : {}  b : {}  c : {} ".format(self.a,self.b,self.c))

def main() :
    obj = Derived(10,20,30)
    obj.printInfo() 



if __name__ == "__main__" : 
    main() 