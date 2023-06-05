class Super:
    def __init__(self):
        self._value1 = 100
        self.__value2 = 200

    def display(self):
        print(self._value1)
        print(self.__value2)

class Sub(Super):
    def show(self):
        print(self._value1)
        #print(self.__value2) do not print beacuse value2 is privarte


s = Sub()
s.show()

s1  =Super()
s1.display()
