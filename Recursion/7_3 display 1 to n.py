# display numbers from 1 to n 

def display1(num) : 
    if num == 1 :
        print(num) 
        return 
    
    print(num)              # print in winding phase 
    display1(num-1)     


def display2(num) : 
    if num == 1 :
        print(num)
        return 
    
    display2(num-1)
    print(num)              # print in unwinding phase 



def main() :
    num = int(input("Enter any number   :   "))
    # display1(num)
    display2(num)


if __name__ == "__main__" : 
    main() 