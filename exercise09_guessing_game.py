'''Generate a random number between 1 and 9 (including 1 and 9). Ask the user to guess the number, 
then tell them whether they guessed too low, too high, or exactly right.
Extras:
1. Keep the  game going until the user types “exit”
2. Keep track of how many guesses the user has taken, and when the game ends, print this out. '''

import random
print("Let's Play: Guess the number")
num = random.randint(1, 10)
guess = int(input("Guess a number between 1 to 10: "))
while guess != num:
    if guess > num:
        print ("You guessed too high")
    else:
        print ("You guessed too low")
    guess = int(input("Guess again: "))

print("Congratulations, you guessed it!")

# Extras:
# 1.
print("Let's Play: Guess the number")
num = random.randint(1, 10)
guess_input = input("Guess a number between 1 to 10 (or type 'exit' to quit): ")

while guess_input.lower() != "exit":
    guess = int(guess_input)
    
    if guess == num:
        print("Congratulations, you guessed it!")
        break
    elif guess > num:
        print("You guessed too high")
    else:
        print("You guessed too low")
    
    guess_input = input("Guess again (or type 'exit' to quit): ")

if guess_input.lower() == "exit":
    print("Thanks for playing!")

#2.
print("Let's Play: Guess the number")
num = random.randint(1, 10)
attempts = 0
guess_input = input("Guess a number between 1 to 10 (or type 'exit' to quit): ")

while guess_input.lower() != "exit":
    guess = int(guess_input)
    attempts += 1
    
    if guess == num:
        print("Congratulations, you guessed it in", attempts, "attempts!")
        break
    elif guess > num:
        print("You guessed too high")
    else:
        print("You guessed too low")
    
    guess_input = input("Guess again (or type 'exit' to quit): ")

if guess_input.lower() == "exit":
    print("Thanks for playing! You made", attempts, "guesses.")