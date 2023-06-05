from sklearn import tree

#load the dataset
#Rough 1
# smooth 0

#Tennis 1
#Cricket 2
def BallPredictor():
    Feature = [[35,1],[47,1],[90,0],[48,1],[90,0],[35,1],[92,0],[35,1],[35,1],[35,1],[96,0],[43,1],[110,0],[35,1],[95,0]]

    Labels =[1,1,2,1,2,1,2,1,1,1,2,1,2,1,2]

    obj = tree.DecisionTreeClassifier()

    obj = obj.fit(Feature,Labels)

    print(obj.predict([[97,0]]))


def main():
    print("-------Ball Predictor Case Study------")

    BallPredictor()

if __name__=="__main__":
    main()