# accept n numbers from users and print sum of all accepted program 

def sumList( list ) :
    result = 0 
    for i in range(0,len(list)) :
        result = result + list[i]
    return result  


def main() :
    num = int(input("How many values you want to enter    :   "))
    
    arr = [] 
    for i in range(0,num) :
        no = int(input("Enter number {}     :   ".format(i)))
        arr.append(no) 

    print("Accepted data is {}".format(arr))

    result = sumList(arr) 
    print("Sum of numbers of liat is {} ".format(result))




if __name__ == "__main__" : 
    main() 

