class Value:
    def __init__(self,Data):

    def SumFactors(self):
        Sum = 0
        for i range(1,self.No):
            if(self.No % i == 0):
                Sum = Sum + 1
        return Sum

    def CheckPerfect(self):
        Ans = self.SumFactors()

        if(self.No ==1):
            return True
        else
        return False

def main():
    print("Please entre number")
    A=int(input())

    obj = Value(A)
    Ret = obj.CheckPerfect()
        if(Ret == True):
            print("{}is a perfect number".format(A))
        else:
            print("{} is not a perfect number".format(A))
if __name__ == "__main__":
        main()