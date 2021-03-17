# recursive function for coubnting prime numbers between a and b 

def isPrime(num,i=2) : 
    if num == i :
        return True 
    
    if num%i == 0 : 
        return False 
    else : 
        return isPrime(num,i+1)


count = 0 
def primeCount(a,b) : 
    global count 
    if a==b : 
        return 
    
    if (isPrime(a) == True) : 
        count += 1 
    primeCount(a+1,b) 


def main() :
    low = int(input("Enetr lower limit : "))
    high = int(input("Enter high limit : "))

    primeCount(low,high)
    global count 
    print("No of prime no between {} and {} are {}".format(low,high,count))



if __name__ == "__main__" : 
    main() 