
def main():
    try:
        print("Entre the first Number")
        no1 = int(input())

        print("Entre the second  Number")
        no2 = int(input())
    
        Ans = no1/no2
        print(Ans)
    except ZeroDivisionError:
        print("Exception ocured")

    except ValueError:
        print("Value Error")
    finally:
        print("Inside finally block")
if __name__=="__main__":
    main()