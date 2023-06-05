class Animal:
    animalType = "Mammal"

class Pets:
    color = "White"

class Dog:
    @staticmethod
    def barK():
        print("Bow Bow!")

def main():
    d = Dog()
    d.barK()


if __name__=="__main__":
    main()