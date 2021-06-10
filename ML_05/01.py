import numpy as np


def marvellous() : 
    x = [1,2,3,4,5]
    y = [3,4,2,4,5]

    X_mean = np.mean(x)
    Y_mean = np.mean(y) 

    Numberator = 0 
    Denominator = 0 

    for i in range(len(x)) : 
        Numberator += ((x[i]-X_mean) * (y[i]-Y_mean)) 
        Denominator +=  ((x[i]-X_mean)**2 )

    m = Numberator / Denominator 
    print("values of m : " , m ) 

    c = Y_mean - (m*X_mean) 
    print("values of c : ",c)  


def main() :
    marvellous() 

if __name__ == "__main__" : 
    main()  