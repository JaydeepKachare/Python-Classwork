# Demo for Access Specifier in pyhton 


class Base : 
    def __init__(self):
        self.no1 = 11       # public member 
        self._no2 = 21      # protedted member
        self.__no3 = 51     # private member

    def fun(self) :         # public method  
        print(self.no1,self._no2,self.__no3)

    def _fun(self) :         # protected method  
        print(self.no1,self._no2,self.__no3)

    def __fun(self) :         # private method  
        print(self.no1,self._no2,self.__no3)


class Derived (Base) : 
    def __init__(self):
        Base.__init__(self)

    def gun(self) : 
        print(self.no1)         # can access public method 
        print(self._no2)        # can 
        # print(Base.__no3)
        self.fun() 
        self._fun() 
        # self.__fun()          # cannot call private method of base class 


def main() :
    # bobj = Base() 
    # print(bobj.no1) 
    # print(bobj._no2) 
    # print(bobj.__no3)     # private member cannot access outside class
  
    # bobj.fun() 
    # bobj._fun() 
    # bobj.__fun()          # private method cannot access outside class

    dobj = Derived() 
    dobj.gun() 


if __name__ == "__main__" : 
    main() 










