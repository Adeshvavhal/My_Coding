from sklearn import dataset 
from sklearn.model_selection from train_test_split
from sklearn import svm
from sklearn import metrics

def MarvellousSVM():
    #load dataset
    cancer =datasets.load_breast_cancer()

    #print the name of the 13 features
    print("Featurea of the cancer :",cancer.feature_names)

    #print the label type of cancer('malignant','benign')
    print("Label of the cancer dataset",cancer.target_names)

    #print data (feature) shape
    print("Shape of dataset is ",cancer.data.shape)

    #print the cancer data feature (top 5 record)
    print("First 5 record are:")
    print(cancer.data[0.5])

    #print cancer label (0:malignant,1:benign)
    print("target of dataset:",cancer.target)

    #spilt the dataset into traning set and test set
    x_train,x_test,y_train,y_test=train_test_split(cancer.data,cancer.target,test_size=0.3,random_state=109)

    #Create the svm classifier
    clf = svm.SVC(kernel ='liner')

    #tarin the model using the traing set 
    clf.fit(x_train,y_train)

    #predict the response for the dataset
    y_pred = clf.predict(x_test)

    #model Accuracy how often is the classifier coreect
    print("Accuracy of the model is :",metrics.accuracy_score(y_test,y_pred)*100)

def main():
    print("---Marvellous Super vector machine----")

    MarvellousSVM()

if __name__=="__main__":
    main()
