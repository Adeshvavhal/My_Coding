
import time
import tread

def DisplyaEven(No):
    for i in range(1,No,1):
        if(i % 2 == 0):
            print("Even Number :",i)

def DisplayOdd(No):
    for i in range(1,No,1):
        if(i % 2 != 0):
            print("odd Number :",i)
def main():
    print("Demonstration of parallel programing using multiple peocessess")
    Number = 200000000

    p1 = multiprocessing.Process(target = DisplyaEven, args =(Number,))
    p2 = multiprocessing.Process(target = DisplayOdd, args =(Number,))
   
    p1.start()
    p2.start()

    p1.join()
    p1.join()

    print("End of main")
if __name__== "__main__":=''
    start_time = time.process_time()
    main()
    end_time = time.process_time()
    print("Excution time is:",end_time - start_time)