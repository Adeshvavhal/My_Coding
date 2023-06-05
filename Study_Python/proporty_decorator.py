class Employee:
    company = "Bhart Gas"
    salary = 4500
    salarybonus = 500


    @property
    def totalSalary(self):
        return self.salary + self.salarybonus
    
    @totalSalary.setter
    def totalSalary(self,val):
        self.salarybonus = val-self.salary
    

def main():
    e = Employee()
    print(e.totalSalary)
    e.totalSalary = 5800
    print(e.salary)
    print(e.salarybonus)




if __name__=="__main__":
    main()
