# take input  n and find summation from 1 to n 

def summation(num) : 
    if num == 0 :
        return 0 
    return num + summation(num-1)

def main() :
    num = int(input("Enter any number   :   ")) 
    print("summation from 1 to {} = {}".format(num,summation(num)))


if __name__ == "__main__" : 
    main() 