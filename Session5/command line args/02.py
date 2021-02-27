# addition of two number using command line argument 
import sys

def add (num1 , num2) : 
    answer = num1 + num2 
    return answer 

def main() :
    if ((len(sys.argv) < 3) or (len(sys.argv) > 3)) :
        print("Invalid number of arguments arguments") 
        return 
    
    print("No of arguments passed from command line     :    ",len(sys.argv))
    num1 = int(sys.argv[1])
    num2 = int(sys.argv[2])

    addition  = add(num1,num2) 
    print("Addition of {} and {} is {} ".format(num1,num2,addition))    


if __name__ == "__main__" : 
    main() 