'''Write a function that takes an ordered list of numbers (order from smallest to largest) and another number. 
The function decides whether or not the given number is inside the list and returns (then prints) an 
appropriate boolean. 
Extras:
1. Use binary search'''

def list1(num , target):
    return target in num

a = [5,67,78,88,90,93,100,105,107]
print(list1(a, 93))     
print(list1(a, 1)) 

# Extras:
# 1.
def binary_search(numbers, target):
    low = 0
    high = len(numbers) - 1

    while low <= high:
        mid = (low + high) // 2

        if numbers[mid] == target:
            return True
        elif numbers[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return False

a = [10, 20, 30, 40, 50, 60, 70, 80, 90]
print(binary_search(a, 70))
print(binary_search(a, 25))