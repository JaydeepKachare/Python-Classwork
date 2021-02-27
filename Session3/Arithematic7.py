# addition of two number 

def addition(num1, num2):
    ans = num1+num2 
    return ans 


def main():
    num1 = int(input("Enter num1    :   "))
    num2 = int(input("Enter num2    :   "))

    ans = addition(num1,num2)

    print("Addition :    ",ans)


# print(__name__)                                 # o/p ==>   __main__ 

if __name__ == "__main__" :
    main() 
    