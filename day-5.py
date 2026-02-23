import random
from hangman import word_list
stages= [''' 6
         
         ''',''' 5 ''','''4''','''3''','''2''','''1''','''0''']
life=6
chosen=random.choice(word_list)
print(chosen)
place=""
word_length=len(chosen)
for position in range(word_length):
    place+="_"
print(place )

game_over = False
correct=[]
while not game_over:
    guess=input("Guess a letter :").lower()
    if guess in correct:
        print("you already guessed{guess}")
    display=""

    for letter in chosen:
        if letter == guess:
            display += letter
            correct.append(guess)
        elif letter in correct:
            display+=letter
        else:
            display +="_"
    print(display)

    if guess not in  chosen:
        life-=1
        print("you guessed it wrong")
        if life ==0:
            game_over=True
            print("you lose")
    
    if "_"not in display:
        game_over= True
        print("you win")

    print(stages[life])

             