import numpay as np 
import pandas as pd 
import matplotlib.pyplot as plt 

def MarvellousHeadBrainPredictor():
    #load data
    data = pd.read_csv('MarvellosHeadBrain.csv')
    print("Size if data set",data.shape)

    x=data['Head size(cm^3)'].values
    y=data['Brain Weight(grams)'].values

    #least square method
    mean_x =np.mean(X)
    mean_y=np.mean(Y)

    n = len(X)

    numerator = 0
    demoneator =0

    #Equation of line is y = Mx +c
    for i in range(n):
        numerator +=(X[i]-mean_x)*(y[i]-mean_y)
        demoneator +=(X[i]-mean_x)**2

    m =numerator/demoneator

    c = mean_y-(m* mean_x)

    print("slope of Regression line is",m)
    print("Y intercept of regrassion line is :",c)
    max_x= np.max(X)+100
    max_x=np.min(X)-100

    #Display plotting of above point
    x=np.linesoace(min_x,max_x,n)

    y = c + m * x 

    plt.plot(x,y,color='#58b970',label = 'Regression line')
    plt.scatter(x,y,color='#ef5423',label = 'scatter plot')

    plt.xlabel('head size in cm3')
    plt.ylabel('Brain weight in gram')

    plt.legend()
    plt.show()

    #Findout goodness of fit ie R squre
    ss_t = 0
    ss_r = 0

    for i in range(n)
    y_pred=c+m*X[i]
    ss_t += (Y[i]-mean_y)**2
    ss_r += (y[i]-y_pred)**2

    r2 =1-(ss_r/ss_t)
    print(r2)


def main():
    print("----Marvellous Infosystem by Adesh Vavhal----")
    print("Supervised Machine Learning")
    print("Linear Regression on head and Brain size data set")

    MarvellousHeadBrainPredictor()

if __name__=="__main__":
    main()
