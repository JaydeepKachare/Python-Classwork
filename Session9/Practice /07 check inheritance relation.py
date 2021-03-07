# check inheritance realation between two classes 

class Base :
    pass


class Derived (Base) : 
    pass


def main() :
    b = Base() 
    d = Derived() 

    print(issubclass(Base,Derived))
    print(issubclass(Derived,Base))

    print("b is instance of Base    : ",isinstance(b,Base))
    print("d is instance of Base    : ",isinstance(d,Base))

    print("d is instance of Derived : ",isinstance(d,Derived))
    print("b is instance of Derived : ",isinstance(b,Derived))

if __name__ == "__main__" : 
    main() 