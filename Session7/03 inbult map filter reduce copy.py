# accept N numbers from user 
# add 2 in every even number 
# perform additio of modified set 

# i/p => [1,2,3,5,4,6,7]
# after filter => [2,4,6]
# after map => [4,6,8]
# after refuce => 18

# function to check if number is even or odd 
from functools import reduce

def isEven (num) :
    return not num%2 


# increment value passed to function by 2
def increment (num1) :
    return num1+2

# addition of two number 
def addition (num1,num2) :
    return num1+num2 


# main function
def main() :
    List = [] 
    count = int(input("How many numbers to enter : ")) 

    for i in range(0,count) :
        num = int(input("enter any number : "))
        List.append(num)
    
    print("your entered data is {}".format(List))

    newList = list(filter(isEven,List))                    # newList = marvellous(list)
    # newData = filter(functionName, Data)
    print("newList input is {}".format(newList))

    resultList = list((map(increment,newList)))              # resultList = addMarvellou(newList) 
    # newDate = map(function , Data)
    print("resultList input is {}".format(resultList))


    sum = reduce(addition,resultList)                       # sum = sumList(resultList)
    print("Addition of resultList is {} ".format(sum))



# main starter 
if __name__ == "__main__" : 
    main() 

