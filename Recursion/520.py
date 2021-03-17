# display all positive proper divisior and their sum

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
    print("sum : ",sum)



if __name__ == "__main__" : 
    main() 