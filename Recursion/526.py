# display all the  integer in number 

def display(n) : 
    if n == 0 : return "zero" 
    elif n==1 : return "one"
    elif n==2 : return "two"
    elif n==3 : return "three"
    elif n==4 : return "four"
    elif n==5 : return "five"
    elif n==6 : return "six"
    elif n==7 : return "seven"
    elif n==8 : return "eight"
    elif n==9 : return "nine"

def recnum(num) :
    if num == 0 :
        return 
    
    recnum(int(num/10)) 
    print(display(num%10))


def main() :
    num = int(input("Enetr any number : "))
    recnum(num)

if __name__ == "__main__" : 
    main() 