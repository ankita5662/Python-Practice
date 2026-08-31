'''Create a program that asks the user to enter their name and their age. 
Print out a message addressed to them that tells them the year that they will turn 100 years old. 
Note: for this exercise, the expectation is that you explicitly write out the year 
(and therefore be out of date the next year).'''

name = str(input("enter your name: "))
age = int(input("enter your current age: "))
year = 2026 - age + 100
print ( name + " , will turn 100 years old in  " + str(year) )


'''Extras:
1. Add on to the previous program by asking the user for another number and 
printing out that many copies of the previous message
2. Print out that many copies of the previous message on separate lines. 
(Hint: the string "\n is the same as pressing the ENTER button)'''

# 1. 
name = str(input("enter your name: "))
age = int(input("enter your current age: "))
num = int(input("enter a number: "))
year = 2026 - age + 100
print (num*(name + " , will turn 100 years old in  " + str(year)))

# 2. 
name = str(input("enter your name: "))
age = int(input("enter your current age: "))
num = int(input("enter a number: "))
year = 2026 - age + 100
message = name + " , will turn 100 years old in  " + str(year) + "\n"
print(message*num)