#Avike Seal
#Hangman game

import random
import time

print("Welcome to the Hangman game by avike\n")
name  = input("Enter your name: ")
print("Hello " + name + "! Best of Luck!" )

time.sleep(2) #predefined function sleep used to pause the program for given amount of seconds
            
print("The game is about to start!\n Let's play Hangman!")
time.sleep(3)

def main():
    global count
    global display
    global word
    global already_guessed
    global length
    global play_game
    words_to_guess = ["january", "border", "image", "film", "promise", "kids", "lungs", "doll", "rhyme", "damage", "plants"]
    words = random.choice(words_to_guess)
    length = len(word)
    count = 0
    display = '_' * length
    already_guessed = []
    play_game = ""
