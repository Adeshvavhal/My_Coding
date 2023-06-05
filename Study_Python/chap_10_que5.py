class Train :
    def __init__(self,name,fare,seats):
        self.name= name
        self.fare = fare
        self.seats = seats

    def getStatus(self):
        print(f"the name of train is {self.name}")
        print(f"the seat avalable in the train are {self.seats}")

    def fareInfo(self):
        print(f"the price of the ticket is {self.fare}")

    def bookTicket(self):
        if(self.seats>0):
            print(f"your ticket has been booked! your seat number is {self.seats}")
            self.seats = self.seats -1
        else:
            print("Sorry this train is full! kindly try in tatkal")


    
def main():

    intercity = Train("Intercity Express :14015",90,300)

    intercity.getStatus()
    intercity.fareInfo()
    intercity.bookTicket()
    intercity.getStatus()
    intercity.bookTicket()
    intercity.getStatus() 
    intercity.bookTicket()
    intercity.getStatus()


if __name__=="__main__":
    main()
