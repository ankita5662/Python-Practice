'''Ask the user for a number and determine whether the number is prime or not.'''

def is_prime(num):
    if num < 2:
        return False
    for i in range (2, num) :
        if num % i == 0:
            return False
    return True

number = int(input("enter a number to check primality: "))
if is_prime(number):
    print (number , "is prime")
else:
    print(number , "is not prime")
