class Person:
    country = "India"
    def  takeBreath(self):
        print("I am breathing")

class Employee :
    company ="honda"

    def getSalary(self):
        print(f"salary is {self.salary}")

    def takeBreath(self):
        print("I am amployee so i am luckly breathing")

class Programmer(Employee):
    company ="Google"

    def getSalary(self):
        print("No salary to programmer")

def main():
    p = Person()
    p.takeBreath()
    e = Employee()
    pr = Programmer()
    




if __name__=="__main__":
    main()
