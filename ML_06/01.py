import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt 


def MeanData(arr) : 
    sum = 0 ; 
    size = len(arr)
    for i in range(size) :  
        sum += arr[i]
    
    return sum/size


def marvellousHeadBrain(name) :
    dataset = pd.read_csv(name) 
    print("Size of data set :  ",dataset.shape)

    #Head Size(cm^3),Brain Weight(grams)
    X = dataset["Head Size(cm^3)"].values
    Y = dataset["Brain Weight(grams)"].values

    print("Length of X : ",len(Y))
    print("Length of Y : ",len(X))

    Mean_X = MeanData(X)
    Mean_Y = MeanData(Y)

    Numerator = 0 
    Denomenator = 0 

    for i in range(len(X)) : 
        Numerator += (X[i]-Mean_X)*(Y[i]-Mean_Y) 
        Denomenator += (X[i]-Mean_X)**2 

    m = Numerator / Denomenator 
    print("Value of m is : ",m)    

    c = Mean_Y - (m * Mean_X) 
    print("Value of c is : ",c)


    X_start = np.min(X) - 200
    # X_start = 0 
    X_end = np.max(X) + 200
    x = np.linspace(X_start,X_end) 

    y = m*x + c 

    plt.plot(x,y,color = 'r', label='Regression Line')
    plt.scatter(X,Y,color='b') 
    
    plt.xlabel("Head Size")
    plt.ylabel("Brain Weight ")

    plt.legend() 
    plt.show() 

def myfunc(name) :
    dataset = pd.read_csv(name) 
    print("Size of data set :  ",dataset.shape)

    #Head Size(cm^3),Brain Weight(grams)
    X = dataset["Head Size(cm^3)"].values
    Y = dataset["Brain Weight(grams)"].values

    print("Length of X : ",len(X))
    print("Length of Y : ",len(Y))

    slope_intercept = np.polyfit(X,Y,1)

    m = slope_intercept[0]
    c = slope_intercept[1]

    X_start = np.min(X) - 200
    # X_start = 0 
    X_end = np.max(X) + 200
    x = np.linspace(X_start,X_end) 

    y = m*x + c 

    plt.plot(x,y,color = 'r', label='Regression Line')
    plt.scatter(X,Y,color='b') 
    
    plt.xlabel("Head Size")
    plt.ylabel("Brain Weight ")

    plt.legend() 
    plt.show() 


def main() :
    print("Enter file name : ",end=" ") 
    # name = input() 
    name = "HB.csv"
    # marvellousHeadBrain(name) 
    myfunc(name)


if __name__ == "__main__" : 
    main() 

