# take unmber as input and find factorial 

def fact(num) :
    # ---------------------------------------------------------------
    # winding phase 
    # base condition
    if num == 0 : 
        return 1    # return value after bas condition == True
    # ----------------------------------------------------------------

    # unwinding phase 
    return num * fact(num-1)


def main() :
    num = int(input("Enter any number   :   ")) 
    print("{}! = {}".format(num,fact(num)))



if __name__ == "__main__" : 
    main() 