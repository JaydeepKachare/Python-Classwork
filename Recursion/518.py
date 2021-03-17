# Enter line of text and and diaplay it in reverse order 

def recDisplay(str) : 
    if len(str) == 0 : 
        return 
    
    recDisplay(str[1:])
    print(str[0],end="")
    return 



def main() : 
    line = str(input("enter line of text : "))
    print("Reverse str is : ",end=" ")
    recDisplay(line)
    print()


if __name__ == "__main__" : 
    main() 