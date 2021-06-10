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
    print("I(nside user defined IMplementation : ")
    iris = load_iris() 
    data = iris.data 
    target = iris.target 
    data_train , data_test , target_train , target_test = train_test_split(data,target,test_size=0.50)

    print("dataset loaded successfully ;)" ) 

    mobj = Marvellous() 

    mobj.fit(data_train,target_train)  
    ret = mobj.preditct(data_test)  

    print("result is : " , ret )
    accuracy = accuracy_score(target_test,ret) 
    return accuracy 


def main() :
    ret = marvellousKNN() 
    print(f"accuracy of KNN is {ret*100} % ")


if __name__ == "__main__" : 
    main()


