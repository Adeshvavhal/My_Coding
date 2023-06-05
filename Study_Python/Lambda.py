
def Add(No1,No2):
    return No1+No2

Addfunction = lambda A,B : A+B

Ans1 = Add(10,11)
Ans2 = Addfunction(10,11)

print("Addition using normalfunction",Ans1)
print("Addition using lambdafunction",Ans2)
print("Type of lambda function is :",type(Addfunction))