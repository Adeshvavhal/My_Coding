while (True):
    print("press q to quit")
    a= input("Entre the Number ")

    if a == 'q':
        break

    try:
        a = int(a)

        if a>6:
            print("You entered number grator than 6")

    except Exception as e:
        print(e)

print("Thanks for playing this game")