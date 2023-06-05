import os

def main():
    print("PID  current:",os.getpid())
    print("PID parent :",os.getppid())

if __name__=="__main__":
    main()