# addtion of two number complete code with module 

# import functions needed for program from Arithmetic.py

# import Arithmetic as AR           # aithemtetic module
# from Arithmetic import addition , subtraction
from Arithmetic import addition , subtraction 

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

