# __str__ method in python object


class Complex : 

    def __init__(self,real,imag):
        print("Inside Complex __init__")
        self.real = real 
        self.imag = imag
    
    def __str__(self):
        return "Real : {}   Imag : {}".format(self.real,self.imag)


def main() :
    c1 = Complex(10,20) 
    print(c1)
    print(c1.__str__() )



if __name__ == "__main__" : 
    main() 