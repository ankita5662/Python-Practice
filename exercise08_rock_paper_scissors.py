''' Q. Make a two-player Rock-Paper-Scissors  game. (Hint: Ask for player plays (using input), 
compare them, print out a message of congratulations to the winner, and ask if the players want to 
start a new game).
Remember the rules:
1. Rock beats  scissors
2. Scissors beats paper
3. Paper beats rock'''

import random
print ("Game of Rock, Paper, Scissors Begins")
choices = ["rock", "paper", "scissors"]
computer_choice = random.choice(choices)
user_choice = input("Enter rock, paper, or scissors: ")

print("Computer chose:", computer_choice)

if user_choice == computer_choice:
    print("It's a tie!")
elif user_choice == "rock" and computer_choice == "scissors":
    print("You win!")
elif user_choice == "paper" and computer_choice == "rock":
    print("You win!")
elif user_choice == "scissors" and computer_choice == "paper":
    print("You win!")
else:
    print("Computer wins!")