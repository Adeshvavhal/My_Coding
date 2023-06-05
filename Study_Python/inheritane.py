class Employee:
    company = "Google"

    def showDetails(self):
        print("this is employee")

class Programmer(Employee):
    language ="Python"

    def getLanguage(self):
        print(f"The language is {self.language}")


e = Employee()
e.showDetails()
p = Programmer()
p.showDetails()
print(p.company)