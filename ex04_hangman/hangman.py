import random
from words import Words
import os

used_letters=[]
shown=""

def game():    
    lives=0
    shown = list("")
    print("Welcome to Hangman, try to find the secret word before you get hanged")
    print("!rules to learn more about the game")
    secret = random.choice(Words.english_words)
    for letters in secret:
        if(letters == '-' or letters == " "):
            shown.append(letters)
        else:
            shown.append("_")
    while True:
        print(Words.HANGMANPICS[lives])
        print(''.join(shown))
        
        if(''.join(shown) == secret):
            print('GG, you win!')
            break
        if(lives == 9):
            print(f'Too bad, You lost! The secret word was {secret}')
            break

        choice = input("Your input : ").lower()
        if(len(choice) > 1 or not choice.isalpha()):
            print("Please type in only one letter")
            continue
        if(choice == "!rules"):
            print(Words.rules)
        elif (choice in secret):
            for (index,letter) in enumerate(secret):
                if(choice == letter):
                    shown[index] = choice
        else:
            lives += 1

if __name__ == "__main__":
    while True:
        game()
        answer = input('Do you want to play again ? (y/n)')
        if (answer!= 'y'):
            break

