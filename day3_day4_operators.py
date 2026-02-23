#ASSIGNMENT OPERATOR
balance = 4000.50
print(balance)

#ARITHMATIC OPERATOR
print(10+5*3)
print(20-10/5*2)
print(20-2.0*2)

a = 75
b = 14
print(a/b)
print(a//b)
print(a%b)

#to find a to the power b
a = 25
b = 6
c = a**b
print(type(c),c)

print(2**3**(2%10))
#the above calculation is done as following
print(2%10)    #2
print(3**2)    #9
print(2**9)    #512

#RELATIONAL OPERATOR
a = 25
b = 12
print(a<b)
print(a>b)
print(a>=b)
print(a==b)
print(a!=b)
a = b
print(a==b)

#quiz
a = "Nisha"
b = "nisha"
print(a==b)
print(a<b)

#ASCII value
print("N:",ord('N'))
print("n:",ord('n'))
print(a<b)

a = "Nishu"
b = "Nisha"
print(a==b)
print(a<b)
print("u:",ord('u'))
print("a:",ord('a'))
print(a>b)

#AUGMEMNTED OPERATORS
a = 15
b = 25
a = a+2
print(a)
a = a+b
print(a)
a += 2
b *= 3
print("a =",a,"b =",b)
b /= 5
print(b)
b %= 4
print(b)

#Quiz(Augmented Operators)-Bank Acc
name, balance = "Nisha",500.0
print("Before Intrest:",balance)
#Update the balance with 7% interest
balance += (7/100 * balance)
print("After Intrest:",balance)

#MEMBERSHIP OPERATOR
list = [1,2,3,4,'5',6]
print(2 in list)
print(9 in list)
print(9 not in list)
print(5 in list)
print('5' in list)
name = 'Nisha Mary'
print('n' in name)
print('M' in name)

#LOGICAL OPERATORS
#and
num1 = 25
num2 = 15
statement1 = (num1==25)
statement2 = (num2==25)
print(statement1 and statement2)

num1 = 100
num2 = 100
statement1 = (num1==100)
statement2 = (num2==100)
print(statement1 and statement2)

#or
num1 = 15
num2 = 850
statement1 = (num1==15)
statement2 = (num2==850)
print(statement1 or statement2)

#not
print(not(True))
print(not(False))

num = 10
print(num < 5 and num < 15)
print(num % 2 == 0 or num % 3 == 0)
print(not(num==0))

#BITWISE OPERATOR
A = 2
B = 3
print(A & B)
print(A | B)

#right shift
a = 2
b = 3
print(a>>1)
#left shift
print(a<<1)

x = 10 #1010
y = 4  #0100
print(x & y)
print(x | y)
print(x ^ y)
