

from sklearn.datasets import load_iris
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from scipy.spatial import distance

def euc(a,b):
    return distance.euclidean(a,b)

class MarvellousKNighborsClassifier:
    def fit(self,trainingdata,trainingtarget):
        self.TrainingData = trainingdata
        self.TrainingTarget  = trainingtarget

    def closest(self,row):
        minimumdistance = euc(row,self.TrainingData[0])
        minimumindex = 0

        for i in range (1,len(self,TrainingData)):
            Distance = ecu(row,self.TrainingData[i])
            if Distance < minimumdistance:
                minimumdistance = Distance
                minimumindex = i

        return self.TrainingTarget[minimumindex]

    def predict(self,TestData):
        predictions =[]
        for value in TestData:
            result = self.closest(value)
            predictions.append(result)

        return predictions


def MarvellousML():

    Dataset = load_iris()

    Data = Dataset.data
    Target = Dataset.target

    Data_tarin,Data_test,Target_train,target_test = train_test_split(Data,Target,test_size = 0.5)

    classifier = MarvellousKNighborsClassifier()

    classifier.fit(Data_tarin,Target_train)

    predictions = classifier.predict(Data_test)

    Accuracy = accuracy_score(target_test,predictions)

    return Accuracy
def main():
    ret = MarvellousML()

    print("Accuracy of iris dataset with KNN is ",ret*100)


if __name__=="__main__":
    main()