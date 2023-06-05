class Complex:
    def __init__(self,r,i) :
        self.real = r
        self.imaginay = i

    def __add__(self,c):
        return Complex(self.real + c.real, self.imaginay + c.imaginay)
    
    def __str__(self) :
        return f"{self.real} + {self.imaginay}i"


c1 = Complex(1,4)
c2= Complex(8,5)
print(c1+c2)
