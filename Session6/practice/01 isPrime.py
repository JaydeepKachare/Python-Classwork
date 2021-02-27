# check whether given number is prime or not 

def isPrime (num) :
    for i in range(2,num) :
        if num % i == 0 :
            return False 
    return True 


# main function 
def main() :
    num = int(input("Enter any number   :   ")) 

    if isPrime(num) == True :
        print("{} is prime number ".format(num)) 
    else :
        print("{} is not prime number ".format(num))



if __name__ == "__main__" :
    main() 