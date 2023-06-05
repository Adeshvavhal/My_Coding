class employee:
    company = "google"

    def getSalary(self):
        print(f"Salary  for this employee working in {self.company} is {self.salary}")

def main():

    harry = employee()
    harry.salary = 10000
    harry.getSalary()

if __name__=="__main__" :
    main()
