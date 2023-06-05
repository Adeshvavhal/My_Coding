comment = input("Entre the text\n")
if("make a lot of money" in text):
    spam = True
elif("bye now" in text):
    spam = True
elif("click this" in text):
    spam = True
elif("subscribe this" in text):
    spam =True
else:
    spam =False

if (spam):
    print("this text is spam")
else:
    print("this text is not spam")


