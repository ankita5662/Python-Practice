'''Create a program that will play the “cows and bulls” game with the user. 
The game works like this:
Randomly generate a 4-digit number. Ask the user to guess a 4-digit number. 
For every digit that the user guessed correctly in the correct place, they have a “cow”. 
For every digit the user guessed correctly in the wrong place is a “bull.” 
Every time the user makes a guess, tell them how many “cows” and “bulls” they have. 
Once the user guesses the correct number, the game is over. Keep track of the number of
guesses the user makes throughout the game and tell the user at the end.'''

import random
print("Game of the Cows and the Bulls Begin!")

num = random.randint(1000, 9999)
num_str = str(num)

num1 = int(input("Enter your 4 digit guess: "))   
num1_check = str(num1)

while num1_check != num_str:
    for i in range(4):
        if num_str[i] == num1_check[i]:
            print("Cow!")
        elif num1_check[i] in num_str:
            print("Bull!")
    
    num1 = int(input("Enter your 4 digit guess: "))   
    num1_check = str(num1)

print("Congratulations! You guessed it!")