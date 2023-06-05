class Calculater:
    def __init__(self,num):
        self.number = num

    def square(self):
        print(f"the value of {self.number} square {self.number**2}")

    def squreRoot(self):
        print(f"the value of {self.number} square {self.number**0.5}")
        
    def cube(self):
        print(f"the value of {self.number} square {self.number**3}")
        

def main():
    a = Calculater(9)
    a.square()
    a.squreRoot()
    a.cube()

if __name__=="__main__":
    main()
