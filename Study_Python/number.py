def DisplayFactor(no):
    i = 1
    
    print("Factors are :")
    while(i <= int(no/2)):
        if no % i== 0 :
            print(i)
        i = i+1