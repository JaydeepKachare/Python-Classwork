# Access specifiers in python Inheritance 

class Base : 
    def __init__(self):
        self.num1 = 10          # public member 
        self._num2 = 20         # protected member 
        self.__num3 = 30        # private members 


    def fun(self) :                     # public method                  
        print("Inside Base.fun")

    def _gun(self) :                    # protected method 
        print("Inside Base._gun")

    def __sun(self) :                   # private method 
        print("Inside Base.__sun")

class Derived (Base) : 
    def __init__(self):
        Base.__init__(self)
        self.num4 = 40          # public member 
        self._num5 = 50         # protected member 
        self.__num6 = 60        # private members 


    def Dfun(self) :                     # public method                  
        self.fun() 
        self.__sun()
        print("Inside Derived.fun")

    def _Dgun(self) :                    # protected method 
        self._gun()
        print("Inside Derived._gun")

    def __Dsun(self) :                   # private method 
        print("Inside Derived.__sun")




def main() :

    d = Derived() 
    d.fun() 
    d._gun() 
    # d.__sun()         # cannot access private method 
    d.Dfun() 
    d._Dgun() 
    # d.__Dsun()        #cannot access private method 

    

if __name__ == "__main__" : 
    main() 