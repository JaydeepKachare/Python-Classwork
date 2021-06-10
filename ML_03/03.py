from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn import tree 
from sklearn.metrics import accuracy_score
from sklearn.neighbors import KNeighborsClassifier

def marvellousDecision(data_train , data_test , target_train , target_test) : 
    cobj = tree.DecisionTreeClassifier() 
    cobj.fit(data_train,target_train) 
    result = cobj.predict(data_test) 
    accuracy = accuracy_score(target_test,result)
    return accuracy 


def marvellousKNN(data_train , data_test , target_train , target_test ) : 
    cobj = KNeighborsClassifier ()  
    cobj.fit(data_train,target_train) 
    result = cobj.predict(data_test) 
    accuracy = accuracy_score(target_test,result)
    return accuracy 


def main() :
    dataset = load_iris() 
    data = dataset.data
    target = dataset.target 
    data_train , data_test , target_train , target_test = train_test_split(data,target,test_size=0.50)

    ret = marvellousDecision(data_train , data_test , target_train , target_test ) 
    print(f"Accuracy : {ret*100} %" )

    ret = marvellousKNN(data_train , data_test , target_train , target_test )  
    print(f"Accuracy : {ret*100} %" )


if __name__ == "__main__" : 
    main() 


