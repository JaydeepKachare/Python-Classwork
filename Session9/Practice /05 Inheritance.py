# Inheritance in Python 

class Person :
    def __init__(self,name,age):
        self.name = name 
        self.age = age 

    def printInfo(self) : 
        print("Name : {}        Age : {}  ".format(self.name, self.age))


class Employee(Person) : 
    def __init__(self, name, age , empid):
        super().__init__(name, age)
        self.empid = empid
    
    def printInfo(self):
        super().printInfo()
        print("Empid : {} ".format(self.empid))


def main() :

    per = Person("Jaydeep",26)
    per.printInfo()  

    emp = Employee("Jaydeep" , 26 , 101) 
    emp.printInfo()

if __name__ == "__main__" : 
    main() 