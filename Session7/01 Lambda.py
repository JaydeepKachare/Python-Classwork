# Demo of List data type

# named function
def add (num1 , num2) :
    answer = num1 + num2 
    return answer 


# lambda function 
# name = Lambda parameters : body 
sum = lambda num1,num2 : num1+num2 


# main function 
def main() :
    num1 = int(input("Enter num1 : "))
    num2 = int(input("Enter num2 : "))
    result1 = add(num1,num2) 
    print("Addition of {} and {} is {} with normal function".format(num1,num2,result1))
    result2 = sum(num1,num2)
    print("Addition of {} and {} is {} with lambda function".format(num1,num2,result2))



# call to main function 
if __name__ == "__main__" : 
    main() 




