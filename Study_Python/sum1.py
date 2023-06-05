class Number:
    def sum(self):
        return self.a +self.b

def main():

    num = Number()
    num.a = 12
    num.b = 34
    s = num.sum()
    print(s)

if __name__=="__main__":
    main()