'''Create a program that asks the user to enter their name and their age. 
Print out a message addressed to them that tells them the year that they will turn 100 years old. 
Note: for this exercise, the expectation is that you explicitly write out the year 
(and therefore be out of date the next year).'''

name = str(input("enter your name: "))
age = int(input("enter your current age: "))
year = 2026 - age + 100
print ( name + " , will turn 100 years old in  " + str(year) )
