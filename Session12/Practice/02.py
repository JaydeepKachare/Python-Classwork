# Access specifiers in python Inheritance 

class Base : 
    def __init__(self):
        pass

    def fun(self) :                     # public method                  
        print("Inside Base.fun")

    def _gun(self) :                    # protected method 
        print("Inside Base._gun")

    def __sun(self) :                   # private method 
        print("Inside Base.__sun")




def main() :
    b = Base() 
    b.fun()         # public method 
    b._gun()        # protected method 
    # b.__sun()       # private method    ==> Error



if __name__ == "__main__" : 
    main() 