# Restrict access of class variable across class 



class Person :
    # class variable 
    Country = "India"
    __country  = "india"

    def __init__(self,name,age):
        print("Inside __init__ of Person ")
        self.name = name 
        self.age = age

    def printInfo(self) : 
        print("Person.printInfo")
        print("Name : {}        Age : {}        Country : {}".format(self.name,self.age , Person.Country)) 
        print("__country    : ",Person.__country)
        # can access class variable from here but not from outside class 


def main() :
    obj = Person("Jaydeep" , 126) 
    obj.printInfo() 

    # print("\n we can print class variable from here also  =>  Country :",Person.Country)
    # print("\n we can print class variable from here also  => __country :",Person.__country)


    # print(obj.name)
    # print(obj.age)
    # similar way  we can access members (characteristics) of object 
    # Its like they are public 
    # to make  them private use __ (double unserscore ) 

    # simple names ===> public variable 
    # __ names     ===> private variable



    # as we all know there is no such thing called privacy  in Programming 
    # as at binary everything is naked 
    # way to access private (hidden) variable 

    print(obj._Person__country)         # now you can access country 
    



if __name__ == "__main__" : 
    main() 