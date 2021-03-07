# various types of methods in python class 

class Car : 
    # class variable 
    pollutionNorm = "BS IV" 

    # constructor 
    def __init__(self,model,company):
        self.model = model 
        self.company = company
        print("Inside constructor of Car ")

    # instance method 
    def printCar(self) : 
        print("Car Name : {} Comapany : {} ".format(self.model,self.company)) 


    # class method 
    # class method are use to access class variable 
        # which are associated with entire class 
    @classmethod
    def carInfo(cls) : 
        print("Car follows : {} ".format(cls.pollutionNorm))

    # static method 
    # method which is associated with car but not accessing 
    # instance variable or class variable 
    @staticmethod
    def AutoInfo() : 
        print("This class is associated with Car ")

    # destructor 
    def __del__(self) : 
        print("Inside Destructor of Car ")


def main() :
    c1 = Car("Celerio" , "Maruti") 
    
    # static method 
    # called by name of class 
    Car.AutoInfo()

    # class method 
    # called by name of class 
    Car.carInfo() 

    # instance method 
    # called by instance of class 
    c1.printCar() 



if __name__ == "__main__" : 
    main() 