# Demo Program for class methods 

class Arithmetic :
    value = 111                         # class variable 
    def __init__(self,num1,num2):
        print("Inside constructor")
        self.num1 = num1 
        self.num2 = num2
    
    def addition(self) :
        print("Common variable value    :   ",Arithmetic.value)
        print("Common variable value    :   ",self.value)
        return self.num1 + self.num2 

    def subtraction(self) :
        return self.num1 - self.num2 
    

def main() :
    print("Class variable of Arithmetic is      ",Arithmetic.value)
    print()

    obj1 = Arithmetic(151,51) 
    print("Obj1 Addiotn is ",obj1.addition())
    print("Obj1 Subtraction is ",obj1.subtraction())

    print() 

    print("Obj2 Addiotn is ",obj2.addition())
    obj2 = Arithmetic(30,20)
    print("Obj2 Subtraction is ",obj2.subtraction())


if __name__ == "__main__" : 
    main() 

