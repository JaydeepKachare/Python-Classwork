# function accept list and addition of elemet of list  

def addList( list ) :
    result = 0 

    for i in range(0,len(list)) :
        print("arr[ {} ]  :   {}".format(i,list[i]))
        result = result + list[i]

    return result


def main() :
    arr = [10,20,30,40,50]
    result = addList(arr)
    print("Addition of all number of list is {}".format(result))


if __name__ == "__main__" : 
    main() 

