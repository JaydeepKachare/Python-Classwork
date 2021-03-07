# OOP class and object


class Demo : 
    def __init__(self):
        print("Inside constructo")
        self.i = 10 
        self.y = 20 


def main() :
    print("Inside main")

    obj = Demo()                # obj = __init__(obj)
    print("Type of obj is :     ",type(obj))



if __name__ == "__main__" : 
    main() 


