# calculate nth term of fibonacci series 


def fibo(num) : 
    if num == 0 or num == 1 : 
        return 1 
    
    return fibo(num-1) + fibo(num-2)



def main() :
    n = int(input("Enter term to find   :   "))
    print(fibo(n))



if __name__ == "__main__" : 
    main() 