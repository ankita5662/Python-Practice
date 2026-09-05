'''Q. Ask the user for a string and print out whether this string is a palindrome or not. 
(Note- A palindrome is a string that reads the same forwards and backwards.)'''

word = str(input("enter a word: "))
reverse = word [::-1]
print(reverse)
if word == reverse:
    print("This word is a palindrome")
else:
    print("This word is not a palindrome")