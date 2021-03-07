# Take n numbers from users 
# and find even nos , prime nos 

class Numbers : 
    def __init__(self,no = 5):
        self.size = no 
        self.arr = [] 

    def __del__ (self) : 
        print("Deallocatinf memory of object ")
        del self.arr 

    def Accept(self) : 
        print("Enter Elements in Object ")
        for i in range(0,self.size) : 
            self.arr.append(int(input("Enter Elem {} :  ".format(i))))

    def Display(self) : 
        print("Entered Elements are ")
        for i in range(0,self.size) : 
            print("Element {}    :   {}".format(i,self.arr[i]))

    def Summation(self) : 
        sum = 0 
        for i in range(0,self.size) :
            sum += self.arr[i]
        return sum 

    def DisplayEven(self) : 
        print("Even Element in arr  :"  )
        for i in range(0,self.size) : 
            if self.arr[i] % 2 == 0 : 
                print("{}   ".format(self.arr[i]))

    def DisplayOdd(self) : 
        print("Odd Element in arr :")
        for i in range(0,self.size) : 
            if self.arr[i] % 2 != 0 :
                print("{} ".format(self.arr[i]))

    def isPerfect(self,num) : 
        sumFact = 0 
        for i in range(1,num) : 
            if (num % i == 0 ) :
                sumFact = sumFact + i 
        if (num == sumFact) : 
            return True 
        else : 
            return False 

    def perFectNum(self) : 
        print("Perfect Number in List are : ")
        for i in range(0,self.size) : 
            if (self.isPerfect(self.arr[i]) == True) : 
                print(self.arr[i])
    
    def DisplayPrime(self) : 
        print("Prime numbers in objects are : ") 
        for i in range(0,self.size) : 
            for j in range(2,self.arr[i]) : 
                if (self.arr[i] % j == 0 ) : 
                    break 
            print(self.arr[i])
    

def main() :
    num = int(input("How many Element you want   :    ")) 
    obj1 = Numbers(num)
    obj1.Accept() 
    obj1.Display() 
    obj1.DisplayEven() 
    obj1.DisplayOdd() 

    summation = obj1.Summation() 
    print("Summation of obj1.arr is {} ".format(summation) )

    obj1.perFectNum()
    obj1.DisplayPrime()  
    del obj1 

if __name__ == "__main__" : 

    main() 

