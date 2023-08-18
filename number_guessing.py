

import random

print("Welcome to the Number Guessing Game!\n I'm thinking of a number between 1 and 100.")

EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5


def check_answer(users_choice, computer_number, turns):
    if users_choice > computer_number:
        print("Too high.")
        return turns - 1
    elif users_choice < computer_number:
        print("Too low.")
        return turns - 1
    else: 
        print(f"You got it! The answer was {computer_number}.")

def set_difficulty():
    level = input("Choose a difficulty. Type 'easy' or 'hard': ")
    if level == "easy":
        return EASY_LEVEL_TURNS
    else:
        return HARD_LEVEL_TURNS


def game():
    computer_number = random.randint(1,100)
    turns = set_difficulty()
    users_choice = 0
    
    while users_choice != computer_number:
        print(f"You have {turns} attempts remaining to guess the number.")
        users_choice = int(input("Make a guess: "))
        turns = check_answer(users_choice, computer_number, turns)
        if turns == 0:
            print("You are out of turns.")
            return 


game()
