print("Demonstration of Set")

#Data : Hetrogenous
#Ordered : no
#Indexed :no
#mutable : yes
#Duplicates : no

data = {11,21,51,101,21,11}
data1 = {11, 90.80, True, "Hello"}
print("first set data :",data)
print("Data at hetrogenous :",data1)
print("Data at ordered :",data1)
#print("Data at index 2 :",data1[2])
print("Data with duplicate:",data)

print("set is mutable")
#insert element in set
data.add(211)
print("data after insertion : ",data)
data.discard(201)
print("data after remove : ",data)