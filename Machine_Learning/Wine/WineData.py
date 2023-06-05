from sklearn import metrics
from sklearn import datasets
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split

def WinePredictor():
    #load Dataset
    wine = dataset.load_wine()

    print("The name of the features")
    print(wine.feature_names)

    print("the label species")
    print(wine.target_name)

    print(" veiw the 5 entirs from loading data set")
    print(wine.data[0:5])
    
    print("print the wine label")
    print(wine.target)

    #spilt the data 
    X_train,X_test,Y_train,Y_test = train_test_split(wine.data,wine.target,test_size = 0.3)

    #create KNN classifier
    knn = KNeighborsClassifier(n_neighbors=3)

    #tain the model using the traning sets
    knn.fit(X_train,Y_train)

    #Predict the response for the traing data set
    y_pred=knn.predict(X_test)

    #Model Accuracy,how often is the classifier correct
    print("Accuracy:",metrics.accuracy_score(Y_test,y_pred))
def main():
    print("----Marvellous Infosystem by Adesh Vavhal---")

    print("Machine learning Application")

    print("wine predictor applicaion using K Nearest Knighbor Algorithm")

    WinePredictor()

if __name__=="__main__":
    main()