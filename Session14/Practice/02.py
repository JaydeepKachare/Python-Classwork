# classis sumarray example for multithreding 

import time
import threading

class SumArray : 
    def add(self,arr,name,lock) : 
        lock.acquire() 
        total = 0  
        for ele in arr : 
            total += ele 
            print(f"Running total {name}: ",total)
            time.sleep(0.5)
        lock.release() 
        return total 

class PThread : 
    sa = SumArray() 
    def __init__(self,numList,name):
        self.numList = numList
        self.name = name  
    
    def getTotal(self,lock) :
        # lock.acquire() 
        result = PThread.sa.add(self.numList,self.name,lock)
        print(f"{self.name} total is {result}") 
        # lock.release() 

def main() :    
    print("Start of main ")

    lcok = threading.Lock() 

    arr1 = [11,12,13,14,15,16,17,18,19,20]
    th1 = PThread(arr1,"Th1") 
    # th1.getTotal() 
    t1 = threading.Thread(target=th1.getTotal,args=(lcok,))
    t1.start() 


    arr2 = [21,22,23,24,25,26,27,28,29,30]
    th2 = PThread(arr2,"Th2") 
    # th2.getTotal() 
    t2 = threading.Thread(target=th2.getTotal,args=(lcok,))
    t2.start() 

    print("End of main")



if __name__ == "__main__" : 
    main() 