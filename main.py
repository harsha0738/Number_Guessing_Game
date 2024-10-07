import random

EASY_LEVEL_TURNS = 10

HARD_LEVEL_TURNS = 5

answer = random.randint(1,100)

print(f"the actual answer is {answer}")

def check_answer(user_guess, actual_answer):
    if user_guess > actual_answer:
        print("Too High!")
    elif user_guess < actual_answer:
        print("Too Low!")
    elif user_guess == actual_answer:
        print(f"You Got it!. The answer is {answer}")
    else:
        print("Something error occurred.")

def set_difficulty():
    level = input("Choose a difficulty. Type 'easy' or 'hard' : ").lower()
    if level == "easy":
        print(f"You have {EASY_LEVEL_TURNS} attempts remaining to guess the number.")
    elif level == "hard":
        print(f"You have {HARD_LEVEL_TURNS} attempts remaining to guess the number.")
    else:
        print("Something error has occurred.")


print("Welcome to Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")

set_difficulty()

guess = 0
while guess != answer:
    guess = int(input("Make a Guess : "))

    check_answer(guess, answer)














