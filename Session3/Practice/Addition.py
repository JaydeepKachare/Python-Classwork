# Program for addition of two number 

import FunctionSum 

def main() :
    num1 = int(input("Enter num1    :   "))
    num2 = int(input("Enter num2    :   "))

    ans = FunctionSum.sum(num1,num2)

    print("Result is    :   ",ans)

if __name__ == "__main__" :
    main() 