


class Person :
    # class variable 
    Country = "India"

    def __init__(self,name,age):
        print("Inside __init__ of Person ")
        self.name = name 
        self.age = age

    def printInfo(self) : 
        print("Person.printInfo")
        print("Name : {}        Age : {}        Country : {}".format(self.name,self.age , Person.Country)) 



def main() :
    obj = Person("Jaydeep" , 126) 
    obj.printInfo() 

    print("\n we can print class variable from here also  =>  Country :",Person.Country)


if __name__ == "__main__" : 
    main() 