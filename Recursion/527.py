# return given number in reverse order 

def reverse(num) : 
    sum = 0 
    if num == 0 : 
        return 0 
    
    if num != 0 : 
       rem = num%10 
       return sum*10 + rem  + reverse(num//10)
    else : 
        return sum
    return sum 



num = int(input("Enter any number : "))
revnum = reverse(num)
print("reverse number : ",revnum)