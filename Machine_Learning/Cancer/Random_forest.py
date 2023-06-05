
#Required python package

import pandas as pd
from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier

#file path

INPUT_PATH ="breast-cancer-wisconsin.data"
OUTPUT_PATH ="breast-cancer-wisconsin.csv"

#Headers

HEADERS = ["CodeNumber","ClumpThickness","UniformityCellSize","UnformityCellShape","MarginalAdhesion","SingleEpithe;ialCellSize","BareNuclei","BlandChromatin","NormalNucleoli","Mitoses","CancerType"]

#########################
#Functon name:read_data
#Description : read the data into pandas dataframe
#input:path of CSV file
#output:Give the data
#Autor :Adesh Raghunath vavhal
#Date :14/01/2023
#########################

def read_data(path):
    data=pd.read_csv(path)
    return data

##############################
#Functon name:get_headers
#Description : dataset header
#input:dataset
#output:Return the header
#Autor :Adesh Raghunath vavhal
#Date :14/01/2023
##############################

def get_headers(dataset):
    return dataset.columns,values

###############################
#Functon name:add_header
#Description : add the header to the dataset
#input:dataset
#output:updated dataset
#Autor :Adesh Raghunath vavhal
#Date :14/01/2023
###########################

def add_header(dataset,headers):
    dataset.coumns = Headers
    return dataset

###############################
#Functon name:data_file_to_csv
#Description : save the data
#input:nothing
#output:write the data to CSV
#Autor :Adesh Raghunath vavhal
#Date :14/01/2023
###########################

def data_file_to_csv():
    #headers
    headers= ["CodeNumber","ClumpThickness","UniformityCellSize","UnformityCellShape","MarginalAdhesion","SingleEpithe;ialCellSize","BareNuclei","BlandChromatin","NormalNucleoli","Mitoses","CancerType"]

    #load the data into pandas data frame
    dataset =read_data(INPUT_PATH)
    #Add the headers to the loaded dataset
    dataset = add_header(dataset,headers)
    #Save the loaded dataset into csv format
    dataset.to_csv(OUTPUT_PATH,index = False)
    print("File Saved...!")

###############################
#Functon name:split_dataset
#Description : split the dataset with the traning percentage
#input:dataset with the related information
#output:dataset after spliting
#Autor :Adesh Raghunath vavhal
#Date :14/01/2023
###########################

def split_dataset(dataset,train_percentage,feature_headers,target_header):
    #Split dataset into train and test dataset
    train_x,train_y,test_x,test_y=train_test_split(dataset[feature_headers],dataset[target_header],train_size=train_percentage)
    return train_x,train_y,train_x,test_y

###############################
#Functon name:handel_missing_values
#Description : filter missing valuesfrom the dataset
#input:Dataset with the missing value
#output:dataset removing  missing value
#Autor :Adesh Raghunath vavhal
#Date :14/01/2023
###########################

def handel_missing_values(dataset,missing_values_header,missing_label):
    return dataset[dataset[missing_values_header]!=missing_label]

########################
#Functon name:random_forest_classifier
#Description : To train the random forest classifier with feature and target data
#Autor :Adesh Raghunath vavhal
#Date :14/01/2023
#########################

def random_forest_classifier(features,target):
    clf=RandomForestClassifier()
    clf.fit(features,target)
    return clf

###############################
#Functon name:dataset_statistic
#Description : Basic statistic of the dataset
#input:Dataset 
#output:Description of dataset
#Autor :Adesh Raghunath vavhal
#Date :14/01/2023
###########################

def dataset_statistics(dataset):
    print(dataset.describe())

#########################
#Functon name:main
#Description : main Function from where execution starts
#Autor :Adesh Raghunath vavhal
#Date :14/01/2023
#########################

def main():
    #Load the Csv file into pandas dataframe
    dataset=pd.read_csv(OUTPUT_PATH)

    #Get basic statistic of the loaded dataset
    dataset_statistics(dataset)

    #Filter missing values
    dataset = handel_missing_values(dataset,HEADERS[6],'?')

    tarin_x,test_x,train_y,test_y=split_dataset(dataset,0.7,HEADERS[1:-1],HEADERS[-1])

    #Train and test dataset size details
    print("Train_x shape::",train_x.shape)
    print("Train_y shape::",train_y.shape)
    print("Test_x shape::",test_x.shape)
    print("Test_y shape::",test_y.shape)

    #Create Random forest classifier instance
    trained_model = random_forest_classifier(train_x,train_y)
    print("Trained model ::",trained_model)
    predictions = trained_model.predict(test_x)

    for i in range(0,205):
        print("Actual outcome::{}and Predicted Outcome ::{}".format(list(test_y)[i],predictions[i])) 

    print("Train Accuracy::",accuracy_score(train_y,trained_model.predict(train_x)))
    print("Test Accuracy::",accuracy_score(test_y,prediction))
    print("Confusion matrix",confusion_matrix(test_x,predictions))

#Application stater
if __name__=="__main__":
    main()