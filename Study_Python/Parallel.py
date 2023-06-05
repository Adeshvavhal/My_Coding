import os
import multiprocessing

def Square(No):
    print("PID of worker processcis {} for input{}".format(os.getpid(),No))
    return (No*No)


def main():
    print("Process id our application :",os.getpid())
    Data =[1,2,3,4,5]
    Result=[]

    pobj = multiprocessing.Pool()
    Result = pobj.map(Square,Data)

    print("Result after opration is",Result)

if __name__=="__main__":
    main()