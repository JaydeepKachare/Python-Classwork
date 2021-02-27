# use of selection statement in python 
# if .., else 

def isEven ( num ) :
    if num%2 == 0 :
        print("{} is Even Number".format(num)) 
    else :
        print("{} is Odd Number".format(num)) 

def main() :
    num = int(input("Enter any number : "))
    isEven(num=num)

if __name__ == "__main__" : 
    main() 

