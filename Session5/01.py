
def demo() :
    pass 


# import module for arithmetic function 
import functionFile

# main function for entry point 
def main() :
    value1 = int(input("Enter num1 : "))
    value2 = int(input("Enter num2 : "))
    addition = functionFile.add(value1,value2)
    subtraction = functionFile.sub(value1 ,value2)

    print("Addition of {} and {} is {}".format(value1,value2,addition))
    print("Subtraction of {} and {} is {}".format(value1,value2,subtraction))

if __name__ == "__main__" : 
    main() 

