import os 
import time
import multiprocessing

# ----------------------------------------------------------
def square(num) : 
    return num * num 
# ------------------------------------------------------

# ------------------------------------------------------
def serialProcessing() :
    start = time.time() 
    print("Inside serialProcessing") 
    arr = range(10000000) 
    ret = [] 
    
    for i in arr : 
        ret.append(square(i))

    # print("result of serialProcessing is ",ret)
    end = time.time() 
    print("Rrequired for serialProcessing time is ",end-start)
# ------------------------------------------------------

# ------------------------------------------------------
def parallelProcessing() :
    start = time.time() 
    print("Inside parallelProcessing") 
    arr = range(10000000) 
    
    pobj = multiprocessing.Pool() 
    ret = pobj.map(square,arr)

    # print("result of parallelProcessing is ",ret)
    end = time.time() 
    print("Rrequired for parallelProcessing time is ",end-start)
# ------------------------------------------------------

def main() : 
    serialProcessing() 
    parallelProcessing() 


if __name__ == "__main__" : 
    main() 