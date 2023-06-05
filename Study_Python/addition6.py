print("Application to demonstrate Industrial programming")

def Addition(Value1, Value2):
        Ans = Value1 + Value2
        return Ans
       
def main():
        print("Entre first number : ")
        no1 = int(input())
        print("Entre second number :")
        no2 = int(input())
        
        Sum = Addition(no1,no2)  #function call
    
        print("Addition is : ",Sum)
    
if __name__ == "__main__":
 
        main()