# Guess Game

import random

name = input("enter your name: ")
print("hello", name, "welcome to the game")

words = ["geeks","perfect","plan","chocolate","board","apple"]
word = random.choice(words)

print("guess the character")
guesses = ""
turns = 10

while turns > 0:

    failed = 0
    for char in word:
        if char in guesses:
            print(char)

        else:
            print("_")

            failed += 1
    if failed == 0:
        print("you win")
        print("the word is: ", word)
        break

    guess = input("guess a character: ")
    guesses += guess

    if guess not in word:

        turns-=1
        print("wrong")
        print("you have ",+ turns,"more guesses")

        if turns == 0:
            print("You loose")
        
