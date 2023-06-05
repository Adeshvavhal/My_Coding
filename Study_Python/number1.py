class Numbers:
    def __init__(self):
        self.Size = 0
        self.Arr = list()
    def Accept(self):
        print("How many element you want :")
        self.Size= int(input())

        print("please entre the element")
        Value = 0
        for i in range(0,self.Size):
            Value = int(input())
            self.Arr.append(Value)
    
    def Display(self):
            print("Element from list are:")
            for i in range(0,self.Size):
                print(self.Arr[i])

    def Summation(self):
        sum = 0
        for i in range(0,self.Size):
            sum = sum + self.Arr[i]
        return sum
def main():
    obj = Numbers()
    obj.Accept()
    obj.Display()

    Output = obj.Summation()
    print("Summation of element is :")
if __name__ == "__main__":
        main()