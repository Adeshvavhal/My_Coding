

    
def main():
    print("Entre Number of elements you want to elemnet:")
    iSize = int(input())
    
    Data_Input = []
    print("plz entre the data")
    for iCnt in range(0,iSize,1):
        Value = int(input())
        Data_Input.append(Value)
    print("data is :",Data_Input)

    Data_Filter = filter((lambda No:(No % 2 == 0)),Data_Input)

    print("Data after filter is : ",Data_Filter)

    Data_Map = list(map((lambda No : No*2),Data_Filter))
    print("Data after map is :",Data_Map)

    Output = reduce( ( lambda A,B : A+B),Data_Map) 
    print("output :",Output)

if __name__ =="__main__":
    main()