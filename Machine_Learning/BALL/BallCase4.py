from sklearn import tree

#load the dataset
#Rough 1
# smooth 0
#Tennis 1
#Cricket 2
def BallPredictor(weight,surface):
    Feature = [[35,1],[47,1],[90,0],[48,1],[90,0],[35,1],[92,0],[35,1],[35,1],[35,1],[96,0],[43,1],[110,0],[35,1],[95,0]]

    Labels =[1,1,2,1,2,1,2,1,1,1,2,1,2,1,2]

    obj = tree.DecisionTreeClassifier()

    obj = obj.fit(Feature,Labels)

    print(obj.predict([[weight,surface]]))

    if ret=1:
        print("your object look like a Tennis ball")
    else:
        print("your object look like a Cricket ball")


def main():
    print("-------Ball Predictor Case Study------")

    print("please Entre the wight of your object in geams")
    weight = int(input())

    print("Please entre the type of surface of your object (Rough/Smooth)")
    surface = input()
    if surface.lower()=="rough":
        surface =1
    elif surface.lower()=="smooth":
        surface =0
    else:
        print("Invalid type surface")
    BallPredictor(weight,surface)

if __name__=="__main__":
    main()