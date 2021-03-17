# program for unserstanding Decorator in python

# Assume as Inbuilt function from module 
# do not modify anything here  
def sub(num1,num2) : 
    return num1 - num2 


def subdecorator(func_name) : 
    def updator(a,b) : 
        if a < b : 
            temp = a 
            a = b 
            b = temp 
        return  func_name(a,b)

    return updator 
    


def main() : 
    # vtake input from users 
    num1 = int(input("Enter num1 : "))
    num2 = int(input("Enter num2 : "))

    # function call 
    # result = sub(num1,num2)
    # result = subdecorator(sub,num1,num2)

    subFunc = subdecorator(sub)
    result = subFunc(num1,num2)

    # expected result should be always +ve 
    print("result   :   ",result)


if __name__ == "__main__" : 
    main() 
