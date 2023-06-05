def main():
    print("Entre number :")
    no = int(input())
    
    i = 1
    
    print("Factors are :")
    while(1 <= int(no/2)):
        if no % i== 0 :
            print(i)
        i = i+1
if __name__ == "__main__":
    main()
