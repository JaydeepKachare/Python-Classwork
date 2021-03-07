# inheritance demo in python 

class Person : 

    def __init__(self,name,age):
        self.name = name
        self.age = age

    def printInfo(self) : 
        print("inside Person.printInfo ")
        print("name : {} age : {} ".format(self.name,self.age))

    def displayPerson(self) : 
        print("inside Person.displayPerson ")
        print("name : {} age : {} ".format(self.name,self.age))

    
class Employee(Person) : 

    def __init__(self, name, age, salary, empid):
        Person.__init__(self,name,age)
        # super().__init__(name,age) 
        self.salary = salary
        self.empid = empid
    
    def printInfo(self):
        print("inside Employee.printInfo ")
        print("name : {} age : {} empid : {} salary : {} ".format(self.name,self.age, self.empid , self.salary))

    def displayEmployee(self):
        print("inside Employee.displayEmployee ")
        print("name : {} age : {} empid : {} salary : {} ".format(self.name,self.age, self.empid , self.salary))


def main() :
    # p1 = Person("Jaydeep",26)
    # p1.displayPerson() 
    # p1.printInfo() 

    e1 = Employee("Jaydeep",26,1000,101)
    e1.displayEmployee() 
    e1.printInfo() 

if __name__ == "__main__" : 
    main() 