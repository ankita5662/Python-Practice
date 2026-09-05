'''Q. Take two lists,and write a program that returns a list that contains only the elements 
that are common between the lists (without duplicates). 
Make sure your program works on two lists of different sizes.
Extras:
1. Randomly generate two lists to test this.
2. Write this in one line of Python.'''

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 16]
c = []
for i in a:
   if i in b:
    c.append(i)
print (c)


# Extras:
# 1. 

import random
a = [random.randint(1, 100) for _ in range(10)]
print (a)
b = [random.randint(1, 100) for _ in range(10)]
print(b)
c = []
for i in a:
   if i in b:
    c.append(i)
print (c)

# 2. 
print( [ i for i in a if i in b ] )

