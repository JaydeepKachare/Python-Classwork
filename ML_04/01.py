import pandas as pd

def main() :
    data = pd.read_csv("./iris.csv")
    # print(data)
    print(data.head(n=10))



if __name__ == "__main__" : 
    main() 