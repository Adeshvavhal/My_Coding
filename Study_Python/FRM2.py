def CheckEven(No)
    return(No % 2 ==0)

def Doubles(No):
    return No * 2

def sum(A,B):
    return A+B

def reduceX(Helper_Function,Data):
    Ans = 0
    for no in Data:
        Ans = Helper_Function(Ans,No)
    return Ans

def filterX(Helper_Function,Data):
    Result = []
    for No in Data:
        if(Helper_Function(No)==True):
            Result.append(No)
    return Result

def Mapx(Helper_Function,Data):
    Result= []
        for No in Data:
            Value = Helper_Function(No)
            Result.append(Value)
        
        return Result
    ]
def main():
    print("Entre Number of elements you want to elemnet:")
    iSize = int(input())
    
    Data_Input = []
    print("plz entre the data")
    for iCnt in range(0,iSize,1):
        Value = int(input())
        Data_Input.append(Value)
    print("data is :",Data_Input)

    Data_Filter = filterX(CheckEven,Data_Input)

    print("Data after filter is : ",Data_Filter)

    Data_map = mapX(Doubles,Data_Filter)
    print("Data after map is :",Data_Map)

    Output = reduce(sum,Data_Map) 
    print("output :",Output)

if __name__ =="__main__":
    main()