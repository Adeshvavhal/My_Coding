def Add(*Values):

     sum=0
     for no in Values:
        sum = sum + no

     return sum
   
def main():
    Ans = 0
    Ans =Add(1,7,9,4,6,5)
    print("Addition is",Ans)
if __name__ == "__main__":
    main()