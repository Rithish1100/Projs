from random import randint

EASY_LEVEL_TURNS=10
HARD_LEVEL_TURNS=5
turns=0
def check_answer(user_guess,actual_answer,turns):
    if user_guess > actual_answer:
        print("Too high")
        return turns-1
    elif user_guess < actual_answer:
        print("Too low")
        return turns-1
    else:
        print("You got it{actual_answer}")

def set_difficulty():
    level = input("choose a difficulty,Type 'easy' or 'hard':")
    if level == "easy":
        return EASY_LEVEL_TURNS
    else:
        return HARD_LEVEL_TURNS
def game():
    print("welcome to the number guessing game")
    print("I am thinking of a number between 1 to 100")
    answer=randint ( 1,100 )
    print(f"the correct answer is{answer}")

    turns=set_difficulty()

    guess=0
    while guess != answer:
        print(f"you have{turns}attempts remaining to guess the number")
        guess=int(input("make a guess"))
        turns=check_answer(guess,answer,turns)
        if turns==0:
            print("you've run out of guess you lose.")
            return
game()     