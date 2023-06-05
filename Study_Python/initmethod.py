class employee:
    company = "google"

    def __init__(self,name,salary,subunit):
        self.name =name 
        self.salary = salary
        self.subunit = subunit
        print("Employee is created")

    def getDetail(self):
        print(f"The name of employee is {self.name}")
        print(f"The salary of employee is {self.salary}")
        print(f"The subunit of employee is {self.subunit}")
        
    def getSalary(self,signature):
        print(f"Salary  for this employee working in {self.company} is {self.salary}\n {signature}")

    @staticmethod
    def greet():
        print("Good Morining sir....")

def main():

    harry = employee("Adesh",500,"youtubes")
    harry.getDetail()
    
   
if __name__=="__main__" :
    main()
