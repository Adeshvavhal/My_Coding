
def Add(A,B):
    return A+B

def Sub(A,B):
    return A-B

def Caluclator(Target,Value1,Value2):
    return Target(Value1,Value2)

Ret =Caluclator(Target =Add,Value1=10,Value2=11)
print("Addition is :",Ret)

Ret =Caluclator(Target =Sub,Value1=10,Value2=11)
print("Subsrtaction is :",Ret)

