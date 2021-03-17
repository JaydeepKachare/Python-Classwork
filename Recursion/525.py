# find whether element of list are in strict ascending order or not 

def recOrder(l1) : 
    if len(l1) == 0  or len(l1) == 1 :
        return True 
    
    if l1[0] < l1[1] : 
        return recOrder(l1[1:])
    else : 
        return False 



def main() : 
    # l1 = [11,22,15,33,44]
    l1 = [11,22,33,44,55] 
    print(recOrder(l1))

if __name__ == "__main__" : 
    main() 