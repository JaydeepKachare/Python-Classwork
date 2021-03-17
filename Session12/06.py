# Duck typing in python 

class C : 
    def LearnAndCode(self) : 
        print("Learning C Programming")


class CPP : 
    def LearnAndCode(self) : 
        print("Learning CPP Programming")


class GoLang : 
    def LearnAndCode(self) : 
        print("Learning GoLang Programming")


class Demo : 
    pass


class Developer : 
    def coding(self,language) : 
        language.LearnAndCode() 


def main() :
    cobj = C() 
    cppobj = CPP() 
    goobj = GoLang() 
    dobj = Demo() 

    obj = Developer() 

    obj.coding(cobj)
    obj.coding(cppobj)
    obj.coding(goobj)
    # obj.coding(dobj)        # Demo object has no method for LearnAndCode ==> Error 

if __name__ == "__main__" : 
    main() 



