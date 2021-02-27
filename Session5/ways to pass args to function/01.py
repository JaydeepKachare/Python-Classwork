# how to pass arguments to functions

# positional argument passing 
# sequence of passed arguments matters 
def student(name, roll, address, marks):
    print("Name     :   ", name)
    print("roll     :   ", roll)
    print("address  :   ", address)
    print("marks    :   ", marks)


# keyword arguments 
def computer(ram, processor, HDD):
    print("RAM size     :   ", ram)
    print("processor    :   ", processor)
    print("Hard disk    :   ", HDD)


# default argument
def calcArea(radius, PI=3.14):
    print("Values of PI is {}".format(PI))
    area = PI * radius * radius
    return area


# variable number of argument 
def fun(*value):
    print("number of arguments are : ", len(value))


def main():
    # student("Jaydeep" , 101 , "Pune" , 80)
    # computer(processor="i9",ram="16 GB", HDD="512 GB")
    # calcArea(10,3)
    # calcArea(10)
    fun(10, 20, 30, 40, 50)


if __name__ == "__main__":
    main()
