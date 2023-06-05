print("Demonstration of list")

#Data : Hetrogenous
#Ordered : Yes
#Indexed :yes
#mutable : no
#Duplicates : yes

data = (11,21,51,101,21,11)
data1 = (11, 90.80, True, "Hello")

print("Data at hetrogenous :",data1)
print("Data at ordered :",data1)
print("Data at index 2 :",data[2])
print("Data with duplication :",data)

print("List is mutable")

data.append(201)
data.pop()

print("Data after append : ",data)
data.pop()
