# find sum of digit of number till it is reduceo single digit 

def sumdigit(num) : 
    if int(num/10) == 0 :
        return num 
    
    return num%10 + sumdigit(int(num/10)) 


def main() :
    num = int(input("Enter any number   :   "))
    sumd = sumdigit(num)
    print("Sum of digit of {} is {} ".format(num,sumd))



if __name__ == "__main__" : 
    main() 