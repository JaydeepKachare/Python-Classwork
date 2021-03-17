# Take input ofn number and return sum 

def recSum (num) : 
    sum = 0 
    if num == 0 : 
        return 0 

    val = int(input("Enter number to sum : "))
    sum = sum + val + recSum(num-1)
    return sum

def main() : 
    num = int(input("How many number s to add : ")) 
    result = recSum(num) 
    print("result : ",result)



if __name__ == "__main__" : 
    main() 