# addition of two number 

def addition(num1, num2):
    ans = num1+num2 
    return ans 


num1 = int(input("Enter num1    :   "))
num2 = int(input("Enter num2    :   "))

ans = addition(num1,num2)

print("Addition :    ",ans)



num1 = int(input("Enter num1    :   "))
num2 = int(input("Enter num2    :   "))

ans = addition(num1,num2)                   # reusing same function (function call)

print("Addition :       ",ans)

