# getting overloaded method with default argument

class Demo : 
    def add(self,no1=None,no2=None,no3=None) : 
        if no1 != None and no2 != None and no3 != None : 
            return no1+no2+no3 
        elif no1 != None and no2 != None  : 
            return no1+no2 
        if no1 != None  : 
            return no1
        else : 
            return 0  



def main() :    
    obj = Demo() 
    print(obj.add(10) )
    print(obj.add(10,20) )
    print(obj.add(10,20,30) )



if __name__ == "__main__" : 
    main() 