
# addition with for loop
def add(List) : 
    sum = 0 
    for i in range(0,len(List)) :
        sum = sum + List[i] 
    return sum 


# addition with while loop
def addW (List) : 
    sum = 0 
    i = 0 
    while i < len(List) :
        sum = sum + List[i]
        i = i+1 
    return sum 


# addition recursive 
sum = 0 
i = 0 
def addRec (List) :
    global sum 
    global i
    while i < len(List) :
        sum = sum + List[i]
        i = i+1
        addRec(List) 
    return sum 


def main() :
    arr = [] 
    size = int(input("Enter size of list : "))

    for i in range(0,size) :
        arr.append(int(input("Enter element {}  :   ".format(i))))


    print("Entered data is {}".format(arr))
    # addition = add(arr) 
    # addition = addW(arr)
    addition = addRec(arr)
    print("Addition of List is {}".format(addition))


if __name__ == "__main__" : 
    main() 