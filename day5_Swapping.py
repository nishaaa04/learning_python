#Swapping
a = 5
b = 7
print(a,b)
temp = a
a = b 
b = temp
print(a,b)
#(or)
a,b = b,a
print(a,b)

a = 5
b = 10
a += b
b = a-b
a -= b
print(a,b)