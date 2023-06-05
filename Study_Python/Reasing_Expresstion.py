def increment (num):
    try:
        return int(num)+1
    except:
        raise ValueError("This is not good- Adesh")
    
a = increment('df364')
print(a)