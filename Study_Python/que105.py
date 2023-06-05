class Train:
    def __init__(self,name,fare,seats):
        self.name = name
        self.fare = fare
        self.seats =seats
    def getStatus(self):
        print(f"the name of the tarin is {self.name}")
        print(f"the seats avalable in the train are {self.seats}")

    def fareInfo(self):
        print(f"the price of the ticket is :Rs {self.fare}")

    def bookTicket(self):
        if(self.seats >0):
            print(f"Your ticket has been booked your seat number is {self.seats}")
            self.seats = self.seats - 1
        else:
            print("Sorry this train is full kindly try in tatkal")
def main():
    intercity = Train("Intercity Express:14015",90,2)
    intercity.getStatus()
    intercity.fareInfo()
    intercity.bookTicket()
    intercity.getStatus()
    intercity.bookTicket()
    

if __name__=="__main__":
    main()