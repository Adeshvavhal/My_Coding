class Programer:
    company = "Microsoft"
    def __init__(self,name,product):
        self.name = name
        self.product = product

    def getInfo(self):
        print(f"The name of the {self.company}programer is {self.name} and the product is {self.product}")


def main():
    harry = Programer("harry","skype")
    adesh = Programer("Adesh","Github")
    harry.getInfo()
    adesh.getInfo()



if __name__=="__main__":
    main()