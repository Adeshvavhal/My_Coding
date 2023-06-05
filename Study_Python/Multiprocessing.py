
def DisplyaEven(No):
    for i in range(1,No,1):
        if(i % 2 == 0):
            print("Even Number :",i)

def DisplayOdd(No):
    for i in range(1,No,1):
        if(i % 2 != 0):
            print("Even Number :",i)
def main():
    print("Demonstration of serial programing")
    DisplyaEven(20000)
    DisplayOdd(20000)
   
if __name__== "__main__":
    main()