#Nested if statement
age = int(input("Enter your age:"))
eats_pizza = True
exercise = False
if(age < 30):
    if(eats_pizza ):
        print("Unfit")
    else:
        print("Fit")
if(age > 30):
    if(exercise):
        print("Unfit")
    else:
        print("Fit")

#converting the above program into ternary operator program
age = int(input("Enter your age:"))
eats_pizza = True
exercises = False
print("Unfit"if (eats_pizza) else "Fit") if(age < 30)else("Unfit"if (exercises) else "Fit")

#Ternary Operator
#Normal if-else statement
num = int(input("Enter a number:"))
if (num % 2 == 0):
    print(num,"is an even number")
else:
    print(num,"is a odd number")
#Now using ternary operator,
num = int(input("Enter a number:"))
print("Even"if num % 2==0 else "odd")

#Example2
age = int(input("Enter your age:"))
print("Child"if (age < 18) else"Adult")

#Quiz
age = int(input("Enter your age:"))
income = int(input("Enter your income:"))
if (age < 18):
    message = "You are too young to work."
elif(age >= 18) and (age <= 25):
    if (income < 30000):
        message = "You are eligible for a student discount."
    else:
        message = "You are eligible for a regular discount."
else:
    message = "You are eligible for a regular discount."

print(message)

#ODD or EVEN
num = int(input("Enter  a number:"))
if(num%2==0):
    print(num, "is an even number")
else:
    print(num, "is a odd number")

#now using Ternary operator
num = int(input("Enter a number:"))
print(num,"is an even number"if(num % 2 == 0) else "is a odd number")
