import math
import numpy as np 
import pandas as pd 
import seaborn as sns
from seaborn import countplot
import matplotlib.pyplot as plt 
from matplotlib.pyplot import figure,show
from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix
from sklearn.metrics import classification_report
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression

def MarvellousTitanicLogistic():
    titanic_data =pd.read_csv('MarvellousTitanicDataset.cvs')   # step-1 : load the data

    print("First 5 entres from loaded data")
    print(titanic_data.head())

    print("Number of passanger are"+str(len(titanic_data)))

       #step 2 : Analuze data
    print("Visualisation: Survived and non survied passangers")
    figure()
    traget = "Survived"

    countplot(data=titanic_data,x=target).set_title("marvellous infosystem :survived and non survived passangers")
    show()

    print("Visulasation : Survived and non survived passangers based on Gender")
    figure()
    traget ="Survived"

    countplot(data = titanic_data,x=target,hue="Sex").set_title("Marvellous infosystem: survived and non survived passangers based on gender")
    show()

    print("Visulasation : survived and non survived passangers baseb on passanger class")
    figure()
    target="Survied"

    countplot(data=titanic_data,x=target,hue="Pclass").set_title("Marvelous Infosystem : Survived and non survived passangers base on pansanger class")
    show()

    print("Visulasation : survived and non survived passangers baseb on Age")
    figure()
    titanic_data["Age"].plot.hist().set_title("Marvellous Infosystem: survied and non survived passangers base on Age")
    show()

    print("Visulasation : survived and non survived passanger baseb on Fare")
    figure()
    titanic_data["Fare"].plot.hist().set_title("Marvellous Infosystem: survived and non survived passanger based on Fare")
    show()

    #step 3 Data Cleaning
    titanic_data.drop("zero",axis=1,inplace =True)

    print("Fist 5 entries from loaded dataset after removing zero colums")
    print(titanic_data.head(5))

    print("values of sex column")
    print(pd.get_dummies(titanic_data["Sex"]))

    print("values of sex column after removing on filed")
    Sex=pd.get_dummies(titanic_data["Sex"],drop_first=True)
    print(Sex.head(5))

    print("Values of data set after removinf one filed")
    titanic_data=pd.get_dummies(titanic_data["Pclass"],drop_first=True)
    printa(Pclass.head(5))

    print("Values of data set after concatenating new columns")
    titanic_data=pd.concat([titanic_data,Sex,Plass],axis=1)
    print(titanic_data.head(5))

    print("Data after removing irrelevnt columns")
    titanic_data.drop(["Sex","sibsp","Parch","Embarked"],axis =1,inplace=true)
    print(titanic_data.head(5))

    x = titanic_data.drop("Survived",axis =1)
    y = titanic_data["Survived"]

    #step 4: data traning
    xtrain,xtest,ytrain,ytest=train_test_split(x,y,test_size=0.5)

    logmodel= LogisticRegression()

    logmodel.fit(xtrain,ytrain)

    #step data testing
    prediction = logmodel.predict(xtest)

    #step 5 calaculate the accuracy
    print("Classification report of logistic Regression is:")
    print(classification_report(ytest,prediction))

    print("Confusion matrix of logistic Regression:")
    print(confusion_matrix(ytest,prediction))

    print("Accuracy of logistic regression is:")
    print(accuracy_score(ytest,prediction))


def main():
    print("----Marvellous Infosystem by Adesh Vavhal----")
    print("Supervised Machine Learning")
    print("Logistic Regression on Titanic Data set")

    MarvellousTitanicLogistic()

if __name__ =="__main__":
    main()
