def main():
    print("Entre number :")
    no = int(input())
    
    print("Factors are :")
    for i in range(1,no,1):
        if no % i == 0:
            print(i)
      
if __name__ == "__main__":
    main()