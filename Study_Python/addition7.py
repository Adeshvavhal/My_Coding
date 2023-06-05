print("Application to demonstrate Industrial programming")

import AdeshModule      
       
def main():
        print(Value of  __name__ from main is : ",__name__)
        print("Entre first number : ")
        no1 = int(input())
        print("Entre second number :")
        no2 = int(input())
        
        Sum = AdeshModule.Addition(no1,no2)
    
        print("Addition is : ",Sum)
    
if __name__ == "__main__":
 
        main()