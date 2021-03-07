# find prime factors of given number 

# using while loop
def primeFactors(num) : 
    i = 2 
    while (i <= num ) :
        if num % i == 0 :
            print(i,end=" ") 
            num = int(num/i)
            i = 1 
        i+=1 
    
    print()

# using recursion 
def primeFactorsR(num,i) :

    if i >= num : 
        print(i)
        return 
    
    if (num%i == 0) : 
        print(i,end=" ") 
        primeFactorsR(int(num/i),2) 
    else :
        primeFactorsR(num,i+1)
    
    return 



def main() :
    num = int(input("ENterany number    :    "))
    print("Prime factors of {} are ".format(num), end=" ")
    # primeFactors(num)
    primeFactorsR(num,2)


if __name__ == "__main__" : 
    main() 