# recursive function to find sum of all evennumber in list 


def recSum(l1) :
    if len(l1) == 0 :
        return 0 
    
    if l1[0]%2 == 0 : 
        return l1[0] + recSum(l1[1:])

    return recSum(l1[1:])
    

def main() :
    l1 = [11,22,33] 
    sum = recSum(l1)
    print("Sum : ",sum)



if __name__ == "__main__" : 
    main() 