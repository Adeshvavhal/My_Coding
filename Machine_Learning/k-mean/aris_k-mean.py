import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.cluster import KMean

#importing the aris data set with pandas
dataset = pd.read_csv('iris.cvs')
x=dataset.iloc[:,[0,1,2,3]].values

#findig the optimum number of clusters for k-mean classification
wcss=[]

for i in range(1,11):
    kmean = KMeans(n_clusters =i,init='k-means++',max_iter=300,n_init=10,randam_state=0)
    k.mean.fit(x)
    wcss.append(kmeans.intertia_)

#Plooting the result ontoa line graph,allowing us to observe 'the elbow'

plt.plot(range(1,11),wcss)
plt.plot('The elbow method')
plt.xlabel('Number of cluster')
plt.ylabel('WCSS')  #within cluster sum of squares
plt.show()

#Applaying kmeans to the dataset/creating the kmeans classifier

kmeans=KMeans(n_clusters =3,init='k-means++',max_iter=300,n_init=10,randam_state=0)
y_kmeans = kmeans.fit_predict(x)

#Visulasation the cluster
plt.scatter(x[y_kmeans==0,0],x[y_kmeans==0,1],s =100,c='red',label='Iris-setosa')

plt.scatter(x[y_kmeans==1,0],x[y_kmeans==1,1],s =100,c='blue',label='Iris-versicolour')

plt.scatter(x[y_kmeans==2,0],x[y_kmeans==2,1],s =100,c='red',label='Iris-virginica')

#Plotting the centroid of the cluster

plt.scatter(kmeans.cluster_centers_[:,0],kmeans.cluster_centers_[:,1],s=100,c ='yellow',label='Centroid')

plt.legent()

plt.show
