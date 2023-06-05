
def Demo1():
    print("Inside Demo1")

def Demo2(No):
    print("inside Demo2 with argument : ",No)

def Demo3(No):
    print("inside Demo3 with argument",No)
    return No+2

def Demo4(No1,No2):
    print("inside Demo4")
    Add=No1+No2
    return Add

def Demo5(No1,No2):
    print("inside Demo2")
    Add = No1 + No2
    Sub = No1 - No2
    return Add,Sub 

def main():
    Demo1()
    Demo2(11)
    Ans = Demo3(10)
    print("return value of Demo3 is:",Ans)
    Ans = Demo4(10,11)
    print("return value of Demo4 is:",Ans)
    Ans1,Ans2=Demo5(11,10)
    print("return value of Demo5 is:",Ans1)
    print("return value of Demo5 is:",Ans2)
    
if __name__ == "__main__":
    main()