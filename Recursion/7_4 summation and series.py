# display summation ad series upto n


def summation(num) : 
    if num == 1 :
        print("{} + ".format(num), end=" " ) 
        return 1 
    
    sum = num + summation(num-1) 
    print(" {} + ".format(num),end=" ") 
    return sum 



def main() :    
    num = int(input("Enter any number :     "))
    result = summation(num) 
    print(" = " ,result)




if __name__ == "__main__" : 
    main() 