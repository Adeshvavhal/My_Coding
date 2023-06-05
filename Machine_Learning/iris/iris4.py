from sklearn.datasets import load_iris
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split

def MarvellousKNighborsClassifier():
    Dataset = load_iris()

    Data = Dataset.data
    Target = Dataset.target

    Data_tarin,Data_test,Target_train,target_test = train_test_split(Data,Target,test_size = 0.5)

    classifier = KNeighborsClassifier()

    classifier.fit(Data_tarin,Target_train)

    predictions = classifier.predict(Data_test)

    Accuracy = accuracy_score(target_test,predictions)

    return Accuracy
def main():
    ret = MarvellousKNighborsClassifier()

    print("Accuracy of iris dataset with KNN is ",ret*100)


if __name__=="__main__":
    main()