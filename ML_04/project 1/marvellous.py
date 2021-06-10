from my_modules import * 

def CalculateDistance(X,Y) :
    return distance.euclidean(X,Y) 

class Marvellous :

    def fit(self, trainingData, trainingTarget) :
        self.trainingData = trainingData
        self.trainingTarget = trainingTarget 



    def preditct(self, TestData) : 
        predictions = [] 
        for row in TestData : 
            label = self.Shortest(row) 
            predictions.append(label)
        return predictions


    def Shortest(self,row) : 
        mindist = CalculateDistance(row,self.trainingData[0])
        minindex = 0 

        for i in range(1,len(self.trainingData)) : 
            dist = CalculateDistance(row,self.trainingData[i])
            if dist < mindist : 
                mindist = dist 
                minindex = i 
            
        return self.trainingTarget[minindex] 



def marvellousKNN() :
    line = "*"*40 
    print("Inside user defined Implementation : ")
    iris = load_iris() 
    data = iris.data 
    target = iris.target 
    data_train , data_test , target_train , target_test = train_test_split(data,target,test_size=0.50)

    print("dataset loaded successfully ;)" ) 

    print("Training dataset : ") 
    for i in range(0,len(data_train) ) :
        print(f"data : {data_train[i]}  Label : {target_train[i]} "    ) 
    print(line)

    print("Test dataset : ") 
    for i in range(0,len(data_test) ) :
        print(f"data : {data_test[i]}  Label : {target_test[i]} "    ) 
    print(line)

    mobj = Marvellous() 

    mobj.fit(data_train,target_train)  
    ret = mobj.preditct(data_test)  


    counter = 0 ;
    for i in range(0,len(data_test) ) :
        print(f"Id : {i}  Expectation : {target_test[i]} Predicted : {ret[i]}  "    ) 
        if target_test[i] == ret[i ] : 
            counter += 1 
    print(line)

    print(f"Total tests : {len(data_test)}")
    print(f"Correct predictions : {counter}")
    print(f"Wrong predictions : {len(data_test) - counter}")
    print(line)

    print(f"Manual accuracy : {counter/len(data_test)*100} % ")
    # print("result is : " , ret )
    accuracy = accuracy_score(target_test,ret) 
    return accuracy 


def main() :
    ret = marvellousKNN() 
    print(f"accuracy of KNN is {ret*100} % ")


if __name__ == "__main__" : 
    main()


