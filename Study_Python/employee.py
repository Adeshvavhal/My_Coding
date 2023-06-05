class Employee:
    company = "Google" ####class 



def main():

    harry = Employee()
    rajni = Employee()
    print(harry.company)
    print(rajni.company)
    Employee.company ="youtube"
    print(harry.company)
    print(rajni.company)


if __name__=="__main__":
    main()