num = int(input("Entre the number : "))
prime = True
for i in range(2,num):
    if (num%1 == 0):
        prime = False
        break
if prime:
    print("this is prime")
else:
    print("this number is not prime")
