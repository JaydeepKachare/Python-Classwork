

def main() :
    num = int(input("Enter any number   :   "))
    flag = False

    for i in range(2,num) : 
        if num%i == 0 : 
            print("Number is not prime ")
            flag = True 
            break 
        
    if flag == False :
        print("Number is prime ")



if __name__ == "__main__" : 
    main() 
