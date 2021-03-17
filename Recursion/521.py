# find if number is perfect or not 

def properDivisor(num,i=1) : 
    sum = 0 
    if num<=i : 
        print() 
        return 0
    
    if num%i == 0 : 
        print(i,end=" ") 
        sum += i 
    
    return sum + properDivisor(num,i+1)

def main() : 
    num = int(input("Enter any number : "))
    sum = properDivisor(45)
    if sum == num : 
        print("Number is perfect Number ")
    else : 
        print("Number is not perfect number ")



if __name__ == "__main__" : 
    main() 