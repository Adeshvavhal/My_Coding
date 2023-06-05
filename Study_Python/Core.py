import multiprocessing

def main():
    print("NUmber of cores are :",multiprocessing.cpu_count())
if __name__=="__main__":
    main()