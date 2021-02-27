# entry  point function for checking number is even or odd

# import moduloe for use of function 
import isEven 

def main () :
    num = int(input("Enter any number : ")) 
    value = isEven.checkFun(num) 

    if value == True : 
        print("{} is Even".format(num))
    else :
        print("{} is Odd".format(num))


if __name__ == "__main__" :
    main() 