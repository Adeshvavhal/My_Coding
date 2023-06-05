class employee:
    company = "google"

    def getSalary(self,signature):
        print(f"Salary  for this employee working in {self.company} is {self.salary}\n {signature}")

    @staticmethod
    def greet():
        print("Good Morining sir....")

def main():

    harry = employee()
    harry.greet()

    harry.salary = 10000
    harry.getSalary("Thanks!")
    
   
if __name__=="__main__" :
    main()
