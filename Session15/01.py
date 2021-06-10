
class Complex : 
    def __init__(self,real,imag):
        self.real = real 
        self.imag = imag

    def __str__(self):
        return f"real : {self.real}      image : {self.imag}"

    def __add__(self, complex) : 
        result = Complex(0,0) 
        result.real = self.real + complex.real
        result.imag = self.imag + complex.imag
        return result


def main() : 
    obj1 = Complex(10,20)
    obj2 = Complex(30,40)   

    result = obj1 + obj2 

    print(result)


if __name__ == "__main__" : 
    main() 