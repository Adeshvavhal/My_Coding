import time

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
    DisplyaEven(2000)
    DisplayOdd(2000)
   
if __name__== "__main__":
    start_time = time.process_time()
    main()
    end_time = time.process_time()
    print("Excution time is:",end_time - start_time)