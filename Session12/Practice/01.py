# Access specifiers in python Inheritance 

class Base : 
    def __init__(self):
        self.num1 = 10          # public member 
        self._num2 = 20         # protected member 
        self.__num3 = 30        # private members 



def main() :
    b = Base() 
    print(b.num1)           # public member access 
    print(b._num2)          # protected member access 
    # print(b.__num3)       # private member access ==> Error 



if __name__ == "__main__" : 
    main() 