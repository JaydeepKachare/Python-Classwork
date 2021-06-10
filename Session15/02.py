

def main() : 
    num1 = int(input("Enter num1 : "))
    num2 = int(input("Enter num2 : "))

    try : 
        result = num1//num2 

    except Exception as ex : 
        print("Exception occured : ",ex) 

    else :
        print("result : ",result)

    finally : 
        print("Deallocate all resourses ")

if __name__ == "__main__" : 
    main() 