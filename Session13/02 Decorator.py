# program for unserstanding Decorator in python

# Assume as Inbuilt function from module 
# do not modify anything here  
def sub(num1,num2) : 
    return num1 - num2 


def subdecorator(func_name) : 
    print("10 : Inside subdecorator")
    def updator(a,b) : 
        print("12 : Inside upodator")
        if a < b : 
            temp = a 
            a = b 
            b = temp 
            print("17 : inside updator comparision")
        return  func_name(a,b)

    return updator 
    


def main() : 

    print("23 : inside main")

    # vtake input from users 
    num1 = int(input("Enter num1 : "))
    num2 = int(input("Enter num2 : "))

    print("29 : inpute taken from user ")

    # function call 
    # result = sub(num1,num2)
    # result = subdecorator(sub,num1,num2)

    subFunc = subdecorator(sub)
    
    print("37 : subdecorator called returned value stored in subFunc")


    result = subFunc(num1,num2)
    print("37 : subFunc called returned value stored in result")


    # expected result should be always +ve 
    print("result   :   ",result)

    print("50 : end of main")

if __name__ == "__main__" : 
    main() 
