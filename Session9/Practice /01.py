
class Person : 
    def __init__(self,name,age):
        print("Inside constructor")
        self.name = name 
        self.age = age 
    
    def printInfo(self) : 
        print("Inside printInfo")
        print("Name : {}          Age : {}".format(self.name,self.age))



def main() :
    p1 = Person("Jaydeep",26)   # __init__(p1,name,age)
    p1.printInfo()              # printInfo(p1)

    print(p1.__str__()) 

if __name__ == "__main__" : 
    main()
