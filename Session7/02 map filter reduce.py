# accept N numbers from user 
# add 2 in every even number 
# perform additio of modified set 

# i/p => [1,2,3,5,4,6,7]
# after filter => [2,4,6]
# after map => [4,6,8]
# after refuce => 18

# function to check if number is even or odd 
def isEven (num) :
    if num%2 == 0 :
        return True
    else :
        return False 


# filter out even odd number and create new list 
def marvellous (list) :
    brr = [] 
    for i in range(0,len(list)) :
        if isEven(list[i]) == True :
            brr.append(list[i])
    
    return brr 


# addition of two number in even
def addMarvellou (list) :
    for i in range(0,len(list)) : 
        list[i] = list[i] + 2 
    return list


def sumList (list) :
    sum = 0 
    for i in range(0,len(list)) : 
        sum = sum + list[i]
    return sum 


# main function
def main() :
    list = [] 
    count = int(input("How many numbers to enter : ")) 

    for i in range(0,count) :
        num = int(input("enter any number : "))
        list.append(num)
    
    print("your entered data is {}".format(list))

    newList = marvellous(list)
    print("Modified input is {}".format(newList))

    resultList = addMarvellou(newList) 
    print("Final output is {}".format(resultList))

    sum = sumList(resultList)
    print("Addition of result list is {} ".format(sum))



# main starter 
if __name__ == "__main__" : 
    main() 

