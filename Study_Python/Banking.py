
class BanK_Account:

    Bank_Name = "HDFC bank PVT LTD"
    ROI_ON_FD = 6.7
    def __init__(self):
        self.Name=""
        self.Amount=0
        self.Address = ""
        self.AccountNo=0

    def CreateAccount(self):
        print("Entre your name:")
        self.Name = input()

        print("Entre your Amount:")
        self.Amount = int(input())

        print("Entre your Address:")
        self.Addeess = input()

        print("Entre your Account number:")
        self.AccountNo = int(input())

    def DisplyaAccountInfo(self):
        print("Your Account information is a below -----")
        print("Name of aacount Holder :",self.Name)
        print("Account Numberof aacount  Holder :",self.AccountNo)
        print("Address of aacount Holder :",self.Addeess)
        print("Current of aacount Holder :",self.Amount )

    @classmethod
    def DisplyBankInformation(cls):
        print("Wlcome to Banking console")
        print("Name of bank :", cls.Bank_Name)
        print("Rate of intrest on fixed deposit :",cls.ROI_ON_FD)

    @staticmethod
    def DisplayKYCInfo():

        print("KYC Infirmation")
        print("Accordung to the rule of Goverment of india you have to submit below document")
        print("1: Clear and Recebt passport size photo")
        print("2: photo of Adhar card")
        print("3 : Photo of PAN Card")

    def Deposit(self,Value):
        self.Amount = self.Amount + Value

    def Withdraw(slef,Value):
        self.Amount = self.Amount - Value

def main():
    BanK_Account.DisplayKYCInfo()
    print("Name of bank :", BanK_Account.Bank_Name)
    print("Rate of intrest on fixed deposit :",BanK_Account.ROI_ON_FD)

    BanK_Account.DisplyBankInformation

    User1 = BanK_Account()
    User2 =BanK_Account()

    print("Ceating first account")
    User1.CreateAccount()
    print("Ceating second account")
    User2.CreateAccount()

    User1.DisplyaAccountInfo()
    User2.DisplyaAccountInfo()

    User1.Deposit(500)
    User2.Deposit(1200)
    print("Amount of {} after Deposit is {} :".format(User1.Name,User1.Amount))
    print("Amount of {} after Deposit is {} :".format(User2.Name,User2.Amount))

    User1.Withdraw(200)
    User2.Withdraw(3000)
    print("Amount of {} after withraw  is {} :".format(User1.Name,User1.Amount))
    print("Amount of {} after Deposit is {} :".format(User2.Name,User2.Amount))



if __name__ == "__main__":
    main()