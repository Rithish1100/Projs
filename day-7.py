import random

words = ["apple", "banana", "grapes", "orange", "mango"]
word = random.choice(words)

guessed = ["_"] * len(word)
attempts = 6
used_letters = []

print("Welcome to Hangman Game!")

while attempts > 0 and "_" in guessed:
    print("\nWord:", " ".join(guessed))
    print("Attempts left:", attempts)
    print("Used letters:", used_letters)

    guess = input("Enter a letter: ").lower()

    if guess in used_letters:
        print("You already guessed that letter!")
        continue

    used_letters.append(guess)

    if guess in word:
        for i in range(len(word)):
            if word[i] == guess:
                guessed[i] = guess
        print("Correct!")
    else:
        attempts -= 1
        print("Wrong!")

if "_" not in guessed:
    print("\nYou won! The word was:", word)
else:
    print("\nYou lost! The word was:", word)