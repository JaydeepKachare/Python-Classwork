# find greates common divisior of two number 

def GCD(num1,num2) : 
    if (num2==0) : 
        return num1

    return GCD(num2,num1%num2) 


def main() :
    print(GCD(12,26))



if __name__ == "__main__" : 
    main() 