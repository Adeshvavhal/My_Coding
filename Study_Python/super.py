class Person:
    
    country = "India"
    def takeBreak(self):
        print("I am breathing")

class Employee(Person):
    comapny = "Honda"

    def getSalary(self):
        print(f"salary is {self.salary}")

    def takeBreak(self):
        print("I am an Employee so i am luckly breathing .")

class Programmer(Employee):
    company = "Fiver"

    def getSalary(self):
        print(f"No salary to programer")

    def takeBreak(self):
        super().takeBreak()
        print("I am a programer so i am brathing")

p = Person()
p.takeBreak()

e = Employee()
e.takeBreak()

pr = Programmer()
pr.takeBreak()

