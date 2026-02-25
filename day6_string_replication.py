#STRING REPLICATION
'''a = "Yesappa i love you always"
print(a*50)

#String Concatenation
str1 = "Nisha"
str2 = "Hariharan"
print(str1+str2)'''

#String Replication and Concatenation
#problem: print 20 stars in 1st line and Happy Holidays! in 2nd line
# and again 20 stars in 3rd line 
stars = "*"
greeting = "Happy" + "\tHolidays!"
print(stars * 20, greeting, stars * 20, sep = "\n")
#(or)
print(stars * 20 + '\n' + greeting + '\n' + stars * 20)