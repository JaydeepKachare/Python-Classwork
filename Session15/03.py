
class AgeInvalid (Exception) : 
    def __init__(self, data):
        self.data = data 
    


def main() : 
    try : 
        age = int(input("Enter age : "))

        if age<18 : 
            raise AgeInvalid("Your age is less than 18")
    
    except AgeInvalid as obj : 
        print(obj)
    
    else : 
        print("your age is greater than 18")

    


if __name__ == "__main__" : 
    main() 