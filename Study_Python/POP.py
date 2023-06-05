def Add(A,B):
    return A+B

def Sub(A,B):
    return A-B
def main ():
    print("Entre first Number")
    No1 = int(input())

    print("entre second number")
    No2 = int(input())

    Ans = Add(No1,No2)
    print(Ans)

    Ans = Sub(No1,No2)
    print(Ans)

if __name__=="__main__":
    main()
