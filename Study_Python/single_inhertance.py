class Empoyee:
    company ="Google"

    def showDetails(self):
        print("this is an employe")

class Programmer(Empoyee):
    language = "python"
    def getLanguage(self):
        print(f"the language is {self.language}")

    

def main():

    e=Empoyee()
    e.showDetails()
    p=Programmer()
    p.showDetails()

if __name__=="__main__":
    main()


