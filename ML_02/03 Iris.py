from sklearn.datasets import load_iris
import numpy as np
from sklearn import tree


def main():
    dataset = load_iris()
    print("Features of dataset : ")
    print(dataset.feature_names)
    print("Target names of dataset : ")
    print(dataset.target_names)

    index = [1, 51, 101]
    test_target = dataset.target[index]
    test_feature = dataset.data[index]

    train_target = np.delete(dataset.target, index)
    train_feature = np.delete(dataset.data, index, axis=0)

    # 1 2 : collect and clean data 
    # 3 : select algorithm 
    obj = tree.DecisionTreeClassifier()

    # 4 : train data 
    obj.fit(train_feature, train_target)

    # 5 : test data  
    result = obj.predict(test_feature)

    print("Result predection by Algorithm : ", result)
    print("Result Expected                : ", test_target)


if __name__ == "__main__":
    main()
