import numpy as np 
import pandas as pd 
from sklearn import preprocessing 
from sklearn.neighbors import KNeighborsClassifier

def MarvellousPlayPredictor(data_path):

    data =pd.read_csv(data_path,index_col=0)

    print("Size of Actual dataset",len(data))

    feature_name =['Whether','Tempreature']

    print("Name of features",feature_name)

    whether = data.Whether
    Tempreature = data.Tempreature
    play = data.play

    #creating labelEcoding
    le =preprocessing.LabelEncoder()

    #converting string label into number

    waether_encoded=le.fit_transform(whether)
    print(waether_encoded)

    temp_encoded =le.fit_transform(Tempreature)
    print(temp_encoded)

    #combing weather and temp into single list of tuples
    features=list(zip(waether_encoded,temp_encoded))

    model = KNeighborsClassifier(n_neighbors=3)

    model.fit(features,label)

    predicted =model.predict([[0,2]])

    print(predicted)

def main():
    print("---Marvellous Infosystem by Adesh Vavhal----")

    print("Machine learning application")

    print("Play predictor application by using K Nearest Knighbor algorithm")

    MarvellousPlayPredictor("playPredictor.csv")


if __name__=="__main__":
    main()