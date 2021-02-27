# addition of two number 

import AddFunction 

 

def main():
    num1 = int(input("Enter num1    :   "))
    num2 = int(input("Enter num2    :   "))

    ans = AddFunction.addition(num1,num2)
 
    print("Addition :    ",ans)


# print(__name__)                                 # o/p ==>   __main__ 

if __name__ == "__main__" :
    main() 
    