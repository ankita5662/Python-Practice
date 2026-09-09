'''write a program that returns a list that contains only the elements that are common 
between the lists (without duplicates). Make sure your program works on two lists of
different sizes. 
Write this in one line of Python using at least one list comprehension. '''

import random 

a = random.sample(range (1,30), 13)
b = random.sample(range (1,30), 16)
print (a) 
print (b)
result = [i for i in a if i in b]
print(result)
