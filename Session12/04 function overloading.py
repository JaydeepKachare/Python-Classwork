# function overloading 


class Demo : 
    def add(self,no1,no2) : 
        return no1+no2
    
    def add(self,no1,no2,no3) : 
        return no1+no2+no3 
    

obj = Demo() 
print(obj.add(10,20))
print(obj.add(10,20,30))

