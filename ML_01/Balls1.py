import sklearn
from sklearn import tree

def main():
    # step 1 and 2 --> Get and clean data 
    Features = [
        [35,"Rough"],
        [47,"Rough"],
        [90,"Smooth"],
        [48,"Rough"],
        [90,"Smooth"],
        [35,"Rough"],
        [92,"Smooth"],
        [35,"Rough"],
        [35,"Rough"],
        [35,"Rough"],
        [96,"Smooth"],
        [43,"Rough"],
        [110,"Smooth"],
        [35,"Rough"],
        [95,"Smooth"]
        ]

    Labeles = [
        "Tennis",
        "Tennis",
        "Cricket",
        "Tennis",
        "Cricket",
        "Tennis",
        "Cricket",
        "Tennis",
        "Tennis",
        "Tennis",
        "Cricket",
        "Tennis",
        "Cricket",
        "Tennis",
        "Cricket"
    ]

    # step 3 --> decide alforithm 
    dobj = tree.DecisionTreeClassifier() 

    # step 4 ---> use algo on data 
    dobj.fit(Features,Labeles) 


    # step 5 ---> result 
    result = dobj.predict([[40,1]])
    print(result) 


if __name__ == "__main__":
    main() 