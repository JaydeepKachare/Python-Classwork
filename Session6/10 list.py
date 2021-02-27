# function accept list and display element iun list 

def printList( list ) :
    for i in range(0,len(list)) :
        print("arr[ {} ]  :   {}".format(i,list[i]))


def main() :
    arr = [10,20,30,40,50]
    printList(arr)



if __name__ == "__main__" : 
    main() 

