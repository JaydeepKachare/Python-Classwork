
def factorial (num) :
    fact = 1 
    if num == 1 :
        return 1 
    
    fact = fact * num 
    num = num - 1 
    fact = fact * factorial(num) 
    return fact 


def main() :
    num = int(input("Enter number : "))
    fact = factorial(num)
    print("{}! = {}".format(num,fact))



if __name__ == "__main__" :
    main() 