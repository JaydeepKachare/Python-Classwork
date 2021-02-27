# addtion of two number complete code 

# defintiion of addition function 
def addition(num1,num2) :
    ans = num1 + num2 
    return ans 

# definition of subtraction function 
def subtraction(num1,num2) :
    ans = num1 - num2 
    return ans 

# entry point function
def main() :
    num1 = int(input("Enter num1    :   "))
    num2 = int(input("Enter num2    :   ") )

    answer1 = addition(num1,num2) 
    answer2 = subtraction(num1,num2)

    print("Addition is      :   ",answer1) 
    print("Subtraction is   :   ",answer2)

# code starter 
if __name__ == "__main__" : 
    main() 
