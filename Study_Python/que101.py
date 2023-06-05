class Programmer:
    company = "Microsoft"

    def __init__(self,name,product):
        self.name = name
        self.product = product

    def getOInfo(self):
        print(f"The  name of the {self.company}of programmer is {self.name} and the product is {self.product}")
def main():
    harry = Programmer("Harry","Skype")
    alka = Programmer("Alka","Github")
    harry.getOInfo()
    alka.getOInfo()
if __name__=="__main__":
    main()
    
