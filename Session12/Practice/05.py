# function overloading in python 


class Demo : 
    def add (self,num1,num2) : 
        print(num1+num2) 

    def add (self,num1,num2,num3) : 
        print(num1+num2+num3) 


def main() : 
    d = Demo() 
    # d.add(10,20)      # Error b/c new method for add is available 
    d.add(10,20,30)
                
    # there is np function overloading in python 
    # but we can acheive overloading in ways --> variable no of arguments 
    # another way --> Default argument




if __name__ == "__main__" : 
    main() 