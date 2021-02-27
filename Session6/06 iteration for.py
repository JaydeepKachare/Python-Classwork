# for loop in python 

def display (message,val) : 
    for i in range(val,0,-1) :
        print(message,"     ",i)

def main() :
    message = input("Enter message to print     :   ")
    val = int(input("How may times to print     :   ")) 

    display(message , val)


if __name__ == "__main__" : 
    main() 