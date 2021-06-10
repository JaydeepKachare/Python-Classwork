import pandas as pd 
import numpy as np 
from sklearn.linear_model import LinearRegression

def marvellous(name) : 
    dataset = pd.read_csv(name) 
    print("Size of data set : ",dataset.shape)
    
    X = dataset["Head Size(cm^3)"].values
    Y = dataset["Brain Weight(grams)"].values
    X = X.reshape((-1,1))
    obj = LinearRegression() 
    obj.fit(X,Y) 

    output = obj.predict(X) 

    rsquare = obj.score(X,Y)
    print(rsquare)


def main() : 
    marvellous("HB.csv")


if __name__ == "__main__" : 
    main() 