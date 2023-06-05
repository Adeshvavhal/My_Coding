class Employe:
    company = "Google"
    salary = 100
harry = Employe()
rajni = Employe()
harry.salary = 300
rajni.salary = 400
print(harry.company)
print(rajni.company)

Employe.company = "YouTube"
print(harry.company)
print(rajni.company)
print(harry.salary)

print(rajni.salary)





