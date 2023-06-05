def CheckEven(No):
    if(No%2 == 0):
        return True
    else:
        return False
if CheckEvenX(No):
    return (No % 2 == 0)

Ret = CheckEven(12)

if(Ret==True):
    print("its even")
else:
    print("its odd")