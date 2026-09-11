'''Write a program (function!) that takes a list and returns a new list that contains 
all the elements of the first list minus all the duplicates. 
Extras:
1. Write two different functions to do this - one using a loop and constructing a list, 
and another using sets.
2. Go back and do Exercise 5 using sets, and write the solution for that in a different function.'''

import random

def list1(n):
    b = []
    for i in n:
        if i not in b:
            b.append(i)
    return b

a = random.choices( range(1 , 10) , k=12)
print (a)
print ( list1 (a) )

# Extras:
# 1. 
def list2(n):
    return list(set(n))
print("Set version:", list2(a))

# 2. 
def list_overlap_set(a, b):
    return list(set(a) & set(b))

x = [1, 2, 3, 4, 5]
y = [3, 4, 5, 6, 7]
print("Overlap (set):", list_overlap_set(x, y))