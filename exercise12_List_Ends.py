'''Write a program that takes a list of numbers (for example, a = [5, 10, 15, 20, 25]) and makes a new list of only the first 
and last elements of the given list. For practice, write this code inside a function.'''

def list_end(a_list):
    return [a_list[0] , a_list[-1]]

import random

a = random.sample(range(1,20), 10)
print (a)

result = list_end(a)
print(result)


