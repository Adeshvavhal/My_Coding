from abc import ABC,abstractclassmethod

class Car(ABC):
    @abstractclassmethod
    def mileage(self):
        pass
    def color(self):
        print("White")

class Maruti_Suzuki(Car):
    def mileage(self):
        print("mileage is 30 kmph")


class TATA(Car):
    def mileage(self):
        print("mileage is 35 kmph")

class Duster(Car):
    def mileage(self):
        print("mileage is 40 kmph")


m1=Maruti_Suzuki()
t1 = TATA()
d1 =Duster()
m1.mileage()
t1.mileage()
d1.mileage()