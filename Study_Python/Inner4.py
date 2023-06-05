
def Subsrtaction(No1,No2):
    Ans = 0
    Ans =No1 - No2
    return Ans

def Decorated_Function(Function_Name):
    def Inner(A,B):
        if(A<B):
            A,B =B,A 
        Outer =Function_Name(A,B)
        return Outer
    return Inner
def main():
    Value1 = int(input("Entre first number : "))
    Value2 = int(input("Entre seond number : "))
   
   
    New_Function = Decorated_Function(Subsrtaction)
    ret = New_Function(Value1,Value2)
    print("Subsstraction is :",ret)

if __name__=="__main__":
    main()

