# OOPS in python demo 

class Employee : 
    # class vvariable 
    company = "XYZ pvt ltd"

    # constructor 
    def __init__(self,empid,name,salary):
        self.empid = empid 
        self.name = name 
        self.salary = salary 
        print("Inisde Constructor of Employee ")

    # instance method 
    def printInfo(self) : 
        print("Name : {} Empid : {} Salary : {} ".format(self.name,self.empid,self.salary))
        print("Company : {}".format(Employee.company))
    
    # destructor 
    def __del__(self) : 
        print("Inside Destructor of Employee")


def main() : 
    emp = Employee("101" , "Jaydeep" , 10000)
    emp.printInfo() 


if __name__ == "__main__" : 
    main() 