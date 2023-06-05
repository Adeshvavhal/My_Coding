class Employee:
    company  = "Visa"
    eCode = 120
class Freeleancer:
    company = "Fiverr"
    level = 0
    def upgradeLevel(self):
        self.level = self.level+1
class Programmer(Employee,Freeleancer):
    name = "Rohit"

p = Programmer()
print(p.company)