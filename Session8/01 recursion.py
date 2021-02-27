
# iterative number 
def displayNumI (num) :
    for i in range(0,num) :
        print("Hello !!!")


# recursive approach
def displayNumR (num) :
    if num != 0 :
        print("Hello !!!")
        num = num - 1 
        displayNumR(num)


# get recusrion limit 
import sys 
def getLimit () :
    print("Current recusion Limit : {}".format(sys.getrecursionlimit()))
    sys.setrecursionlimit(1500)
    print("Modified recusion Limit : {}".format(sys.getrecursionlimit()))


def main() :
    # num = int(input("Enter no of iteration  :   ")) 
    # displayNum(num)
    # displayNumR(num)
    getLimit() 


if __name__ == "__main__" :
    main() 

