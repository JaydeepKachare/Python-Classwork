# reverse list recursively 

def reverseList(l1):
    if len(l1) == 1 or len(l1) == 0 : 
        return 
    
    l1[0],l1[-1] = l1[-1],l1[0]
    l2= l1[1:-2]
    reverseList(l2)




def main() :
    l1 = ["h","e","l","l","o"] 
    print("List before reversing : ",l1)
    reverseList(l1)
    print("List after  reversing : ",l1)

if __name__ == "__main__" : 
    main() 