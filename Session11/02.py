# Demo 2 for OOPS in python 

class Student : 
    School = "Abhinav" 

    def __init__(self,no1,no2,no3):
        self.m1 = no1 
        self.m2 = no2 
        self.m3 = no3

    def Instance_Total(self) :                      # Instance Method 
        print("Inside instace method")
        return self.m1 + self.m2 + self.m3
    
    @classmethod
    def Class_Display_School(cls) :                 # Class Method 
        print("School Name is : ",cls.School)

    @staticmethod
    def Static_Info() :
        print("This method contains info about school")


def main() :
    Student.Class_Display_School()                  # calling class method

    obj1 = Student(70,80,90)                        # object creation  
    obj2 = Student(55,65,75) 
    obj3 = Student(50,60,70) 

    result1 = obj1.Instance_Total()             # calling instance method 
    print("Total Marks Obtained : ",result1)
    
    Student.Static_Info()           # call static method 


if __name__ == "__main__" : 
    main() 

    