
from sklearn.model_selection import train_test_split
from sklearn import datasets
from sklearn.ensemble import AdaBoostClassifier
from sklearn import metrics

iris = datasets.load_iris()
x=iris.data
y=iris.target

x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.3)

abc=AdaBoostClassifier(n_estimators=50,learning_rate=1)

model = abc.fit(x_train,y_train)

y_pred = model.predict(x_test)

print("Accurcuy",metrics.accuracy_score(y_test,y_pred))