# no of ways to pass parameter to any function  

# positional parameters 
def prinEmp (empid, name, salary) :
    print("empid        :   ",empid)
    print("name         :   ",name)
    print("salary       :   ",salary)

# keyword parameter 
def printStudent(roll, name , marks ) :
    print("roll     :   ",roll)
    print("name     :   ",name)
    print("marks    :   ",marks)

# default parameter 
def printAccount(accNo , name , balance = 10 ) :
    print("Account no       :   " , accNo) 
    print("Name             :   ",name)
    print("balance          :   ",balance)

# variable number of arguments 
def studentList (*students) : 
    print("lenght of stundes list   :   ",len(students))
    print("{} , {} , {} ".format(students[0] , students[2] , students[1]))



def main() :
    # prinEmp(101 , "Jaydeep" , 98000) 
    # printStudent(roll=101 , name="Jaydeep" , marks=80)
    # printAccount(101, "Jaydeep")
    # studentList("Jaydeep","Rohan","Kishor")
    pass 



if __name__ == "__main__" : 
    main() 