'''Q. Write a password generator in Python. Be creative with how you generate passwords - 
strong passwords have a mix of lowercase letters, uppercase letters, numbers, and symbols. 
The passwords should be random, generating a new password every time the user asks for a 
new password. Include your run-time code in a main method. 
Extra:
1. Ask the user how strong they want their password to be. 
For weak passwords, pick a word or two from a list'''

import string
import random 

all_characters = string.ascii_letters + string.digits + string.punctuation
one_char = random.choice(all_characters)
length = int(input("How many characters do you want in your password? "))
password = ""
for i in range(length):
    char = random.choice(all_characters)
    password = password + char
print(password)

