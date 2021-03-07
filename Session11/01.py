# OOPS in Python3 

class Marvellous : 
    Value1 = 11                     # class characteristic 

    def __init__(self,no1,no2):     # constructor
        self.i = no1              # instance variable 
        self.j = no2 
        print("Inside Constructor")

    def __del__(self) :             # destructor
        print("Inside Destructor")

    def Fun(self) :                 # instance method 
        print("Inside Fun")
        print("value of j is ",self.j)


def main() :
    obj1 = Marvellous(11,21) 
    obj2 = Marvellous(51,101)

    print("Value of i from obj1 ",obj1.i)               # accessing instance variable
    print("Value of i from obj2 ",obj2.i)
    print("Value of class member ",Marvellous.Value1)   # accesing class variable

    obj1.Fun()                                      # calling instance method 
    obj2.Fun() 

    del obj1 
    del obj2


if __name__ == "__main__" : 
    main() 

